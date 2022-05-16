
#----- Librerias -----#
import numpy as np
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
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField,RadioField, DateField, DateTimeField, SelectField, SelectMultipleField, TimeField)
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
    clave_per = IntegerField('Clave: ', validators=[InputRequired()], render_kw={"placeholder": "Ingrese la clave"})
    nombre_per = StringField('Nombre: ', validators=[InputRequired()], render_kw={"placeholder": "Ingrese su nombre"})
    paterno = StringField('Apellido Paterno: ', validators=[InputRequired()], render_kw={"placeholder": "Ingrese su apellido paterno"})
    materno = StringField('Apellido Materno: ', validators=[InputRequired()], render_kw={"placeholder": "Ingrese su apellido materno"})
    edad = IntegerField('Edad: ', validators=[InputRequired()], render_kw={"placeholder": "Ingrese su edad"})
    genero = SelectField('Genero: ', choices=[("Hombre"), ("Mujer")], validators=[InputRequired()], render_kw={"placeholder": "Ingrese la clave"})
    edo_civil = SelectField('Genero: ', choices=[("Solter@"), ("Casad@"),("Viud@"),("Separad@"),("Divorciad@")], validators=[InputRequired()])
    fecha_nac = DateField('Fecha de Nacimiento: ', validators=[InputRequired()])
    fe_inicio = DateField('Fecha Inicio: ', validators=[InputRequired()])
    fe_fin = DateField('Fecha Fin: ', validators=[InputRequired()])
    puesto = SelectField('Genero: ', choices=[("Gerente"), ("Cajero"), ("Asistente"),("Acomodador"),("Chofer")], validators=[InputRequired()])
    sueldo = StringField('Sueldo: ', validators=[InputRequired()], render_kw={"placeholder": "Ingrese su sueldo"})
    hora_entrada = TimeField('Hora Entrada: ', validators=[InputRequired()], render_kw={"placeholder": "Ingrese la hora en formato 'HH:MM:SS'"})
    hora_salida = TimeField('Hora Salida: ', validators=[InputRequired()], render_kw={"placeholder": "Ingrese la hora en formato 'HH:MM:SS'"})
    submit = SubmitField('Registrar', validators=[InputRequired()])

class Actualizar(FlaskForm):
    clave_per1 = IntegerField('Clave: ', validators=[InputRequired()], render_kw={"placeholder": "Ingrese la clave"})
    nombre_per1 = StringField('Nombre: ', validators=[InputRequired()], render_kw={"placeholder": "Ingrese su nombre"})
    paterno1 = StringField('Apellido Paterno: ', validators=[InputRequired()], render_kw={"placeholder": "Ingrese su apellido paterno"})
    materno1 = StringField('Apellido Materno: ', validators=[InputRequired()], render_kw={"placeholder": "Ingrese su apellido materno"})
    edad1 = IntegerField('Edad: ', validators=[InputRequired()], render_kw={"placeholder": "Ingrese su edad"})
    genero1 = SelectField('Genero: ', choices=[("Hombre"), ("Mujer")], validators=[InputRequired()], render_kw={"placeholder": "Ingrese la clave"})
    edo_civil1 = SelectField('Genero: ', choices=[("Solter@"), ("Casad@"),("Viud@"),("Separad@"),("Divorciad@")], validators=[InputRequired()])
    fecha_nac1 = DateField('Fecha de Nacimiento: ', validators=[InputRequired()])
    clave_contra1 = IntegerField('Clave: ', validators=[InputRequired()], render_kw={"placeholder": "Ingrese la clave del contrato"})
    fe_inicio1 = DateField('Fecha Inicio: ', validators=[InputRequired()])
    fe_fin1 = DateField('Fecha Fin: ', validators=[InputRequired()])
    puesto1 = SelectField('Genero: ', choices=[("Gerente"), ("Cajero"), ("Asistente"),("Acomodador"),("Chofer")], validators=[InputRequired()])
    sueldo1 = StringField('Sueldo: ', validators=[InputRequired()], render_kw={"placeholder": "Ingrese su sueldo"})
    hora_entrada1 = TimeField('Hora Entrada: ', validators=[InputRequired()], render_kw={"placeholder": "Ingrese la hora en formato 'HH:MM:SS'"})
    hora_salida1 = TimeField('Hora Salida: ', validators=[InputRequired()], render_kw={"placeholder": "Ingrese la hora en formato 'HH:MM:SS'"})
    submit1 = SubmitField('Actualizar', validators=[InputRequired()])

class ActualizarCliente(FlaskForm):
    clave_per2 = IntegerField('Clave: ', validators=[InputRequired()], render_kw={"placeholder": "Ingrese la clave"})
    nombre_per2 = StringField('Nombre: ', validators=[InputRequired()], render_kw={"placeholder": "Ingrese su nombre"})
    paterno2 = StringField('Apellido Paterno: ', validators=[InputRequired()], render_kw={"placeholder": "Ingrese su apellido paterno"})
    materno2 = StringField('Apellido Materno: ', validators=[InputRequired()], render_kw={"placeholder": "Ingrese su apellido materno"})
    edad2 = IntegerField('Edad: ', validators=[InputRequired()], render_kw={"placeholder": "Ingrese su edad"})
    genero2 = SelectField('Genero: ', choices=[(1, "Hombre"), (2, "Mujer")], validators=[InputRequired()], render_kw={"placeholder": "Ingrese la clave"})
    edo_civil2 = SelectField('Edo_Civil: ', choices=[("Solter@"), ("Casad@"),("Viud@"),("Separad@"),("Divorciad@")], validators=[InputRequired()])
    fecha_nac2 = DateField('Fecha de Nacimiento: ', validators=[InputRequired()])
    clave_cli2 = IntegerField('Clave: ', validators=[InputRequired()], render_kw={"placeholder": "Ingrese la clave del cliente"})
    credito_clien2 = StringField('Credito: ', validators=[InputRequired()])
    tipo_clien2 = StringField('Tipo: ', validators=[InputRequired()])
    submit2 = SubmitField('Actualizar', validators=[InputRequired()])
