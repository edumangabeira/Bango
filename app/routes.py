from flask import render_template
from app import app
from app.forms import GastosForm
from updateSheets import atualiza_tabela

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	form = GastosForm()
	if form.validate_on_submit():
		atualiza_tabela(form.categoria.data, form.quantia.data)
	return render_template('index.html', title='Bango', form=form)