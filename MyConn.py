from ast import Assign
from bd import MySQLConn

def Consulta(SQL):
    conexion = MySQLConn()
    cursor = conexion.cursor()
    roles = []
    cursor.execute(SQL)
    roles = cursor.fetchall()
    conexion.close()
    return roles

def insertarComic(clave, nombre, numero, paginas, editorial, autor, anio):
    conexion = MySQLConn()
    with conexion.cursor() as cursor:
        SQL = "Insert into comic(cve_comic, nombre_comic, numero_comic, paginas_comic, editorial_comic, autor_comic, año_comic) "
        SQL += "values(%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(SQL, (clave, nombre, numero, paginas, editorial, autor, anio))
    conexion.commit()
    conexion.close()

def insertarPersona(cve_per, nombre_per, paterno_per, materno_per, edad_per, genero_per, edocivil, fechaNac_per):
    conexion = MySQLConn()
    with conexion.cursor() as cursor:
        SQL = "Insert into persona(cve_per, nombre_per, paterno_per, materno_per, edad_per, genero_per, edocivil, fechaNac_per) "
        SQL += "values(%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(SQL, (cve_per, nombre_per, paterno_per, materno_per, edad_per, genero_per, edocivil, fechaNac_per))
    conexion.commit()
    conexion.close()

def insertarContrato(cve_contra, fechaIni_contra, fechaFin_contra, puesto_contra, sueldo_contra, hrEntrada_contra, hrSalida_contra, cve_perF):
    conexion = MySQLConn()
    with conexion.cursor() as cursor:
        SQL = "Insert into contrato(cve_contra, fechaIni_contra, fechaFin_contra, puesto_contra, sueldo_contra, hrEntrada_contra, hrSalida_contra, cve_per) "
        SQL += "values(%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(SQL, (cve_contra, fechaIni_contra, fechaFin_contra, puesto_contra, sueldo_contra, hrEntrada_contra, hrSalida_contra, cve_perF))
    conexion.commit()
    conexion.close()

def eliminarContrato(id):
    conexion = MySQLConn()
    with conexion.cursor() as cursor:
        SQL = "delete from contrato where cve_contra=" + id
        cursor.execute(SQL)
    conexion.commit()
    conexion.close()

def eliminarCliente(id):
    conexion = MySQLConn()
    with conexion.cursor() as cursor:
        SQL = "delete from cliente where cve_clien=" + id
        cursor.execute(SQL)
    conexion.commit()
    conexion.close()

def actualizarPersona(nombre_per, paterno_per, materno_per, edad_per, genero_per, edocivil, fechaNac_per, cve_per):
    conexion = MySQLConn()
    with conexion.cursor() as cursor:
        SQL = "update persona set nombre_per='{0}', paterno_per='{1}', materno_per='{2}', edad_per='{3}', genero_per='{4}', edocivil='{5}', fechaNac_per='{6}' where cve_per = '{7}'".format(nombre_per, paterno_per, materno_per, edad_per, genero_per, edocivil, fechaNac_per, cve_per)
        cursor.execute(SQL)
    conexion.commit()
    conexion.close()

def actualizarContrato(fechaInicio, fechaFin, puesto, sueldo, horaEntrada, horaSalida, cve_contra):
    conexion = MySQLConn()
    with conexion.cursor() as cursor:
        SQL = "update contrato set fechaIni_contra='{0}', fechaFin_contra='{1}', puesto_contra='{2}', sueldo_contra='{3}', hrEntrada_contra='{4}', hrSalida_contra='{5}' where cve_contra = '{6}'".format(fechaInicio, fechaFin, puesto, sueldo, horaEntrada, horaSalida, cve_contra)
        cursor.execute(SQL)
    conexion.commit()
    conexion.close()

def actualizarCliente(credito, tipo, cve_clien):
    conexion = MySQLConn()
    with conexion.cursor() as cursor:
        SQL = "update cliente set credito_clien='{0}', tipo_clien='{1}' where cve_clien='{2}';".format(credito, tipo, cve_clien)
        cursor.execute(SQL)
    conexion.commit()
    conexion.close()