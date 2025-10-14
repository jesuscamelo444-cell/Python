#case servidor
class Servidor:
    def muestra_pagina(self):
        print("Mostrarndo la pagina principal al usuario...")
        
    def enviar_sugerencia(self):
        print("enviado sugerencia...")
            
    def enviar_datos_de_compra(self):
        print("enviando datos de compra...")
        
    def enviar_datos_de_ventas(self):
        print("Enviando datos de venta...")
        
servidor1 = Servidor()
servidor1.muestra_pagina()
usuario1.enviar_sugerencia(servidor1)
servidor1.enviar_datos_de_compra()
servidor1.enviar_datos_de_ventas()
        