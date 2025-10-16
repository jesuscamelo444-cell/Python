#class novedades
class Novedades:
    def __init__(self, Clasificacion, Tema):
        self.Clasificacion = Clasificacion
        self.Tema = Tema
        
    def cambiar_clasificacion(self, nueva_calsificacion):
        print(f"Camviando clasifcacion de {self.Clasificacion} a { nueva_calsificacion}")
        self.Clasificacion = nueva_calsificacion
        print(f"clasificacion actualizada a {self.Clasificacion}")
        
Noveda1 = Novedades("ciencia", "")
Noveda1.cambiar_clasificacion("Libros de naturaleza y tecnologia\n")
