import sqlite3

# Función para conectar a la base de datos
def conectar_db():
    return sqlite3.connect("biblioteca_python.db")

# Función para crear las tablas si no existen
def crear_tablas():
    conexion = conectar_db()
    cursor = conexion.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS libros (
        isbn TEXT PRIMARY KEY,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        año INTEGER NOT NULL,
        categoria TEXT NOT NULL
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS socios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        tipo TEXT NOT NULL,
        dni INTEGER UNIQUE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS prestamos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        isbn TEXT NOT NULL,
        socio_id INTEGER NOT NULL,
        fecha_prestamo TEXT NOT NULL,
        fecha_devolucion TEXT NOT NULL,
        FOREIGN KEY(isbn) REFERENCES libros(isbn),
        FOREIGN KEY(socio_id) REFERENCES socios(id)
    )
    """)
    
    conexion.commit()
    conexion.close()

# Ejecutar la creación de tablas al importar el módulo
crear_tablas()
