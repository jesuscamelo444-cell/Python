class Carro:
    def __init__(self, modelo, color, motor, numeroPuertas, capacidadPasajeros, tipoCombustible):
        self.modelo =  modelo
        self.color = color
        self.motor = motor
        self.numeroPuertas = numeroPuertas
        self.capacidadPasajeros = capacidadPasajeros
        self.tipoCombustible = tipoCombustible
        
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


