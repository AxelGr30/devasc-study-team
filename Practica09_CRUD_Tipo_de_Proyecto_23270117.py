import mysql.connector

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",  # Cambia esto si usas otro usuario
            password="",  # Cambia esto si tienes contraseña
            database="dbtaller"
        )
        return conexion
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def crear_tipo(tipo, nombre):
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO tipoproyecto (tipo, nombre) VALUES (%s, %s)", (tipo, nombre))
            conexion.commit()
            print("Tipo de proyecto agregado con éxito")
        except mysql.connector.Error as err:
            print(f"Error al insertar: {err}")
        finally:
            cursor.close()
            conexion.close()


def leer_tipos():
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM tipoproyecto")
            tipos = cursor.fetchall()
            for tipo in tipos:
                print(f"Tipo: {tipo[0]}, Nombre: {tipo[1]}")
        except mysql.connector.Error as err:
            print(f"Error al leer datos: {err}")
        finally:
            cursor.close()
            conexion.close()

def actualizar_tipo(tipo, nuevo_nombre):
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("UPDATE tipoproyecto SET nombre = %s WHERE tipo = %s", (nuevo_nombre, tipo))
            conexion.commit()
            if cursor.rowcount > 0:
                print("Tipo de proyecto actualizado correctamente")
            else:
                print("No se encontró el tipo especificado")
        except mysql.connector.Error as err:
            print(f"Error al actualizar: {err}")
        finally:
            cursor.close()
            conexion.close()


def eliminar_tipo(tipo):
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM tipoproyecto WHERE tipo = %s", (tipo,))
            conexion.commit()
            if cursor.rowcount > 0:
                print("Tipo de proyecto eliminado correctamente")
            else:
                print("No se encontró el tipo especificado")
        except mysql.connector.Error as err:
            print(f"Error al eliminar: {err}")
        finally:
            cursor.close()
            conexion.close()
