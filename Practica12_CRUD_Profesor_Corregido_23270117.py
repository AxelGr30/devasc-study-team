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
    if profesores:
        print("\nLista de Profesores:")
        for prof in profesores:
            print(f"ID: {prof[0]}, Nombre: {prof[1]}")
    else:
        print("No hay profesores en la base de datos.")
    cursor.close()
    conexion.close()

def actualizar_profesor(idprofesor, nuevo_nombre):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "UPDATE profesor SET nombreProf = %s WHERE idprofesor = %s"
    cursor.execute(sql, (nuevo_nombre, idprofesor))
    conexion.commit()
    if cursor.rowcount > 0:
        print("Profesor actualizado con éxito.")
    else:
        print("No se encontró un profesor con ese ID.")
    cursor.close()
    conexion.close()

def eliminar_profesor(idprofesor):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "DELETE FROM profesor WHERE idprofesor = %s"
    cursor.execute(sql, (idprofesor,))
    conexion.commit()
    if cursor.rowcount > 0:
        print("Profesor eliminado con éxito.")
    else:
        print("No se encontró un profesor con ese ID.")
    cursor.close()
    conexion.close()

def menu_profesor():
    while True:
        print("\n--- CRUD de Profesor ---")
        print("1. Agregar Profesor")
        print("2. Mostrar Profesores")
        print("3. Actualizar Profesor")
        print("4. Eliminar Profesor")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del profesor: ")
            crear_profesor(nombre)
        elif opcion == "2":
            leer_profesores()
        elif opcion == "3":
            try:
                idp = int(input("Ingrese el ID del profesor a actualizar: "))
                nuevo_nombre = input("Ingrese el nuevo nombre: ")
                actualizar_profesor(idp, nuevo_nombre)
            except ValueError:
                print("Ingrese un valor numérico válido para el ID.")
        elif opcion == "4":
            try:
                idp = int(input("Ingrese el ID del profesor a eliminar: "))
                eliminar_profesor(idp)
            except ValueError:
                print("Ingrese un valor numérico válido para el ID.")
        elif opcion == "5":
            print("Saliendo del CRUD de Profesor.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu_profesor()
