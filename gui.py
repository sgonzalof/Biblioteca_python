import tkinter as tk
from tkinter import ttk, messagebox
from functions import (
    agregar_libro, eliminar_libro, obtener_libros,
    agregar_socio, eliminar_socio, obtener_socios,
    agregar_prestamo, eliminar_prestamo, obtener_prestamos
)

# Función para actualizar la tabla de libros
def actualizar_tabla_libros():
    for row in tabla_libros.get_children():
        tabla_libros.delete(row)
    for libro in obtener_libros():
        tabla_libros.insert("", "end", values=libro)

# Función para actualizar la tabla de socios
def actualizar_tabla_socios():
    for row in tabla_socios.get_children():
        tabla_socios.delete(row)
    for socio in obtener_socios():
        tabla_socios.insert("", "end", values=socio)

# Función para actualizar la tabla de préstamos
def actualizar_tabla_prestamos():
    for row in tabla_prestamos.get_children():
        tabla_prestamos.delete(row)
    for prestamo in obtener_prestamos():
        tabla_prestamos.insert("", "end", values=prestamo)

# Función para agregar un libro
def boton_agregar_libro():
    agregar_libro(entry_isbn.get(), entry_titulo.get(), entry_autor.get(), entry_año.get(), combo_categoria.get())
    messagebox.showinfo("Éxito", "Libro agregado correctamente")
    actualizar_tabla_libros()

# Función para eliminar un libro
def boton_eliminar_libro():
    eliminar_libro(entry_isbn.get())
    messagebox.showinfo("Éxito", "Libro eliminado correctamente")
    actualizar_tabla_libros()

# Función para agregar un socio
def boton_agregar_socio():
    agregar_socio(entry_nombre_socio.get(), combo_tipo_socio.get(), entry_dni_socio.get())
    messagebox.showinfo("Éxito", "Socio agregado correctamente")
    actualizar_tabla_socios()

# Función para eliminar un socio
def boton_eliminar_socio():
    eliminar_socio(entry_id_socio.get())
    messagebox.showinfo("Éxito", "Socio eliminado correctamente")
    actualizar_tabla_socios()

# Función para dar de alta un préstamo
def boton_agregar_prestamo():
    agregar_prestamo(entry_isbn_prestamo.get(), entry_socio_prestamo.get(), combo_duracion_prestamo.get())
    messagebox.showinfo("Éxito", "Préstamo registrado correctamente")
    actualizar_tabla_prestamos()

# Función para dar de baja un préstamo
def boton_eliminar_prestamo():
    eliminar_prestamo(entry_id_prestamo.get())
    messagebox.showinfo("Éxito", "Préstamo eliminado correctamente")
    actualizar_tabla_prestamos()

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Biblioteca")
ventana.geometry("800x600")

# Pestañas
notebook = ttk.Notebook(ventana)
notebook.pack(fill="both", expand=True)

# ========== PESTAÑA LIBROS ==========
frame_libros = ttk.Frame(notebook)
notebook.add(frame_libros, text="Libros")

# Formulario de libros
ttk.Label(frame_libros, text="ISBN:").pack()
entry_isbn = ttk.Entry(frame_libros)
entry_isbn.pack()

ttk.Label(frame_libros, text="Título:").pack()
entry_titulo = ttk.Entry(frame_libros)
entry_titulo.pack()

ttk.Label(frame_libros, text="Autor:").pack()
entry_autor = ttk.Entry(frame_libros)
entry_autor.pack()

ttk.Label(frame_libros, text="Año:").pack()
entry_año = ttk.Entry(frame_libros)
entry_año.pack()

ttk.Label(frame_libros, text="Categoría:").pack()
combo_categoria = ttk.Combobox(frame_libros, values=["Adulto", "Menores de 14 años"])
combo_categoria.pack()

ttk.Button(frame_libros, text="Agregar Libro", command=boton_agregar_libro).pack()
ttk.Button(frame_libros, text="Eliminar Libro", command=boton_eliminar_libro).pack()

# Tabla de libros
tabla_libros = ttk.Treeview(frame_libros, columns=("ISBN", "Título", "Autor", "Año", "Categoría"), show="headings")
for col in ("ISBN", "Título", "Autor", "Año", "Categoría"):
    tabla_libros.heading(col, text=col)
tabla_libros.pack(fill="both", expand=True)
actualizar_tabla_libros()

# ========== PESTAÑA SOCIOS ==========
frame_socios = ttk.Frame(notebook)
notebook.add(frame_socios, text="Socios")

ttk.Label(frame_socios, text="Nombre:").pack()
entry_nombre_socio = ttk.Entry(frame_socios)
entry_nombre_socio.pack()

ttk.Label(frame_socios, text="Tipo:").pack()
combo_tipo_socio = ttk.Combobox(frame_socios, values=["Adulto", "Niño"])
combo_tipo_socio.pack()

ttk.Label(frame_socios, text="DNI (solo adultos):").pack()
entry_dni_socio = ttk.Entry(frame_socios)
entry_dni_socio.pack()

ttk.Button(frame_socios, text="Agregar Socio", command=boton_agregar_socio).pack()
ttk.Button(frame_socios, text="Eliminar Socio", command=boton_eliminar_socio).pack()

tabla_socios = ttk.Treeview(frame_socios, columns=("ID", "Nombre", "Tipo", "DNI"), show="headings")
for col in ("ID", "Nombre", "Tipo", "DNI"):
    tabla_socios.heading(col, text=col)
tabla_socios.pack(fill="both", expand=True)
actualizar_tabla_socios()

# ========== PESTAÑA PRÉSTAMOS ==========
frame_prestamos = ttk.Frame(notebook)
notebook.add(frame_prestamos, text="Préstamos")

ttk.Label(frame_prestamos, text="ISBN:").pack()
entry_isbn_prestamo = ttk.Entry(frame_prestamos)
entry_isbn_prestamo.pack()

ttk.Label(frame_prestamos, text="ID Socio:").pack()
entry_socio_prestamo = ttk.Entry(frame_prestamos)
entry_socio_prestamo.pack()

ttk.Label(frame_prestamos, text="Duración:").pack()
combo_duracion_prestamo = ttk.Combobox(frame_prestamos, values=["15 días", "30 días"])
combo_duracion_prestamo.pack()

ttk.Button(frame_prestamos, text="Registrar Préstamo", command=boton_agregar_prestamo).pack()

ttk.Label(frame_prestamos, text="ID Préstamo:").pack()
entry_id_prestamo = ttk.Entry(frame_prestamos)
entry_id_prestamo.pack()

ttk.Button(frame_prestamos, text="Eliminar Préstamo", command=boton_eliminar_prestamo).pack()

tabla_prestamos = ttk.Treeview(frame_prestamos, columns=("ID", "ISBN", "Socio", "Fecha Préstamo", "Fecha Devolución"), show="headings")
for col in ("ID", "ISBN", "Socio", "Fecha Préstamo", "Fecha Devolución"):
    tabla_prestamos.heading(col, text=col)
tabla_prestamos.pack(fill="both", expand=True)
actualizar_tabla_prestamos()

ventana.mainloop()