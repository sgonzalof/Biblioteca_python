import sqlite3
from database import conectar_db

# Agregar un libro
def agregar_libro(isbn, titulo, autor, año, categoria):
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO libros (isbn, titulo, autor, año, categoria) VALUES (?, ?, ?, ?, ?)",
        (isbn, titulo, autor, año, categoria),
    )
    conexion.commit()
    conexion.close()

# Eliminar un libro
def eliminar_libro(isbn):
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM libros WHERE isbn = ?", (isbn,))
    conexion.commit()
    conexion.close()

# Buscar libros
def obtener_libros():
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM libros")
    libros = cursor.fetchall()
    conexion.close()
    return libros
