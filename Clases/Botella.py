class Botella:
    def __init__(self, material, capacidad, forma, diseño, tapa, grabados, color):
        self.material = material
        self.capacidad = capacidad 
        self.forma = forma
        self.diseño = diseño
        self.tapa = tapa
        self.grabados = grabados
        self.color = color
        
    def ContenerLiquido(self):
        print(f"La botella de {self.material} contiene {self.capacidad} ml.")
        
    def FacilitarVertido(self):
        print(f"La botella de {self.material} facilita el vertido de liquídos")
            
    def Transport(self):
        print(f"La botella de {self.material} es facil de transportar gracias a su forma {self.diseño}.")
        
    def Manejo(self):
        print(f"La botella de {self.material} es facial de manejar gracias a su forma {self.forma}.")
            
            
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
            
        
botella1 = Plastica(
"plastico 1",
500, 
"cilindrica",
"egonomico",
"plastica de rosca",
"gravado de Flores",
"transparente"
)
botella1.ContenerLiquido()
botella1.FacilitarVertido()
botella1.CierrePlastico()
botella1.Transport()
botella1.Manejo()
botella1.CompatibilidadPlasstico()
botella1.ReutilizablePlastico()
botella1.ColorPlastico()
print("\n")
    
botella2 = Vidrio(
"vidrio 1",
1000,
"cilindrica",
"clasica",
"corcho",
"grabado de uvas",
"ambar"
)
    
botella2.ContenerLiquido()
botella2.FacilitarVertido()
botella2.CierreVidrio()
botella2.Transport()
botella2.Manejo()
botella2.CompatibilidadVidrio()
botella2.ReutilizableVidrio()
botella2.ColorVidrio()
    