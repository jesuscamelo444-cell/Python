        #class procesador
class Procesador:
    def mandar_datos_de_venta(self):
        print("Mandando datos de venta...")

    def mandar_articulo_online(self):
        print("Mandando artículo online...")

    def envia_sugerencia_administrador(self):
        print("Enviando sugerencia al administrador...")

    def modificar_stock(self):
        print("Modificando stock...")

    def realizar_cobro(self):
        print("Realizando cobro...")

    def realizar_pago(self):
        print("Realizando pago...")

    def actualiza_catalogo(self):
        print("Actualizando catálogo...")

    def realiza_busqueda(self):
        print("Realizando búsqueda...")
        
    def notificar_novedades(self, recolector, editorial):
        print("Procesador: detectó nuevas novedades, enviando al recolector...")
        recolector.envia_novedades(editorial)
        print("Procesador: novedades enviadas correctamente.")
        

