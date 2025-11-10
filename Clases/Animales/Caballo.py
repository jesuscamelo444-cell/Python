from Animales import Animal
class Caballo(Animal):
    def __init__(self, Nombre, Edad, Habita, Dieta, Tamaño, Color):
        super().__init__(Nombre, Edad, Habita, Dieta, Tamaño, Color)
        
    def Galopar(self):
        print(f"el {self.Nombre} se mueve galopando.")
        
    def Comunicarse(self):
        print(f"el {self.Nombre} se comounica relinchando.")
        
    def Reproduccion(self):
        print(f"El {self.Nombre} se reproduce sexualmente.")
        
    def Alimentarse(self):
        print(f"El {self.Nombre} se alimenta de {self.Dieta}.")
        
    def Adaptacion(self):
        print(f"El {self.Nombre} se adapta a su {self.Habita}")
        
    def Instintos(self):
        print(f"El {self.Nombre} tiene instintos  salvajes.")
        
    def Desacanso(self):
        print(f"El {self.Nombre} descansa acostado o de pie.")
        
    def Sueño(self):
        print(f"El {self.Nombre} duerme entre 2 a 3 horas diarias.")
        
    def InteraccionSocial(self):
        print(f"El {self.Nombre} es un animal social que interactua con otros caballos.")
        
Caballo1 = Caballo("Spirit", 5, "montañas", "hierbas y frutas", "grande", "marrón claro")

Caballo1.Galopar()
Caballo1.Comunicarse()
Caballo1.Reproduccion()
Caballo1.Alimentarse()
Caballo1.Adaptacion()
Caballo1.Instintos()
Caballo1.Desacanso()
Caballo1.Sueño()
Caballo1.InteraccionSocial()

print("\n")