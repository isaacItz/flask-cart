#----- Librerias -----#
from socket import NI_NUMERICHOST
from email.mime import application
from re import S
from xmlrpc.client import APPLICATION_ERROR
from flask import Flask
from flask import request
from flask import make_response
from flask import render_template
from flask import url_for
from flask import session, redirect, flash # Usadas para sesiones de usuario


#----- Librerias de WTF -----#
from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField,RadioField, DateField, DateTimeField)
from wtforms import SubmitField
from wtforms.validators import InputRequired, Length, NumberRange

#----- Librerias de Bootstrap -----#
from flask_bootstrap import Bootstrap
#------------------------------------#
app = Flask(__name__)
APPLICATION = Flask(__name__)
APPLICATION.SECRET_KEY = "ININ_2022"


#----- Configuracion de sessiones permanentes -----#
@app.before_request
def session_management():
    session.permanent = True

#----- Bootstrap -----#
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'ININ-mate-2022'


class Alta(FlaskForm):
    clave = IntegerField('Clave: ', validators=[InputRequired()], render_kw={"placeholder": "Ingrese la clave"})
    nombre = StringField('Nombre: ', validators=[InputRequired()], render_kw={"placeholder": "Ingrese el nombre"})
    numero = StringField('Numero: ', validators=[InputRequired()], render_kw={"placeholder": "Ingrese el numero del comic"})
    paginas = IntegerField('Numero Paginas: ', validators=[InputRequired()], render_kw={"placeholder": "Ingrese el numero de paginas"})
    editorial = StringField('Editorial:', validators=[InputRequired()], render_kw={"placeholder": "Ingrese la editorial"})
    autor = StringField('Autor: ', validators=[InputRequired()], render_kw={"placeholder": "Ingrese el autor"})
    anio = DateField(validators=[InputRequired()], render_kw={"placeholder": "Ingrese el año"})
    submit = SubmitField('Registrar', validators=[InputRequired()])