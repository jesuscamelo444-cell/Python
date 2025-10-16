        #class hilo
class Hilo:
    def busca_novedades(self, recolector, editorial):
        print("Hilo: buscando novedades...")
        recolector.envia_novedades(editorial)
        print("Hilo: proceso de envío de novedades completado.")
