class Animal:
    def __init__(self, Nombre, Edad, Habita, Dieta, Tamaño, Color):
        self.Nombre = Nombre
        self.Edad = Edad
        self.Habita = Habita
        self.Dieta = Dieta
        self.Tamaño = Tamaño
        self.Color = Color  
        
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
