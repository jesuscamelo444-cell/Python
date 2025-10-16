# clase usuario
class Usuarios:
    def __init__(self, Nombre, Apellido, No_cuenta, Dirección, Loing, Password):
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.No_cuenta = No_cuenta
        self.Dirección = Dirección
        self.Loing = Loing
        self.Password = Password
        
    def enviar_sugerencia(self, servidor):
        print(f"{self.Nombre} A enviadoo una sugerencia")
        servidor.enviar_sugerencia()
        
    def leer(self):
        print(f"El usuario {self.Nombre} esta leyendo")
        
    def comprar(self,servidor):
        print(f"El usuario {self.Nombre} ha comprado un producto")
        servidor.enviar_datos_de_compra()
        
    def vender(self,servidor):
        print(f"El uduario {self.Nombre} ha vendido un producto")
        
    def realizar_reclamación(self):
        print(f"El usuario {self.Nombre}  ha realizado una reclamación")
        
