#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------

# La lógica de orden superior es un área de la lógica matemática y la teoría de la computación que trata con funciones que toman 
# otras funciones como argumentos o devuelven funciones como resultados. Se utiliza para abordar problemas donde es necesario 
# razonar sobre funciones y manipularlas de manera programática.

# Funcionamiento:

# 1.- Funciones de Orden Superior:
# - Las funciones de orden superior son aquellas que toman otras funciones como argumentos o devuelven funciones como resultados.
# - Permiten abstraer patrones de cálculo comunes y parametrizarlos con funciones específicas que realizan tareas específicas.

# 2.- Aplicación de Funciones:
# - En la lógica de orden superior, las funciones pueden ser aplicadas a otras funciones como argumentos, lo que permite la creación 
#   de funciones más generales y reutilizables.

# 3.- Composición de Funciones:
# - La composición de funciones es una operación fundamental en la lógica de orden superior que permite combinar funciones para crear nuevas funciones.
# - Esto se logra aplicando una función a la salida de otra función, lo que permite construir operaciones complejas a partir de operaciones más simples.

# 4.- Funciones Anónimas:
# - La lógica de orden superior a menudo hace uso de funciones anónimas o lambda que son funciones sin nombre que pueden ser definidas en línea y
#   pasadas como argumentos a otras funciones.
#--------------- PROGRAMA ------------------------------------

# Definimos una función de orden superior llamada map_list
def map_list(funcion, lista):
    """
    Aplica la función dada a cada elemento de la lista y devuelve una nueva lista con los resultados.
    """
    return [funcion(elemento) for elemento in lista]

# Definimos algunas funciones que podríamos querer aplicar a elementos de una lista
def cuadrado(numero):
    return numero ** 2

def doble(numero):
    return numero * 2

def inverso(numero):
    return 1 / numero

# Creamos una lista de números
numeros = [1, 2, 3, 4, 5]

# Usamos nuestra función de orden superior para aplicar la función cuadrado a cada elemento de la lista
resultado_cuadrado = map_list(cuadrado, numeros)
print("Cuadrado de cada número:", resultado_cuadrado)

# Usamos nuestra función de orden superior para aplicar la función doble a cada elemento de la lista
resultado_doble = map_list(doble, numeros)
print("Doble de cada número:", resultado_doble)

# Usamos nuestra función de orden superior para aplicar la función inverso a cada elemento de la lista
resultado_inverso = map_list(inverso, numeros)
print("Inverso de cada número:", resultado_inverso)