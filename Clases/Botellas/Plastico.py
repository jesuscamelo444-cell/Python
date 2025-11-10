from Botella import Botella
class Plastica(Botella):
    def __init__(self, material, capacidad, forma, diseño, tapa, gravados, color):
        super().__init__(material, capacidad, forma, diseño, tapa, gravados, color)
        
    def CierrePlastico(self):
        if self.tapa == "plastica de rosca":
            print(f"La botella de {self.material} tiene un cierre hermetico gracias a su tapa de {self.tapa}.")
            
        elif self.tapa == "plastica a presion":
            print(f"La botella de {self.material} tiene un cierre no hermetico gracias a su tapa de {self.tapa}.")
            
        else:
            print("Tipo de tapa no reconocida para la botella de plastico.")
        
    def CompatibilidadPlasstico(self):
        if self.material == "plastico 1":
            print(f"La botella de {self.material}  no es compatible con bebidas calientes.")
            
        elif self.material == "plastico 2":
            print(f"La botella de {self.material} no es compatible con bebidas calientes.")
            
        elif self.material == "plastico 3":
            print(f"La botella de {self.material} no es compatible con bebidas calientes.")
            
        else:
            print("Material de botella no existente.")
        
        
    def ReutilizablePlastico(self):
        if self.material == "plastico 1":
            print(f"La botella de {self.material} es reutilizable.")
            
        elif self.material == "plastico 2":
            print/(f"La botella de {self. material} no es reutilizable.")
            
        elif self.material == "plastico 3":
            print(f"La botella de {self.material} no es reutilizable.")
        
        else:
            print("Ma terial de botella no existente.")
            
            
    def ColorPlastico(self):
        if self.color == "transparente":
            print(f"La botella de {self.material} es de color transparente.")
            
        elif self.color == "marron": 
            print(f"La botella de {self.material} es de color marron.")
            
        elif self.color == "verde":
            print(f"La botella de {self.material} es de color verde.")
            
        else:
            
            print("Color de botella no existente:")
        
