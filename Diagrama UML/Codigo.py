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
        
        # clase usuario
class Usuario:
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
        
# classe producto
class Producto:
    def __init__(self, Precio, Titulo, Autor, Editorial, Año_edición, Preferencias):
        self.Precio = Precio
        self.Titulo = Titulo
        self.Autor = Autor
        self.Editorial = Editorial
        self.Año_edición = Año_edición
        self.Preferencias = Preferencias
        
    def vender(self):
        print(f"El producto {self.Titulo} ha sido puesto en venta por ${self.Precio}\n")
        
    def comprar(self):
        print(f"El producto {self.Titulo} ha sido comprado por {self.Precio}\n")
        
    def ver_catalogo(self):
        print(F"Titulo: {self.Titulo}")
        print(f"Autor: {self.Autor}")
        print(f"Editorial: {self.Editorial}")
        print(f"Año de edición: {self.Año_edición}")
        print(f"Precio: ${self.Precio:,}")
        print(f"Preferencias: {self.Preferencias}")
        
        #classe libro (herencia de productof)
class Libro(Producto):
    def __init__(self, Precio, Titulo, Autor, Editorial, Año_edición, Preferencias, Genero):
        super().__init__(Precio, Titulo, Autor, Editorial, Año_edición, Preferencias)
        self.Genero = Genero
        
    def ver_catalogo_libro(self):
        print("______CATALAGO DE LIBROS______")
        super().ver_catalogo()
        print(f"Genero: {self.Genero}")
        
        #calss revsita herenica de producto     
class Revista(Producto):
    def __init__(self, Precio, Titulo, Autor, Editorial, Año_edición, Preferencias, Categoria):
        super().__init__(Precio, Titulo, Autor, Editorial, Año_edición, Preferencias)
        self.Categoria = Categoria
    
    def ver_catalogo_revista(self):
        print("______CATALOGO DE REVISTA______")
        super().ver_catalogo()
        print(f"Categoria: {self.Categoria}")
        
        #class porductos de segunda mano libros y revistas
class ArticuloSegundaMano:
    def __init__(self, Clasificacion, Tema, Vendedor):
        self.Tema = Tema
        self.Clasificacion = Clasificacion
        self.Vendedor = Vendedor
        
    def ver_catalogo_segunda_mano(self):
        print(f"Clasificación: {self.Clasificacion}")
        print(f"Tema: {self.Tema}")
        print(f"Vendedor: {self.Vendedor}")
        
        #creo una clase que hereda de libro y ArticuloSegundamao , o clase de tipo multuplre herencia
class LibroSegundaMano(Libro,ArticuloSegundaMano):
    def __init__(self, Precio, Titulo, Autor, Editorial, Año_edición, Preferencias, Genero, Clasificacion, tema, vendedor):
        Libro.__init__(self, Precio, Titulo, Autor, Editorial, Año_edición, Preferencias, Genero)
        ArticuloSegundaMano.__init__(self, Clasificacion, tema, vendedor)
        
    def ver_catalogo_libro_usado(self):
        print("______LIBROS DE SEGUNDA MANO______")
        Libro.ver_catalogo_libro(self)
        ArticuloSegundaMano.ver_catalogo_segunda_mano(self)
        
        #creo una clase que hereda de revista y articuloSegundamano, o clase de tipo multiple herencia
class RevistaSegundaMano(Revista, ArticuloSegundaMano):
    def __init__(self, Precio, Titulo, Autor, Editorial, Año_edición, Preferencias, Categoria, Clasifcacion, Tema , Vendedor):
        Revista.__init__(self, Precio, Titulo, Autor, Editorial, Año_edición, Preferencias, Categoria)
        ArticuloSegundaMano.__init__(self, Clasifcacion, Tema, Vendedor)
    
    def ver_catalogo_revista_usada(self):
        print("______REVISTAS DE SEGUNDA MANO______")
        Revista.ver_catalogo_revista(self)
        ArticuloSegundaMano.ver_catalogo_segunda_mano(self)
    
#class novedades
class Novedades:
    def __init__(self, Clasificacion, Tema):
        self.Clasificacion = Clasificacion
        self.Tema = Tema
        
    def cambiar_clasificacion(self, nueva_calsificacion):
        print(f"Camviando clasifcacion de {self.Clasificacion} a { nueva_calsificacion}")
        self.Clasificacion = nueva_calsificacion
        print(f"clasificacion actualizada a {self.Clasificacion}")
        
class ArticuloOnline:
    def __init__(self, Tema):
        self.Tema = Tema
        
    def pubucar(self):
        print(f"El articulo sobre {self.Tema} ha sido publicada en linea.")
        
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
        
        #recolector
class Recolector:
    def rec_envia_novedades(self, editorial ):
        print("Recolector: enviando novedades al sistema...")
        
    def envia_novedades(self, editorial):
        print("Recolector: enviando novedades a la editorial...")
        editorial.recibe_novedades()
        print("Recolector: novedades enviadas correctamente.")
        
        #class hilo
class Hilo:
    def busca_novedades(self, recolector, editorial):
        print("Hilo: buscando novedades...")
        recolector.envia_novedades(editorial)
        print("Hilo: proceso de envío de novedades completado.")
        
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



            
        
        # Servidor       
servidor1 = Servidor()

# Usuarios
usuario1 = Usuario("Jesus",
"Camelo",
8881234,
"cra 4 #34-34",
"Jesus123",
123455)

servidor1.muestra_pagina()
usuario1.enviar_sugerencia(servidor1)
servidor1.enviar_datos_de_compra()
servidor1.enviar_datos_de_ventas()
print()
usuario1.leer()
usuario1.comprar(servidor1)
usuario1.vender(servidor1)
usuario1.realizar_reclamación()
print()

# Libros
Libro1 = Libro(30000,
"El ironico",
"El vago",
"Editorial SENA",
2025,
"Tecnologia",
"Ciencia\n")

Libro1.vender()
Libro1.comprar()
Libro1.ver_catalogo_libro()

# Revsitas
revista1 = Revista(40000,
"National Geographic",
"pedro",
"The Walt Disney Company",
2025,
"Ciencia",
"Naturaleza\n")

revista1.vender()
revista1.comprar()
revista1 .ver_catalogo_revista()

Libro_usado = LibroSegundaMano(
20000,
"El Principito",
"Antoine de Saint-Exupéry",
"Reynal & Hitchcock",
1943,
"Aventura",
"infantil",
"como nuevo",
"Filosofia para niños",
"Luis Pérez "
)

revista_usada = RevistaSegundaMano(
8000,
"Muy Interesante",
"Disney",
"New york",
2015,
"Ciencia",
"Dibulgación",
"Usado",
"Descubrimiento",
"Ana Gómez\n"
)

Libro_usado.ver_catalogo_libro_usado()
print()
revista_usada.ver_catalogo_revista_usada()

#metodos de novedades
Noveda1 = Novedades("ciencia", "")
Noveda1.cambiar_clasificacion("Libros de naturaleza y tecnologia\n")

#metodis de articulo online
Articulo1 = ArticuloOnline("Ciencias y tecnologia")
Articulo1.pubucar()
print()

procesador = Procesador()
procesador.mandar_datos_de_venta()
procesador.mandar_articulo_online()
procesador.envia_sugerencia_administrador()
procesador.modificar_stock()
procesador.realizar_cobro()
procesador.realizar_pago()
procesador.actualiza_catalogo()
procesador.realiza_busqueda()

print()

indexador_ojt = indexador(procesador)
indexador_ojt.actualiza_almacen()
indexador_ojt.envia_resultado_busqueda("ciencia")
print()

recolector = Recolector()
#recolector.envia_novedades(editorial)
print()



print()
editorial = Editorial(
"ANIBAL",
"Calle 45 #10-20",
3214567890
)
recolector = Recolector()
hilo = Hilo()
#recolector.envia_novedades(editorial)
recolector.envia_novedades(editorial)
print()

hilo.busca_novedades(recolector, editorial)


print()
recolector1 = Recolector()
recolector1.envia_novedades(editorial)
procesador.notificar_novedades(recolector1, editorial)
