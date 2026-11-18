# Recuperatorio práctico - Terminal de Expedición Espacial
# Nombre y apellido: a. sebe
# Curso:2do 2da
#
# IMPORTANTE:
# Resolver el programa siguiendo las etapas indicadas en el README.md.
# Realizar los commits y push cuando se indique.
#
# No borrar estos comentarios.


# =========================
# ETAPA 1 - INICIO
# =========================

# Crear las variables necesarias.
# Crear las listas de destinos y costos.
# Pedir el nombre del piloto.


# =========================
# ETAPA 2 - NAVEGACIÓN
# =========================

# Mostrar el menú y procesar la opción seleccionada.
# Utilizar las listas para obtener destino y costo.


# =========================
# ETAPA 3 - CICLO PRINCIPAL
# =========================

# Modificar el programa para que continúe funcionando
# hasta que el usuario decida finalizar la expedición.


# =========================
# ETAPA 4 - ESTADO Y RESUMEN
# =========================

# Mostrar el estado de la nave.
# Recorrer las listas con un for para mostrar destinos y costos.


nombre = input ("nombre: ")
combustible = 100
destino = ["luna","marte","saturno"]
costo = [20,35,50]

print (nombre)
print ("caballedo este es el combustible disponible:", combustible)
print ("destinos disponibles:", destino)
lugar= input("ingrese destino:")
if lugar in destino:
    index = destino.index(lugar)
    costo_destino = costo[index]
    if combustible > costo_destino:
        combustible = combustible - costo_destino
        print("viaje a", lugar, "realizado peefeto caballedo")
        print("combustible restante:", combustible)
    else:
        print("no hay combutible para ir a", lugar, "caballedo")