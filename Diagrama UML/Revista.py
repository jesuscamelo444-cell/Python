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
        
        #calss revsita herenica de producto     
class Revista(Producto):
    def __init__(self, Precio, Titulo, Autor, Editorial, Año_edición, Preferencias, Categoria):
        super().__init__(Precio, Titulo, Autor, Editorial, Año_edición, Preferencias)
        self.Categoria = Categoria
    
    def ver_catalogo_revista(self):
        print("______CATALOGO DE REVISTA______")
        super().ver_catalogo()
        print(f"Categoria: {self.Categoria}")
        
# Revsitas
revista1 = Revista(40000,
"National Geographic",
"pedro",
"The Walt Disney Company",
2025,
"Ciencia",
"Naturaleza\n")

