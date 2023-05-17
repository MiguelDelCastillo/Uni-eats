from collections import namedtuple
import sys
import sqlite3
from sqlite3 import Error
from werkzeug.security import generate_password_hash, check_password_hash

def login():
    global usuario
    usuario = ""
    contrasenia = ""
    datosLista = []
    print("Ingresa tu nombre de usuario")
    usuario = input("Usuario: ")
    print("Ingresa tu contrasenia")
    contrasenia = input("Contrasenia: ")
    try:
        with sqlite3.connect("unieats.bd") as conn:
            mi_cursor = conn.cursor()
            mi_cursor.execute(f"""SELECT NOMBRE, CONTRASENIA, ID_ROL\
                                FROM USUARIOS \
                                WHERE USUARIO = ? ;""",(usuario,))
            datos = mi_cursor.fetchall()
            if datos == []:
                print("No existe el usuario")
                return exit()
            else:
                for name, pasw, rol in datos:
                    datosLista.append(name)
                    datosLista.append(pasw)
                    datosLista.append(rol)

    except Error as e:
            print(e)
    except Exception:
        print(f"Error: {sys.exc_info()[0]}")
    finally:
        if conn:
            conn.close()
    
    newName = datosLista[0]
    newPass = datosLista[1]
    rol = datosLista[2]
    if(check_password_hash(newPass,contrasenia)):
        return True
    else:
        print("Contrasenia incorrecta")
        return False
        

def menu():
    try:
        with sqlite3.connect("unieats.bd") as conn:
            mi_cursor = conn.cursor()
            mi_cursor.execute(f"""SELECT ID_ROL\
                                FROM USUARIOS \
                                WHERE USUARIO = ? ;""",(usuario,))
            datos = mi_cursor.fetchall()
            rol = datos[0]
    except Error as e:
            print(e)
    except Exception:
        print(f"Error: {sys.exc_info()[0]}")
    finally:
        if conn:
            conn.close()

    user_rol = rol
    rol_list = {1:"Admin", 2:"Estudiante", 3:"Comerciante"}


    menu_on = True
    while menu_on == True:

        print("|---------------|MENÚ|--------------|")
        print("|------------|BIENVENIDO|-----------|")
        print("")
        print("1) Ver Alumnos. \n2) Ver Vendedores. \n3) Ver Productos y Servicios. \n4) Agregar Producto o Servicio. \n5) Salir.")
        print("")
        choice_menu = int(input("Ingrese la opción deseada: "))

        if choice_menu == 1 and user_rol == rol_list[1]:
            
            print("")
            print("Función de la Opción 1.")
            print("")

        elif choice_menu == 2 and user_rol == rol_list[1]:

            print("")
            print("Función de la Opción 2.")
            print("")

        elif choice_menu == 3:

            print("")
            print("Función de la Opción 3.")
            print("")

        elif choice_menu == 4 and user_rol == rol_list[3]:

            print("")
            print("Función de la Opción 4.")
            print("")

        elif choice_menu == 5:

            print("")
            print("Cerrando Sesión.")
            newRol = 0

            menu_on = False

        else:

            print("")
            print("ERROR: Opción no valida o falta de permisos.")
            print("")


    

def register():
    print("Bienvenido al sistema de registro de UNIEATS")
    while True:
        print("Ingresa tu nombre")
        nombre = input("Nombre: ")
        
        print("Escribe tu primer apellido")
        apellido = input("Apellido: ")
    
        if(apellido =="" and usuario == ""):
            print("No se pueden agregar campos vacios")
        else:
            break
    
    while True:
        print("Selecciona un rol:")
        print("""
            \t 1. Estudiante\n\
            \t 2. Comerciante\n\
        """)
        rol = int(input("Rol: "))

        if rol>=1 and rol<=2:
            if(rol ==1):
                rol = 2
            elif(rol == 2):
                rol = 3
            break
        else:
            print("Solo se puede el 1 o el 2")
    
    while True:
        print("Escribe un usuario")
        usuario = input("Usuario: ")

        print("Escribe tu contrasenia")
        contrasenia = input("Contrasenia: ")

        contrasenia2 = input("Ingresa otra vez tu contrasenia: ")
        if contrasenia == contrasenia2:
            encrypt = generate_password_hash(contrasenia)

        if usuario == "" and contrasenia == "":
            print("Los campos no pueden estar vacios")
        else:
            break

    try:
        with sqlite3.connect("unieats.bd") as conn:
            mi_cursor = conn.cursor()
            mi_cursor.execute("SELECT COUNT(*) FROM USUARIOS;")
            data = mi_cursor.fetchone()
            id_usuario = data[0] + 1
            mi_cursor.execute(f"""INSERT INTO USUARIOS\
            VALUES(?,?,?,?,?,?);""",(id_usuario,nombre,apellido,rol,usuario,encrypt))
            print("Usuario agregado correctamente!!")
    except Error as e:
            print(e)
    except Exception:
        print(f"Error: {sys.exc_info()[0]}")
    finally:
        if conn:
            conn.close()
    id_usuario = 0
    nombre = ""
    apellido = ""
    rol = 0
    usuario = ""
    contrasenia = ""
    contrasenia2 = ""
    encrypt = ""


while True:
    respuesta = ""
    print('Bienvenido a UniEats')
    print("¿Eres nuevo? - Selecciona (1)")
    print("¿Ya tienes cuenta? - Selecciona (2)")
    print("Salir - Selecciona (3)")

    try:
        
        respuesta = int(input("Escriba su opcion: "))

        if (1 >= respuesta or respuesta <= 3):
            if respuesta == 2:
                respuestaLogin = login()
                if(respuestaLogin):
                    menu()
            elif respuesta == 1:
                register()
            elif respuesta == 3:
                break
        else:
            print(f"Solo existen 2 opciones")
                

    except Exception:
        print("Ingresa numeros, porfavor")




