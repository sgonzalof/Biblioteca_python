import sqlite3
import random
from datetime import datetime, timedelta

# Conexión a la base de datos SQLite
DB_NAME = "biblioteca_python.db"

def conectar():
    """Crea y devuelve la conexión a la base de datos."""
    return sqlite3.connect(DB_NAME)

# ===================== LIBROS =====================

def agregar_libro(isbn, titulo, autor, año, categoria):
    """Agrega un libro a la base de datos."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO libros (isbn, titulo, autor, año, categoria) VALUES (?, ?, ?, ?, ?)",
                   (isbn, titulo, autor, año, categoria))
    conn.commit()
    conn.close()

def eliminar_libro(isbn):
    """Elimina un libro de la base de datos."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM libros WHERE isbn = ?", (isbn,))
    conn.commit()
    conn.close()

def obtener_libros():
    """Devuelve una lista de todos los libros en la biblioteca."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM libros")
    libros = cursor.fetchall()
    conn.close()
    return libros

# ===================== SOCIOS =====================

def agregar_socio(nombre, tipo, dni=None):
    """Agrega un socio a la base de datos."""
    conn = conectar()
    cursor = conn.cursor()
    
    if tipo == "Adulto":
        cursor.execute("INSERT INTO adultos (dni, trabajador, sancion) VALUES (?, 0, 0)", (dni,))
        socio_id = dni
    else:
        socio_id = random.randint(0, 99999)
        cursor.execute("INSERT INTO niños (id, sancion) VALUES (?, 0)", (socio_id,))
    
    cursor.execute("INSERT INTO socios (id, nombre, tipo) VALUES (?, ?, ?)", (socio_id, nombre, tipo))
    conn.commit()
    conn.close()

def eliminar_socio(socio_id):
    """Elimina un socio de la base de datos."""
    conn = conectar()
    cursor = conn.cursor()
    
    # Verificar si el socio tiene préstamos activos
    cursor.execute("SELECT * FROM prestamos WHERE socio = ?", (socio_id,))
    if cursor.fetchone():
        print("El socio tiene préstamos activos y no puede ser eliminado.")
        return
    
    cursor.execute("DELETE FROM socios WHERE id = ?", (socio_id,))
    cursor.execute("DELETE FROM adultos WHERE dni = ?", (socio_id,))
    cursor.execute("DELETE FROM niños WHERE id = ?", (socio_id,))
    
    conn.commit()
    conn.close()

def obtener_socios():
    """Devuelve una lista de todos los socios registrados."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM socios")
    socios = cursor.fetchall()
    conn.close()
    return socios

# ===================== PRÉSTAMOS =====================

def agregar_prestamo(isbn, socio, duracion):
    """Registra un préstamo en la base de datos."""
    conn = conectar()
    cursor = conn.cursor()

    # Verificar si el socio tiene más de 3 libros prestados
    cursor.execute("SELECT COUNT(*) FROM prestamos WHERE socio = ?", (socio,))
    if cursor.fetchone()[0] >= 3:
        print("El socio ya tiene 3 préstamos activos.")
        return

    # Verificar si el socio tiene préstamos vencidos
    cursor.execute("SELECT * FROM prestamos WHERE socio = ? AND fecha_devolucion < DATE('now')", (socio,))
    if cursor.fetchone():
        print("El socio tiene préstamos vencidos y no puede sacar más libros.")
        return

    # Calcular fecha de devolución
    dias = 15 if duracion == "15 días" else 30
    fecha_prestamo = datetime.now().strftime("%Y-%m-%d")
    fecha_devolucion = (datetime.now() + timedelta(days=dias)).strftime("%Y-%m-%d")

    cursor.execute("INSERT INTO prestamos (isbn, socio, fecha_prestamo, fecha_devolucion) VALUES (?, ?, ?, ?)",
                   (isbn, socio, fecha_prestamo, fecha_devolucion))
    conn.commit()
    conn.close()

def eliminar_prestamo(prestamo_id):
    """Elimina un préstamo de la base de datos."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM prestamos WHERE rowid = ?", (prestamo_id,))
    conn.commit()
    conn.close()

def obtener_prestamos():
    """Devuelve una lista de todos los préstamos activos."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT rowid, isbn, socio, fecha_prestamo, fecha_devolucion FROM prestamos")
    prestamos = cursor.fetchall()
    conn.close()
    return prestamos
