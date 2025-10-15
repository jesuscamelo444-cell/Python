# classe producto
class Producto:
    def __init__(self, Precio, Titulo, Autor, Editorial, Año_edición, Preferencias):
        self.Precio = Precio
        self.Titulo = Titulo
        self.Autor = Autor
        self.Editorial = Editorial
        self.Año_edición = Año_edición
        self.Preferencias = Preferencias
        
    def vender(self):
        print(f"El producto {self.Titulo} ha sido puesto en venta por ${self.Precio}\n")
        
    def comprar(self):
        print(f"El producto {self.Titulo} ha sido comprado por {self.Precio}\n")
        
    def ver_catalogo(self):
        print(F"Titulo: {self.Titulo}")
        print(f"Autor: {self.Autor}")
        print(f"Editorial: {self.Editorial}")
        print(f"Año de edición: {self.Año_edición}")
        print(f"Precio: ${self.Precio:,}")
        print(f"Preferencias: {self.Preferencias}")
        
        #classe libro (herencia de productof)
class Libro(Producto):
    def __init__(self, Precio, Titulo, Autor, Editorial, Año_edición, Preferencias, Genero):
        super().__init__(Precio, Titulo, Autor, Editorial, Año_edición, Preferencias)
        self.Genero = Genero
        
    def ver_catalogo_libro(self):
        print("______CATALAGO DE LIBROS______")
        super().ver_catalogo()
        print(f"Genero: {self.Genero}")
        
        #calss revsita herenica de producto     
class Revista(Producto):
    def __init__(self, Precio, Titulo, Autor, Editorial, Año_edición, Preferencias, Categoria):
        super().__init__(Precio, Titulo, Autor, Editorial, Año_edición, Preferencias)
        self.Categoria = Categoria
    
    def ver_catalogo_revista(self):
        print("______CATALOGO DE REVISTA______")
        super().ver_catalogo()
        print(f"Categoria: {self.Categoria}")
       #class porductos de segunda mano libros y revistas
class ArticuloSegundaMano:
    def __init__(self, Clasificacion, Tema, Vendedor):
        self.Tema = Tema
        self.Clasificacion = Clasificacion
        self.Vendedor = Vendedor
        
    def ver_catalogo_segunda_mano(self):
        print(f"Clasificación: {self.Clasificacion}")
        print(f"Tema: {self.Tema}")
        print(f"Vendedor: {self.Vendedor}")
        
        #creo una clase que hereda de libro y ArticuloSegundamao , o clase de tipo multuplre herencia
class LibroSegundaMano(Libro,ArticuloSegundaMano):
    def __init__(self, Precio, Titulo, Autor, Editorial, Año_edición, Preferencias, Genero, Clasificacion, tema, vendedor):
        Libro.__init__(self, Precio, Titulo, Autor, Editorial, Año_edición, Preferencias, Genero)
        ArticuloSegundaMano.__init__(self, Clasificacion, tema, vendedor)
        
    def ver_catalogo_libro_usado(self):
        print("______LIBROS DE SEGUNDA MANO______")
        Libro.ver_catalogo_libro(self)
        ArticuloSegundaMano.ver_catalogo_segunda_mano(self)
        
        #creo una clase que hereda de revista y articuloSegundamano, o clase de tipo multiple herencia
class RevistaSegundaMano(Revista, ArticuloSegundaMano):
    def __init__(self, Precio, Titulo, Autor, Editorial, Año_edición, Preferencias, Categoria, Clasifcacion, Tema , Vendedor):
        Revista.__init__(self, Precio, Titulo, Autor, Editorial, Año_edición, Preferencias, Categoria)
        ArticuloSegundaMano.__init__(self, Clasifcacion, Tema, Vendedor)
    
    def ver_catalogo_revista_usada(self):
        print("______REVISTAS DE SEGUNDA MANO______")
        Revista.ver_catalogo_revista(self)
        ArticuloSegundaMano.ver_catalogo_segunda_mano(self)
        