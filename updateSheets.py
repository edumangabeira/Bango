import gspread
import pandas as pd
import configparser
from oauth2client.service_account import ServiceAccountCredentials
import datetime


def atualiza_tabela(categoria, quantia):
	'''
	atualiza_tabela(categoria, quantia)

	Recebe valores dados pelo usuário na tela do app
	e salva numa planilha do google sheets.
	'''

	# valida credenciais
	scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
	credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
	client = gspread.authorize(credentials)

	# configurações
	config = configparser.ConfigParser()
	config.read_file(open('app.cfg'))
	gastos = client.open_by_key(config['SHEETS']['TABELA_GASTOS']).sheet1

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