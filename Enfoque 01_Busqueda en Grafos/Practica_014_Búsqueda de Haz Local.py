#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------

#--------------- PROGRAMA ------------------------------------

import random # El modulo random se utiliza para generar soluciones iniciales aleatorias
# Definimos el grafo como un diccionario de listas de adyacencua
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'], 
    'D': ['B',],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# En la siguiene funcion se usa para evaluar una soluciondada
def evaluar_solucion(solucion):
    suma_distacias = 0
    # Se cuenta el numeri de nodos en la solucion
    for  i in range(len(solucion) - 1):
        suma_distacias += 1
    return suma_distacias
    
# Se genera una solucion inicial aleatoria mezclando aleatoriamente el grafo
def generar_solucion_inicial():
    nodos = list(grafo.keys())
    random.shuffle(nodos)
    return nodos

# Se define la funcion principal que implementa el algoritmo
# Toma dos parametros: num haces (el numero de haces a mantener)
# y Tam_haz: (El tamaño de cada haz, es decir, cuantos vecinos generar en cada iteracion)
def busqueda_haz_local(num_haces, tam_haz):

    # Se inicializan los haces con soluciones aleatorias
    haces = [generar_solucion_inicial() for _ in range(num_haces)]
    iteracion = 0


    while iteracion < tam_haz:
        nuevos_haces = []

        for solucion in haces:
            vecinos = encontrar_vecinos(solucion) # Se generan vecinos cada solucion en cada haz usando la funcion de encontrar vecinos
            nuevos_haces.extend(vecinos)

        # Se seleccionan las mejores soluciones para el proximo paso
        haces = seleccionar_mejores_haces(nuevos_haces, num_haces)
        
        iteracion += 1
    # Despues de determinado de iteraciones se selecciona la mejor solucion entre todos los haces
    mejor_solucion = seleccionar_mejor_solucion(haces) 
    mejor_evaluacion = evaluar_solucion(mejor_solucion)
    return mejor_solucion, mejor_evaluacion

# La siguiente funcion genera vecinos de una solucion dada intercamdiando dos nodos.
def encontrar_vecinos(solucion):
    vecinos = []
    # Se iteran todos los pares de indices luego crea un nuevo vecino intercambiando los nodos  de la solucion original
    for i in range(len(solucion)):
        for j in range(i + 1, len(solucion)):
            vecino = solucion[:i] + [solucion[j]] + solucion[i+1:j] + [solucion[i]] + solucion[j+1:]
            #Todos los vecinos generados se agregan a uuna lista que se devuelve
            vecinos.append(vecino) 
    return vecinos

# Esta funcion selecciona los mejores haces de una lista de haces
def seleccionar_mejores_haces(haces, num_haces):
    # Se comienza ordenando los haces segun su evaluacion, de manera que los haces con evaluaciones mas bajas (mejores soluciones) estén al principio de la lista
    haces.sort(key = lambda x: evaluar_solucion(x))
    # Se selecciona los primeros 'num_haces' haces de la lista ordenada y los devuelve como los mejores haces
    return haces[:num_haces]

# La siguiente solucion selecciona la mejor solucion de una lista de haces basandose en la evaluacion de cada solucion
def seleccionar_mejor_solucion(haces):
    #Despues de completar todas las iteraciones en la busqueda de haz local
    # Se utiliza la funcion min() para encontrer el haz con la evaluacion mas baja (mejor solucion). se pasa una funcion lambda como argumento para especificar que la evaluacion de cada solucion se utilice para determinar el minimo
    mejor_solucion = min(haces, key=lambda x: evaluar_solucion(x))
    # se devuelte la mejor solucion encontrada
    return mejor_solucion

num_haces = 5
tam_haz = 10
solucion_optima, evaluacion_optima = busqueda_haz_local(num_haces, tam_haz)
print("Solucion optima: ", solucion_optima)
print("Evaluacion de la solucion optima:", evaluacion_optima)        