class Libro:
    def __init__(self, isbn, titulo, autor, año, categoria):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.categoria = categoria

class Socio:
    def __init__(self, nombre, tipo, dni=None):
        self.nombre = nombre
        self.tipo = tipo
        self.dni = dni  # Solo los adultos tienen DNI

class Prestamo:
    def __init__(self, isbn, socio_id, fecha_prestamo, fecha_devolucion):
        self.isbn = isbn
        self.socio_id = socio_id
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
