
from Animales import Animal
class Cocodrilo(Animal):
    def __init__(self, Nombre, Edad, Habita, Dieta, Tamaño, Color):
        super().__init__(Nombre, Edad, Habita, Dieta, Tamaño, Color)
        
    def Nadar(self):
        print(f"El {self.Nombre} se mueve nadando.")
            
    def Comunicarse(self):
        print(f"El {self.Nombre} se comunica mediante sonidos guturales.")
            
    def Reproduccion(self):
        print(f"El {self.Nombre} se reproduce sexualmente.")
            
    def Alimentarse(self):
        print(f"El {self.Nombre} se alimenta de {self.Dieta}.")
            
    def Adaptacion(self):
        print(f"El {self.Nombre} se adapta a su {self.Habita}.")
            
    def Instintos(self):
        print(f"El {self.Nombre} tiene instintos depredadores.")
            
    def Desacanso(self):
        print(f"El {self.Nombre} descansa flotando en el agua o en la orilla.")
            
    def Sueño(self):
        print(f"El {self.Nombre} duerme entre 6 a 8 horas diarias.")
            
    def InteraccionSocial(self):
        print(f"El {self.Nombre} es un animal solitario que rara vez interactua con otros cocodrilos.")
            
Cocodrilo1 = Cocodrilo("Rex", 7, "ríos y lagos", "peces y mamíferos", "grande", "verde oscuro")

Cocodrilo1.Nadar()
Cocodrilo1.Comunicarse()
Cocodrilo1.Reproduccion()
Cocodrilo1.Alimentarse()
Cocodrilo1.Adaptacion()
Cocodrilo1.Instintos()
Cocodrilo1.Desacanso()
Cocodrilo1.Sueño()
Cocodrilo1.InteraccionSocial()

print("\n")