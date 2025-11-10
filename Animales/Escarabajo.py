from Animales import Animal
class Escarabajo(Animal):
    def __init__(self, Nombre, Edad, Habita, Dieta, Tamaño, Color):
        super().__init__(Nombre, Edad, Habita, Dieta, Tamaño, Color)
        
    def Caminar(self):
        print(f"El {self.Nombre} se mueve caminando.")
        
    def Comunicarse(self):
        print(f"El {self.Nombre} se comunica mediante feromonas y sonidos.")
        
    def Reproduccion(self):
        print(f"El {self.Nombre} se reproduce sexualmente.")
        
    def Alimentarse(self):
        print(f"El {self.Nombre} se alimenta de {self.Dieta}.")
        
    def Adaptacion(self):
        print(f"El {self.Nombre} se adapta a su {self.Habita}.")
        
    def Instintos(self):
        print(f"El {self.Nombre} tiene instintos de supervivencia terrestres.")
        
    def Desacanso(self):
        print(f"El {self.Nombre} descansa escondido bajo tierra o en la vegetacion.")
        
    def Sueño(self):
        print(f"El {self.Nombre} duerme entre 1 a 2 horas diarias.")
        
    def InteraccionSocial(self):
        print(f"El {self.Nombre} puede ser solitario o social dependiendo de la especie.")
        
Escarabajo1 = Escarabajo("Beetle", 1, "bosques y praderas", "hojas y materia orgánica", "pequeño", "marrón oscuro")

Escarabajo1.Caminar()
Escarabajo1.Comunicarse()
Escarabajo1.Reproduccion()
Escarabajo1.Alimentarse()
Escarabajo1.Adaptacion()
Escarabajo1.Instintos()
Escarabajo1.Desacanso()
Escarabajo1.Sueño()
Escarabajo1.InteraccionSocial()

print("\n")