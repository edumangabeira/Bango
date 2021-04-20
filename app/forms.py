from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired

class GastosForm(FlaskForm):
    categoria = StringField('Categoria', validators=[DataRequired()])
    quantia = StringField('Quantia', validators=[DataRequired()])
    salvar = SubmitField('Salvar')

class LoginForm(FlaskForm):
	usuario = StringField('Usuário', validators=[DataRequired()])
	senha = PasswordField('Senha super secreta', validators=[DataRequired()])
	entrar = SubmitField('Entrar')

