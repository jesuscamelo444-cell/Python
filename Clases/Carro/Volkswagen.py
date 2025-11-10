from Carro import Carro
class volkswagen(Carro):
    def __init__(self, modelo, color, motor, numeroPuertas, capacidadPasajeros, tipoCombustible):
        super().__init__(modelo, color, motor, numeroPuertas, capacidadPasajeros, tipoCombustible)
            
    def Arranque(self):
        print(f"El Volkswagen de modelo {self.modelo} tiene un arranque con llave.")
                
    def Apagado(self):
        print(f"El Volkswagen de modelo {self.modelo} tiene un apagado con llave.")
            
    def AceleraCion_y_fenado(self):
        print(f"El Volkswagen de modelo {self.modelo} acelera de forma equilibrada y frena con eficacia.")
                
    def SistemaDireccional(self):
        print(f"El Volkswagen del modelo {self.modelo} tiene un sistema direccional aleman.")
                
    def Climatizacion(self):
        print(f"El Volkswagen del modelo {self.modelo} tiene un sistema de climatizacion avanzado.")
                
    def Seguridad(self):
        print(f"El Volkswagen del modelo {self.modelo} tiene un sistema de seguridad integral.")
                
    def Luces(self):
        print(f"El Volkswagen del modelo {self.modelo} tiene un sistema de luces LED adaptativas.")
            
    def Ventanas(self):
        print(f"El Volkswagen del modelo {self.modelo} tiene ventanas electricas.")
                
    def Espejos(self):
        print(f"El Volkswagen del modelo {self.modelo} tiene espejos con ajuste electrico y calefaccion.")
        
volkswagen1 = volkswagen("Modelo Golf", "Azul", "Motor I4", "Puertas 4", "Pasajeros 5", "Gasolina" )

volkswagen1.Arranque()
volkswagen1.Apagado()
volkswagen1.AceleraCion_y_fenado()
volkswagen1.SistemaDireccional()
volkswagen1.Climatizacion()
volkswagen1.Seguridad()
volkswagen1.Luces()
volkswagen1.Ventanas()
volkswagen1.Espejos()


