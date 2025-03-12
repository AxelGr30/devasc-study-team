#Repositorio GitHub:
#https://github.com/AxelGr30/devasc-study-team.git


import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",      # Cambia según tu configuración
        password="",      # Agrega tu contraseña si es necesaria
        database="dbtaller"
    )

def crear_tipo_proyecto(tipo, nombre):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "INSERT INTO tipoproyecto (tipo, nombre) VALUES (%s, %s)"
    cursor.execute(sql, (tipo, nombre))
    conexion.commit()
    print("Tipo de Proyecto agregado con éxito.")
    cursor.close()
    conexion.close()

def leer_tipos_proyecto():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM tipoproyecto")
    tipos = cursor.fetchall()
    if tipos:
        print("\nLista de Tipos de Proyecto:")
        for t in tipos:
            print(f"Tipo: {t[0]}, Nombre: {t[1]}")
    else:
        print("No hay tipos de proyecto en la base de datos.")
    cursor.close()
    conexion.close()

def actualizar_tipo_proyecto(tipo, nuevo_nombre):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "UPDATE tipoproyecto SET nombre = %s WHERE tipo = %s"
    cursor.execute(sql, (nuevo_nombre, tipo))
    conexion.commit()
    if cursor.rowcount > 0:
        print("Tipo de Proyecto actualizado con éxito.")
    else:
        print("No se encontró el tipo de proyecto indicado.")
    cursor.close()
    conexion.close()

def eliminar_tipo_proyecto(tipo):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "DELETE FROM tipoproyecto WHERE tipo = %s"
    cursor.execute(sql, (tipo,))
    conexion.commit()
    if cursor.rowcount > 0:
        print("Tipo de Proyecto eliminado con éxito.")
    else:
        print("No se encontró el tipo de proyecto indicado.")
    cursor.close()
    conexion.close()

def menu_tipo_proyecto():
    while True:
        print("\n--- CRUD de Tipo de Proyecto ---")
        print("1. Agregar Tipo de Proyecto")
        print("2. Mostrar Tipos de Proyecto")
        print("3. Actualizar Tipo de Proyecto")
        print("4. Eliminar Tipo de Proyecto")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tipo = input("Ingrese el tipo (ID) del proyecto: ")
            nombre = input("Ingrese el nombre del tipo de proyecto: ")
            crear_tipo_proyecto(tipo, nombre)
        elif opcion == "2":
            leer_tipos_proyecto()
        elif opcion == "3":
            tipo = input("Ingrese el tipo (ID) del proyecto a actualizar: ")
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            actualizar_tipo_proyecto(tipo, nuevo_nombre)
        elif opcion == "4":
            tipo = input("Ingrese el tipo (ID) del proyecto a eliminar: ")
            eliminar_tipo_proyecto(tipo)
        elif opcion == "5":
            print("Saliendo del CRUD de Tipo de Proyecto.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu_tipo_proyecto()
