       # class indexador
class indexador:
    def __init__(self, procesador):
        self.procesador = procesador
        
    def actualiza_almacen(self):
        print("Indexador: actualizando almacén...")
        self.procesador.actualiza_catalogo()
        print("Indexador: notificación enviada al procesador (catálogo actualizado).")
        
    def envia_resultado_busqueda(self, termino):
        print(f"Indexador: enviando resultado de búsqueda para '{termino}'...")
        self.procesador.realiza_busqueda()
        print("Indexador: resultado de búsqueda enviado al procesador.")
        
        