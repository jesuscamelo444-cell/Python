        #class editoraial
class Editorial:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def vender(self):
        print(f"Editorial {self.nombre}: realizando una venta...")

    def recibe_novedades(self):
        print(f"Editorial {self.nombre}: recibiendo novedades del recolector...")

