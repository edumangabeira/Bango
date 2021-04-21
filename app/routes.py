from app import app
from app.forms import GastosForm, LoginForm
# from updateSheets import atualiza_tabela
from flask import render_template, request, flash, redirect
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse

import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import ast
import os
import datetime


def atualiza_tabela(categoria, quantia):
    '''
    atualiza_tabela(categoria, quantia)

    Recebe valores dados pelo usuário na tela do app
    e salva numa planilha do google sheets.
    '''

    # valida credenciais
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    # credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    ws_credentials = {
        "type": os.environ.get('TYPE'),
        "project_id": os.environ.get('PROJECT_ID'),
        "private_key_id": os.environ.get('PRIVATE_KEY_ID'),
        "private_key": os.environ.get('PRIVATE_KEY').replace("\\n", "\n"),
        "client_email": os.environ.get("CLIENT_EMAIL"),
        "client_id": os.environ.get("CLIENT_ID"),
        "auth_uri": os.environ.get("AUTH_URI"),
        "token_uri": os.environ.get("TOKEN_URI"),
        "project_id": os.environ.get("PROJECT_ID"),
        "auth_provider_x509_cert_url":os.environ.get("AUTH_PROVIDER_CERT_URL"),
        "client_x509_cert_url":os.environ.get("CLIENT_CERT_URL")
    }
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(ws_credentials, scope)
    client = gspread.authorize(credentials)

    # configurações
    gastos = client.open_by_key(os.environ.get('TABELA_GASTOS')).sheet1

    # adiciona valores
    novo_gasto = pd.DataFrame(
        {
        # operação computacionalmente custosa
        'id': [len(gastos.get_all_values())], \
        'categoria': [categoria], \
        'quantia': [quantia], \
        'data': [datetime.date.today().strftime("%d/%m/%Y")], \
        'hora': [datetime.datetime.now().strftime("%H:%M")]
        }
        )
    gastos.append_rows(novo_gasto.values.tolist())

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
	form = GastosForm()
	if form.validate_on_submit():
		atualiza_tabela(form.categoria.data, form.quantia.data)
	return render_template('index.html', title='Bango', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.usuario.data).first()
        if user is None or not user.check_password(form.senha.data):
            flash('Usuário ou senha inválidos.')
            return redirect(url_for('login'))
        login_user(user, remember=True)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))