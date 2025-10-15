class Producto:
    def __init__(self, precio, titulo, autor, editorial, año_edicion, preferencias):
        self.precio = precio
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.año_edicion = año_edicion
        self.preferencias = preferencias

    def ver_catalago(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Editorial: {self.editorial}")
        print(f"Año de edición: {self.año_edicion}")
        print(f"Preferencias: {self.preferencias}")
        print(f"Precio: ${self.precio}")


# Clase intermedia
class ArticuloSegundaMano(Producto):
    def __init__(self, precio, titulo, autor, editorial, año_edicion, preferencias, clasificacion, tema, vendedor):
        super().__init__(precio, titulo, autor, editorial, año_edicion, preferencias)
        self.clasificacion = clasificacion
        self.tema = tema
        self.vendedor = vendedor

    def ver_catalogo_segunda_mano(self):
        super().ver_catalago()
        print(f"Clasificación: {self.clasificacion}")
        print(f"Tema: {self.tema}")
        print(f"Vendedor: {self.vendedor}")


# Subclases específicas
class LibroSegundaMano(ArticuloSegundaMano):
    def ver_catalogo_libro_segunda_mano(self):
        print("______LIBRO DE SEGUNDA MANO______")
        super().ver_catalogo_segunda_mano()


class RevistaSegundaMano(ArticuloSegundaMano):
    def ver_catalogo_revista_segunda_mano(self):
        print("______REVISTA DE SEGUNDA MANO______")
        super().ver_catalogo_segunda_mano()
