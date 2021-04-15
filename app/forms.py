from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class GastosForm(FlaskForm):
    categoria = StringField('Categoria', validators=[DataRequired()])
    quantia = StringField('Quantia', validators=[DataRequired()])
    salvar = SubmitField('Salvar')