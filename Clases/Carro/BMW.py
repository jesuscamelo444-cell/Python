from Carro import Carro
class BMW(Carro):
    def __init__(self, modelo, color, motor, numeroPuertas, capacidadPasajeros, tipoCombustible):
        super().__init__(modelo, color, motor, numeroPuertas, capacidadPasajeros, tipoCombustible)
    
    def Arranque(self):
        print(f"El BMW de modelo {self.modelo} tiene un arranque automatico.")
        
    def Apagado(self):
        print(f"El BMW de modelo {self.modelo} tiene un apagado automatico.")
    
    def AceleraCion_y_fenado(self):
        print(f"El BMW de modelo {self.modelo} acelera rápidamente y frena con precicion.")
        
    def SistemaDireccional(self):
        
        print(f"El BMW del modelo {self.modelo} tiene unsistema direccional aleman.")
        
    def Climatizacion(self):
        print(f"El BMW del modelo {self.modelo} tiene un sistema de climatizacion.")
        
    def Seguridad(self):
        print(f"El BMW del modelo {self.modelo} tiene un sistema de seguridad digital.")
        
    def Luces(self):
        print(f"El BMW del modelo {self.modelo} tiene un sistema de luces LED.")
    
    def Ventanas(self):
        print(f"El BMW del modelo {self.modelo} tiene ventanas automaticas.")
        
    def Espejos(self):
        print(f"El BMW del modelo {self.modelo} tiene espejos.")
        
bmw1 = BMW("Modelo X5", "Negro", "Motor V8", "Puertas 2", "Pasajeros 2", "Gasolina" )

bmw1.Arranque()
bmw1.Apagado()
bmw1.AceleraCion_y_fenado()
bmw1.SistemaDireccional()
bmw1.Climatizacion()
bmw1.Seguridad()
bmw1.Luces()
bmw1.Ventanas()
bmw1.Espejos()

print("\n")