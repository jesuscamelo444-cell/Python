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

revista1.vender()
revista1.comprar()
revista1 .ver_catalogo_revista()
