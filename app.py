import email
from datetime import datetime
import random
from ensurepip import bootstrap
from flask import Flask
from flask import request
from flask import make_response
from flask import render_template
from flask import url_for
from flask import session, redirect, flash

import DcComics
import sanborns as sn
import MyConn

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, BooleanField
from wtforms import HiddenField, DateField, DateTimeField, IntegerField, DecimalField
from wtforms.validators import DataRequired
from wtforms.validators import NumberRange
from flask_bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'WelcomePython2022'

@app.before_request
def session_management():
    session.permanent = True

@app.route("/quick-add/<id>")
def quick_add(id):
    if 'cart' not in session:
        session['cart'] = []

    session['cart'].append({'id': id, 'quantity': 1})
    session.Modified = True

    return redirect(url_for('list_cart'))

@app.route("/list-cart")
def list_cart():
    print(type(session))
    return (session)

@app.route("/setTienda/<string:tienda>", methods = ['GET', 'POST'])
def set_tienda(tienda):
    if request.method == 'GET':
        aux = "/" + tienda + "/altas"
        resp = make_response(redirect(aux))
        resp.set_cookie('tienda', tienda)
        return resp

def get_tienda():
    tienda = request.cookies.get('tienda')
    return tienda if tienda else 'dc'

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('plantilla4.html', tienda = get_tienda())

@app.route('/dccomics/<name>', methods=['GET', 'POST'])
def dccomics(name):
    if(name == "altas"):
        form = DcComics.Alta()
        clave = None
        nombre = None
        numero = None
        paginas = None
        editorial = None
        autor = None
        anio = None
        if form.validate_on_submit():
            clave = request.form["clave"]
            nombre = request.form["nombre"]
            numero = request.form["numero"]
            paginas = request.form["paginas"]
            editorial = request.form["editorial"]
            autor = request.form["autor"]
            anio = request.form["anio"]
            MyConn.insertarComic(clave = clave, nombre = nombre, numero = numero, paginas = paginas, editorial = editorial, autor = autor, anio = anio)
            return render_template("plantilla4A.html", form=form, aux=clave)
        return render_template("plantilla4A.html", form=form, aux=clave)
    if(name == "consultas"):
        flash('Tuplas: ', 'info')
        sql = "SELECT *FROM comic order by cve_comic"
        r = MyConn.Consulta(SQL = sql)
        return render_template('plantilla4B.html', tema = "Consultas de Comics", list = r)

@app.route('/sanborns/<name>', methods=['GET', 'POST'])
def caja(name):
    if(name == "caja"):
        flash('Tuplas: ', 'info')
        sql = "select codbar_pro, marca_pro, modelo_pro, procesador_pro, precio_pro, imagen_pro from producto;"
        r = MyConn.Consulta(SQL = sql)
        return(render_template('caja.html', list = r))
    if(name == "inventario"):
        return(render_template('inventario.html'))
    if(name == "carrito"):
        print(type(session))
        lista = []
        lis = session['cart']
        lista = get_detalles(lis)
        return(render_template('carrito.html', lista = lista, folio = build_folio(), fecha = build_date()))

def get_detalles(carrito):
    lista = []
    for i in carrito:
        sql = 'select codbar_pro, marca_pro, modelo_pro, procesador_pro, precio_pro, imagen_pro from producto where codbar_pro = '+ i.get('id')
        r = MyConn.Consulta(SQL = sql)
        lista.append(r[0] + (i.get('quantity'),))
    return lista

@app.route('/test-query/<id>')
def test(id):
    sql = 'select codbar_pro, marca_pro, modelo_pro, procesador_pro, precio_pro, imagen_pro from producto where codbar_pro = '+ id
    r = MyConn.Consulta(SQL = sql)
    return string(r[0]);

@app.route('/sanborns/altas', methods=['GET', 'POST'])
def altas_sanborns():
    formu = sn.Alta()
    MyConn.actualizarContrato(fechaInicio = "1999-10-14", fechaFin = "1999-10-15", puesto = "Acomodador", sueldo = "9999", horaEntrada = "23:00:00", horaSalida = "10:00:00", cve_contra = 136)
    MyConn.actualizarPersona(nombre_per = "Eduardo", paterno_per = "Reyes", materno_per = "Doming", edad_per = 22, genero_per = "hombre", edocivil = "soltero", fechaNac_per = "2022-10-10", cve_per = 122)
    clave_per = None
    nombre_per = None
    paterno = None
    materno = None
    edad = None
    genero = None
    edo_civil = None
    fecha_nac = None
    fe_inicio = None
    fe_fin = None
    puesto = None
    sueldo = None
    hora_entrada = None
    hora_salida = None
    if formu.validate_on_submit():
        clave_per = request.form["clave_per"]
        nombre_per = request.form["nombre_per"]
        paterno = request.form["paterno"]
        materno = request.form["materno"]
        edad = request.form["edad"]
        genero = request.form["genero"]
        edo_civil = request.form["edo_civil"]
        fecha_nac = request.form["fecha_nac"]
        fe_inicio = request.form["fe_inicio"]
        print(fe_inicio)
        fe_fin = request.form["fe_fin"]
        puesto = request.form["puesto"]
        sueldo = request.form["sueldo"]
        hora_entrada = request.form["hora_entrada"]
        hora_salida = request.form["hora_salida"]
        aux_entrada = hora_entrada + ":00"
        aux_salida = hora_salida + ":00"
        MyConn.insertarPersona(cve_per = clave_per, nombre_per=nombre_per, paterno_per = paterno, materno_per = materno, edad_per = edad, genero_per = genero, edocivil = edo_civil, fechaNac_per = fecha_nac)
        MyConn.insertarContrato(cve_contra = None, fechaIni_contra = fe_inicio, fechaFin_contra = fe_fin, puesto_contra = puesto, sueldo_contra = sueldo, hrEntrada_contra = aux_entrada, hrSalida_contra = aux_salida, cve_perF = clave_per)
        #MyConn.actualizarContrato(fechaInicio = "1999-10-14", fechaFin = "1999-10-15", puesto = "Acomodador", sueldo = "9999", horaEntrada = "23:00:00", horaSalida = "10:00:00", cve_contra = 135)
        #MyConn.actualizarPersona(nombre_per = "Eduardo", paterno_per = "Reyes", materno_per = "Doming", edad_per = 22, genero_per = "hombre", edocivil = "soltero", fechaNac_per = "2022-10-10", cve_per = 109)
        return render_template("plantilla5A.html", form=formu)
    return render_template("plantilla5A.html", form=formu)

@app.route('/sanborns/consultas/<name>')
def sanborns(name):
    if(name == "principal"):
        flash('Tuplas: ', 'info')
        sql = "Select persona.*, contrato.cve_contra, contrato.fechaIni_contra, contrato.fechaFin_contra, contrato.puesto_contra, contrato.sueldo_contra, contrato.hrEntrada_contra, contrato.hrSalida_contra, cliente.cve_clien, cliente.credito_clien, cliente.tipo_clien from persona join cliente on persona.cve_per = cliente.cve_per join contrato on contrato.cve_per=persona.cve_per order by persona.nombre_per asc;"
        r = MyConn.Consulta(SQL = sql)
        return render_template('plantilla5B.html', tema = "Consulta Principal", list = r)
    if(name == "personal"):
        flash('Tuplas: ', 'info')
        sql = "Select persona.*, contrato.cve_contra, contrato.fechaIni_contra, contrato.fechaFin_contra, contrato.puesto_contra, contrato.sueldo_contra, contrato.hrEntrada_contra, contrato.hrSalida_contra from persona join contrato on contrato.cve_per=persona.cve_per order by persona.nombre_per asc;"
        r = MyConn.Consulta(SQL = sql)
        return render_template('plantilla5C.html', tema = "Consulta Principal", list = r)
    if(name == "clientes"):
        flash('Tuplas: ', 'info')
        sql = "Select cliente.cve_clien, cliente.credito_clien,cliente.tipo_clien,persona.cve_per, persona.nombre_per, persona.paterno_per, persona.materno_per, persona.edad_per, persona.genero_per, persona.edocivil, persona.fechaNac_per from cliente join persona on cliente.cve_per = persona.cve_per order by cliente.cve_clien;"
        r = MyConn.Consulta(SQL = sql)
        return render_template('plantilla5D.html', tema = "Consulta Principal", list = r)
    
@app.route('/sanborns/consultas/personal/<name>', methods=['GET', 'POST'])
def eliminarPersonal(name):
    number = int(name)
    if(number > 0):
        aux = str(number)
        MyConn.eliminarContrato(aux)
        return redirect("http://127.0.0.1:5000/sanborns/consultas/personal", code=302)

@app.route('/sanborns/consultas/clientes/<name>')
def eliminarClientes(name):
    number = int(name)
    if(number > 0):
        aux = str(number)
        MyConn.eliminarCliente(aux)
        return redirect("http://127.0.0.1:5000/sanborns/consultas/clientes", code=302)

@app.route('/sanborns/consultas/personal/editar', methods=['GET', 'POST'])
def editarPersonal():
    form = sn.Actualizar()
    if request.method == "GET":
        clave_persona = str(request.args.get("persona", default="", type=str))
        nombre = str(request.args.get("nombre", default="", type=str))
        paterno = str(request.args.get("paterno", default="", type=str))
        materno = str(request.args.get("materno", default="", type=str))
        edad = str(request.args.get("edad", default="", type=str))
        genero = str(request.args.get("genero", default="", type=str))
        edo_civil = str(request.args.get("edo_civil", default="", type=str))
        fecha_nac = str(request.args.get("fecha_nac", default="", type=str))
        clave_contrato = str(request.args.get("contrato", default="", type=str))
        fechaInicio = str(request.args.get("fecha_inicio", default="", type=str))
        fechaFin = str(request.args.get("fecha_fin", default="", type=str))
        puesto = str(request.args.get("puesto", default="", type=str))
        sueldo = str(request.args.get("sueldo", default="", type=str))
        horaEntrada = str(request.args.get("horaEntrada", default="", type=str))
        horaSalida = str(request.args.get("horaSalida", default="", type=str))
        return render_template("plantilla5E.html", form = form, cve_per = clave_persona, cve_con = clave_contrato, nombre = nombre, paterno = paterno, materno = materno, edad = edad, genero = genero, edo_civil = edo_civil, fecha_nac = fecha_nac, fechaInicio = fechaInicio, fechaFin = fechaFin, puesto = puesto, sueldo = sueldo, horaEntrada = horaEntrada, horaSalida = horaSalida)
    elif request.method == "POST":
        nombre_per = request.form["nombre_per1"]
        paterno_per = request.form["paterno1"]
        materno_per = request.form["materno1"]
        edad_per = request.form["edad1"]
        genero_per = request.form["genero1"]
        edocivil = request.form["edo_civil1"]
        fechaNac_per = request.form["fecha_nac1"]
        cve_per = request.form["clave_per1"]
        fechaInicio = request.form["fe_inicio1"]
        fechaFin = request.form["fe_fin1"]
        puesto = request.form["puesto1"]
        sueldo = request.form["sueldo1"]
        horaEntrada = request.form["hora_entrada1"]
        horaSalida = request.form["hora_salida1"]
        cve_contra = request.form["clave_contra1"]
        horaEntrada = horaEntrada + ":00"
        horaSalida = horaSalida + ":00"
        MyConn.actualizarContrato(fechaInicio = fechaInicio, fechaFin = fechaFin, puesto = puesto, sueldo = sueldo, horaEntrada = horaEntrada, horaSalida = horaSalida, cve_contra = cve_contra)
        MyConn.actualizarPersona(nombre_per = nombre_per, paterno_per = paterno_per, materno_per = materno_per, edad_per = edad_per, genero_per = genero_per, edocivil = edocivil, fechaNac_per = fechaNac_per, cve_per = cve_per)
        print(nombre_per, paterno_per, materno_per, edad_per, genero_per, edocivil, fechaNac_per, cve_per)
        return redirect("http://127.0.0.1:5000/sanborns/consultas/personal", code=302)
    
@app.route('/sanborns/consultas/clientes/editar', methods=['GET', 'POST'])
def editarCliente():
    form = sn.ActualizarCliente()
    if request.method == "GET":
        clave_persona = str(request.args.get("persona", default="", type=str))
        nombre = str(request.args.get("nombre", default="", type=str))
        paterno = str(request.args.get("paterno", default="", type=str))
        materno = str(request.args.get("materno", default="", type=str))
        edad = str(request.args.get("edad", default="", type=str))
        genero = str(request.args.get("genero", default="", type=str))
        edo_civil = str(request.args.get("edo_civil", default="", type=str))
        fecha_nac = str(request.args.get("fecha_nac", default="", type=str))
        clave_cliente = str(request.args.get("cliente", default="", type=str))
        credito = str(request.args.get("credito", default="", type=str))
        tipo = str(request.args.get("tipo", default="", type=str))
        return render_template("plantilla5F.html", form = form, cve_per = clave_persona, cve_clien = clave_cliente, nombre = nombre, paterno = paterno, materno = materno, edad = edad, genero = genero, edo_civil = edo_civil, fecha_nac = fecha_nac, credito = credito, tipo = tipo)
    elif request.method == "POST":
        nombre_per = request.form["nombre_per2"]
        paterno_per = request.form["paterno2"]
        materno_per = request.form["materno2"]
        edad_per = request.form["edad2"]
        genero_per = request.form["genero2"]
        edocivil = request.form["edo_civil2"]
        fechaNac_per = request.form["fecha_nac2"]
        cve_per = request.form["clave_per2"]
        cve_cli = request.form["clave_cli2"]
        credito = request.form["credito_clien2"]
        tipo_cli = request.form["tipo_clien2"]
        MyConn.actualizarCliente(credito = credito, tipo = tipo_cli, cve_clien = cve_cli)
        MyConn.actualizarPersona(nombre_per = nombre_per, paterno_per = paterno_per, materno_per = materno_per, edad_per = edad_per, genero_per = genero_per, edocivil = edocivil, fechaNac_per = fechaNac_per, cve_per = cve_per)
        print(nombre_per, paterno_per, materno_per, edad_per, genero_per, edocivil, fechaNac_per, cve_per, cve_cli, credito, tipo_cli)
        return redirect("http://127.0.0.1:5000/sanborns/consultas/clientes", code=302)

def build_folio():
    folio = ""
    for i in range(8):
        caracter = chr(random.randint(ord('1'), ord('9')))
        folio += caracter
    return(folio)

def build_date():
    return (datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
