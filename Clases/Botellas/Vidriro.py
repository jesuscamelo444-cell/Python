from Botella import Botella
class Vidrio(Botella):
    def __init__(self, material, capacidad, forma, diseño, tapa, grabados, color):
        super().__init__(material, capacidad, forma, diseño, tapa, grabados, color)
       
    def CierreVidrio(self):
        if self.tapa == "hierro":
            print(f"La botella de {self.material} tiene cierre hermetico gracias a su tapa de {self.tapa} que contien un sello de goma.")
            
        elif self.tapa == "corcho":
            print(f"La botella de {self.material} no tien cierre hermetoco por su {self.tapa}.")
            
        else:
            print("Tipo de tapa no reconocida para la botella de vidrio .")
        
    def CompatibilidadVidrio(self):
        if self.material == "vidrio 1":
            print(f"La botella de {self.material} es compatible con bebidas calientes y frias.")
            
        elif self.material == "vidrio 2":
            print(f"La botella de {self.material} es compatible con bebidas calientes y frias.")
            
        elif self.material == "vidrio 3":
            print(f"La botella de {self.material} es compatible con bebidas calientes y frias.")


    def ReutilizableVidrio(self):  
        if self.material == "vidrio 1":
            print(f"La botella de {self.material} es reutilizable.")
            
        elif self.material == "vidrio 2":
            print(f"La botella de {self.material} es reutilizable.")
            
        elif self.material == "vidrio 3":
            print(f"La botella de {self.material} no es reutilizables.")
    
    def ColorVidrio(self):
        if self.color == "tranparente":
            print(f"La botella de {self.material} es de color transprente y brillante.")
            
        elif self.color == "ambar":
            print(f"La botella de {self.material} es de color ambar y brillante.")