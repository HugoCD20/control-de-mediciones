import sqlite3
def instBD():
    conexion = sqlite3.connect("Invernadero.db")
    cursor = conexion.cursor()
    return cursor

conexion = sqlite3.connect("Invernadero.db")
cursor = conexion.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS mediciones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_semana INTEGER NOT NULL,
        temperatura FLOAT NOT NULL,
        humedad INTEGER NOT NULL,
        fecha TEXT,
        FOREIGN KEY (id_semana) REFERENCES semanas(id) ON DELETE CASCADE
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS semanas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        semana INTEGER
    )
''')

conexion.commit()

def generarSemana():
    conexion = sqlite3.connect("Invernadero.db")
    cursor = conexion.cursor()
    cursor.execute('SELECT MAX(semana) FROM semanas')
    semana=cursor.fetchall()
    if semana==[(None,),]:
        cursor.execute('INSERT INTO semanas (semana) values (1)')
    else:
        cursor.execute(f'INSERT INTO semanas (semana) values ({semana[0][0]+1})')

    conexion.commit()

    cursor.execute('SELECT MAX(semana),id FROM semanas')
    semana=cursor.fetchall()

    return semana[0][1]


def insertMedicion(id_semana,temperatura, humedad, fecha):
    conexion = sqlite3.connect("Invernadero.db")
    cursor = conexion.cursor()
    cursor.execute(f"INSERT INTO mediciones (id_semana,temperatura,humedad,fecha) values ({id_semana},{temperatura},{humedad},'{fecha}')")
    conexion.commit()

def semanaQuery():
    cursor = instBD()
    cursor.execute("SELECT * FROM semanas ORDER BY semana ASC")
    semanas=cursor.fetchall()
    return semanas

def medicionesQuery(id_semana):
    cursor=instBD()
    cursor.execute(f"SELECT * FROM mediciones where id_semana={id_semana}")
    medicion=cursor.fetchall()
    return medicion

def data_sets(id_semana):
    cursor=instBD()
    cursor.execute(f"SELECT temperatura FROM mediciones where id_semana={id_semana}")
    temperatura=cursor.fetchall()
    cursor.execute(f"SELECT humedad FROM mediciones where id_semana={id_semana}")
    humedad=cursor.fetchall()
    cursor.execute(f"SELECT fecha FROM mediciones where id_semana={id_semana}")
    fecha=cursor.fetchall()
    return temperatura, humedad, fecha
# Cerrar la conexión
conexion.close()
