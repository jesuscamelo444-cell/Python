from Carro import Carro
class Renault(Carro):
    def __init__(self, modelo, color, motor, numeroPuertas, capacidadPasajeros, tipoCombustible):
        super().__init__(modelo, color, motor, numeroPuertas, capacidadPasajeros, tipoCombustible)
        
    def Arranque(self):
        print(f"El Renault de modelo {self.modelo} tiene un arranque manual.")
            
    def Apagado(self):
        print(f"El Renault de modelo {self.modelo} tiene un apagado manual.")
        
    def AceleraCion_y_fenado(self):
        print(f"El Renault de modelo {self.modelo} acelera de forma moderada y frena con seguridad.")
            
    def SistemaDireccional(self):
        print(f"El Renault del modelo {self.modelo} tiene un sistema direccional frances.")
            
    def Climatizacion(self):
        print(f"El Renault del modelo {self.modelo} tiene un sistema de climatizacion basico.")
            
    def Seguridad(self):
        print(f"El Renault del modelo {self.modelo} tiene un sistema de seguridad estandar.")
            
    def Luces(self):
        print(f"El Renault del modelo {self.modelo} tiene un sistema de luces halogenas.")
        
    def Ventanas(self):
        print(f"El Renault del modelo {self.modelo} tiene ventanas manuales.")
            
    def Espejos(self):
        print(f"El Renault del modelo {self.modelo} tiene espejos ajustables manualmente.")
        
renault1 = Renault("Modelo Clio", "Rojo", "Motor I4", "Puertas 4", "Pasajeros 5", "Diesel" )

renault1.Arranque()
renault1.Apagado()
renault1.AceleraCion_y_fenado()
renault1.SistemaDireccional()
renault1.Climatizacion()
renault1.Seguridad()
renault1.Luces()
renault1.Ventanas()
renault1.Espejos()

print("\n")