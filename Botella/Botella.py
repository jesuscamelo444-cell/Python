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
            
            
