#Repositorio GitHub:
#https://github.com/AxelGr30/devasc-study-team.git


import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Cambia esto si tienes otra configuración
        password="",  # Agrega tu contraseña si la tienes
        database="dbtaller"
    )

def crear_profesor(nombre):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "INSERT INTO profesor (nombreProf) VALUES (%s)"
    cursor.execute(sql, (nombre,))
    conexion.commit()
    print("Profesor agregado con éxito.")
    cursor.close()
    conexion.close()

def leer_profesores():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM profesor")
    profesores = cursor.fetchall()
    for prof in profesores:
        print(prof)
    cursor.close()
    conexion.close()

def actualizar_profesor(idprofesor, nuevo_nombre):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "UPDATE profesor SET nombreProf = %s WHERE idprofesor = %s"
    cursor.execute(sql, (nuevo_nombre, idprofesor))
    conexion.commit()
    print("Profesor actualizado con éxito.")
    cursor.close()
    conexion.close()

def eliminar_profesor(idprofesor):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "DELETE FROM profesor WHERE idprofesor = %s"
    cursor.execute(sql, (idprofesor,))
    conexion.commit()
    print("Profesor eliminado con éxito.")
    cursor.close()
    conexion.close()

