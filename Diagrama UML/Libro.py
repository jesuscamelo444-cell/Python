        #classe libro (herencia de productof)
class Libro(Producto):
    def __init__(self, Precio, Titulo, Autor, Editorial, Año_edición, Preferencias, Genero):
        super().__init__(Precio, Titulo, Autor, Editorial, Año_edición, Preferencias)
        self.Genero = Genero
        
    def ver_catalogo_libro(self):
        print("______CATALAGO DE LIBROS______")
        super().ver_catalogo()
        print(f"Genero: {self.Genero}")
        
# Libros
Libro1 = Libro(30000,
"El ironico",
"El vago",
"Editorial SENA",
2025,
"Tecnologia",
"Ciencia\n")