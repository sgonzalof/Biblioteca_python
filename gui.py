import tkinter as tk
from tkinter import ttk, messagebox
from functions import agregar_libro, eliminar_libro, obtener_libros

# Función para actualizar la tabla de libros
def actualizar_tabla():
    for row in tabla_libros.get_children():
        tabla_libros.delete(row)
    
    libros = obtener_libros()
    for libro in libros:
        tabla_libros.insert("", "end", values=libro)

# Función para manejar el botón "Agregar Libro"
def boton_agregar_libro():
    isbn = entry_isbn.get()
    titulo = entry_titulo.get()
    autor = entry_autor.get()
    año = entry_año.get()
    categoria = combo_categoria.get()

    if not (isbn and titulo and autor and año and categoria):
        messagebox.showwarning("Error", "Todos los campos son obligatorios")
        return

    agregar_libro(isbn, titulo, autor, año, categoria)
    messagebox.showinfo("Éxito", "Libro agregado correctamente")
    actualizar_tabla()

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Biblioteca")
ventana.geometry("700x500")

# Formulario
frame_form = ttk.LabelFrame(ventana, text="Agregar Libro")
frame_form.pack(pady=10, padx=10, fill="x")

ttk.Label(frame_form, text="ISBN:").grid(row=0, column=0, padx=5, pady=5)
entry_isbn = ttk.Entry(frame_form)
entry_isbn.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame_form, text="Título:").grid(row=1, column=0, padx=5, pady=5)
entry_titulo = ttk.Entry(frame_form)
entry_titulo.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame_form, text="Autor:").grid(row=2, column=0, padx=5, pady=5)
entry_autor = ttk.Entry(frame_form)
entry_autor.grid(row=2, column=1, padx=5, pady=5)

ttk.Label(frame_form, text="Año:").grid(row=3, column=0, padx=5, pady=5)
entry_año = ttk.Entry(frame_form)
entry_año.grid(row=3, column=1, padx=5, pady=5)

ttk.Label(frame_form, text="Categoría:").grid(row=4, column=0, padx=5, pady=5)
combo_categoria = ttk.Combobox(frame_form, values=["Adulto", "Menores de 14 años"])
combo_categoria.grid(row=4, column=1, padx=5, pady=5)

btn_agregar = ttk.Button(frame_form, text="Agregar Libro", command=boton_agregar_libro)
btn_agregar.grid(row=5, column=0, columnspan=2, pady=10)

# Tabla de libros
frame_tabla = ttk.LabelFrame(ventana, text="Inventario de Libros")
frame_tabla.pack(pady=10, padx=10, fill="both", expand=True)

columnas = ("ISBN", "Título", "Autor", "Año", "Categoría")
tabla_libros = ttk.Treeview(frame_tabla, columns=columnas, show="headings")

for col in columnas:
    tabla_libros.heading(col, text=col)
    tabla_libros.column(col, width=100)

tabla_libros.pack(fill="both", expand=True)

btn_eliminar = ttk.Button(ventana, text="Eliminar Libro", command=lambda: eliminar_libro(entry_isbn.get()))
btn_eliminar.pack(pady=10)

actualizar_tabla()

ventana.mainloop()
