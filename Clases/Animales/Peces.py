from Animales import Animal
class Peces(Animal):
    def __init__(self, Nombre, Edad, Habita, Dieta, Tamaño, Color):
        super().__init__(Nombre, Edad, Habita, Dieta, Tamaño, Color)
        
    def Nadar(self):
        print(f"El {self.Nombre} se mueve nadando.")
        
    def Comunicarse(self):
        print(f"El {self.Nombre} se comunica mediante movimientos y cambios de color.")
        
    def Reproduccion(self):
        print(f"El {self.Nombre} se reproduce sexualmente.")
        
    def Alimentarse(self):
        print(f"El {self.Nombre} se alimenta de {self.Dieta}.")
        
    def Adaptacion(self):
        print(f"El {self.Nombre} se adapta a su {self.Habita}.")
        
    def Instintos(self):
        print(f"El {self.Nombre} tiene instintos de supervivencia acuaticos.")
        
    def Desacanso(self):
        print(f"El {self.Nombre} descansa flotando en el agua.")
        
    def Sueño(self):
        print(f"El {self.Nombre} duerme entre 4 a 5 horas diarias.")
        
    def InteraccionSocial(self):
        print(f"El {self.Nombre} puede ser solitario o social dependiendo de la especie.")
        
Pez1 = Peces("Nemo", 2, "océanos y arrecifes", "plancton y pequeños crustáceos", "pequeño", "naranja y blanco")


Pez1.Nadar()
Pez1.Comunicarse()
Pez1.Reproduccion()
Pez1.Alimentarse()
Pez1.Adaptacion()
Pez1.Instintos()
Pez1.Desacanso()
Pez1.Sueño()
Pez1.InteraccionSocial()

print("\n")