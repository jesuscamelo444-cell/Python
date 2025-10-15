# classe producto
class Productos:
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
        

        