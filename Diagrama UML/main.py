from Clases import Servidor, Usuarios, Productos, Libro, Revista, ArticuloSegundaMano, LibroSegundaMano, RevistaSegundaMano, Novedades, ArticuloOnline, Procesador, indexador, Recolector, Hilo, Editorial

        # Servidor       
servidor1 = Servidor()

# Usuarios
usuario1 = Usuarios("Jesus",
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

# productos
producto1 = Productos()

#Libros
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