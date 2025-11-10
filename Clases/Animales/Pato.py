from Animales import Animal
class Pato(Animal):
    def __init__(self, Nombre, Edad, Habita, Dieta, Tamaño, Color):
        super().__init__(Nombre, Edad, Habita, Dieta, Tamaño, Color)
        
    def Nadar(self):
        print(f"El {self.Nombre} se mueve nadando.")
        
    def Comunicarse(self):
        print(f"El {self.Nombre} se comunica mediante graznidos.")
        
    def Reproduccion(self):
        print(f"El {self.Nombre} se reproduce sexualmente.")
        
    def Alimentarse(self):
        print(f"El {self.Nombre} se alimenta de {self.Dieta}.")
        
    def Adaptacion(self):
        print(f"El {self.Nombre} se adapta a su {self.Habita}.")
        
    def Instintos(self):
        print(f"El {self.Nombre} tiene instintos acuaticos y terrestres.")
        
    def Desacanso(self):
        print(f"El {self.Nombre} descansa flotando en el agua o en la orilla.")
        
    def Sueño(self):
        print(f"El {self.Nombre} duerme entre 4 a 5 horas diarias.")
        
    def InteraccionSocial(self):
        print(f"El {self.Nombre} es un animal social que interactua con otros patos.")
        
pato1 = Pato("Donald", 3, "lagos y estanques", "plantas acuáticas e insectos", "mediano", "blanco")

pato1.Nadar()
pato1.Comunicarse()
pato1.Reproduccion()
pato1.Alimentarse()
pato1.Adaptacion()
pato1.Instintos()
pato1.Desacanso()
pato1.Sueño()
pato1.InteraccionSocial()