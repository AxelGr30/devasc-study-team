#Repositorio GitHub:
#https://github.com/AxelGr30/devasc-study-team.git


import mysql.connector

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",  # Cambia por tu usuario de MySQL
            password="",  # Cambia por tu contraseña de MySQL
            database="dbtaller"
        )
        return conexion
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def crear_linea(clavein, nombre):
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO lineainv (clavein, nombre) VALUES (%s, %s)", (clavein, nombre))
            conexion.commit()
            print("Línea de investigación agregada con éxito")
        except mysql.connector.Error as err:
            print(f"Error al insertar: {err}")
        finally:
            cursor.close()
            conexion.close()

def leer_lineas():
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM lineainv")
            lineas = cursor.fetchall()
            for linea in lineas:
                print(f"Clave: {linea[0]}, Nombre: {linea[1]}")
        except mysql.connector.Error as err:
            print(f"Error al leer datos: {err}")
        finally:
            cursor.close()
            conexion.close()

def actualizar_linea(clavein, nuevo_nombre):
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("UPDATE lineainv SET nombre = %s WHERE clavein = %s", (nuevo_nombre, clavein))
            conexion.commit()
            if cursor.rowcount > 0:
                print("Línea de investigación actualizada correctamente")
            else:
                print("No se encontró la clave especificada")
        except mysql.connector.Error as err:
            print(f"Error al actualizar: {err}")
        finally:
            cursor.close()
            conexion.close()

def eliminar_linea(clavein):
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM lineainv WHERE clavein = %s", (clavein,))
            conexion.commit()
            if cursor.rowcount > 0:
                print("Línea de investigación eliminada correctamente")
            else:
                print("No se encontró la clave especificada")
        except mysql.connector.Error as err:
            print(f"Error al eliminar: {err}")
        finally:
            cursor.close()
            conexion.close()