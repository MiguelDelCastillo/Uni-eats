import sys 
import sqlite3
from sqlite3 import Error

try:
    with sqlite3.connect("unieats.bd") as conn:
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS ROLES\
                    (\
                    ID_ROL INTEGER NOT NULL,\
                    TIPO_ROL TEXT NOT NULL,\
                    PRIMARY KEY (ID_ROL)\
                    );""")
        c.execute("""CREATE TABLE IF NOT EXISTS SERVICIOS_PRODUCTOS\
                    (\
                    ID_SERVICIO_P INTEGER NOT NULL,\
                    NOMBRE_S_P TEXT NOT NULL,\
                    DESCRIPCION TEXT NOT NULL,\
                    TIPO INTEGER NOT NULL,\
                    PRIMARY KEY (ID_SERVICIO_P)\
                    );""")
        c.execute("""CREATE TABLE IF NOT EXISTS USUARIOS\
                    (\
                    ID_USUARIO INTEGER NOT NULL,\
                    NOMBRE TEXT NOT NULL,\
                    APELLIDO TEXT NOT NULL,\
                    ID_ROL INTEGER NOT NULL,\
                    PRIMARY KEY (ID_USUARIO),\
                    FOREIGN KEY (ID_ROL) REFERENCES ROLES(ID_ROL)\
                    );""")
        c.execute("""CREATE TABLE IF NOT EXISTS Relationship\
                    (\
                    ID_USUARIO INTEGER NOT NULL,\
                    ID_SERVICIO_P INTEGER NOT NULL,\
                    PRIMARY KEY (ID_USUARIO, ID_SERVICIO_P),\
                    FOREIGN KEY (ID_USUARIO) REFERENCES USUARIOS(ID_USUARIO),\
                    FOREIGN KEY (ID_SERVICIO_P) REFERENCES SERVICIOS_PRODUCTOS(ID_SERVICIO_P)\
                    );""")
        # c.execute("""INSERT INTO ROLES(ID_ROL,TIPO_ROL) VALUES(1,'admin');""")
        # c.execute("""INSERT INTO ROLES(ID_ROL,TIPO_ROL) VALUES(2,'estudiante');""")
        # c.execute("""INSERT INTO ROLES(ID_ROL,TIPO_ROL) VALUES(3,'comerciante');""")
        print("Tabla creada exitosamente")
except Error as e:
    print(e)
except Exception:
    print(f"Error: {sys.exc_info()[0]}")
finally:
    if conn:
        conn.close()
