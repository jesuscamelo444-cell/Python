class ArticuloOnline:
    def __init__(self, Tema):
        self.Tema = Tema
        
    def pubucar(self):
        print(f"El articulo sobre {self.Tema} ha sido publicada en linea.")
        
        
Articulo1 = ArticuloOnline("Ciencias y tecnologia")
Articulo1.pubucar()
