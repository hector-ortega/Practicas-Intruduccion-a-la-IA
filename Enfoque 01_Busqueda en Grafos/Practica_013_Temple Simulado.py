#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# El Temple Simulado es una técnica de optimización que simula el proceso de recocido de metales para buscar soluciones óptimas. 
# Funciona explorando soluciones en un espacio de búsqueda y aceptando soluciones subóptimas con cierta probabilidad,
# con la esperanza de evitar quedarse atrapado en mínimos locales y encontrar soluciones globales óptimas.
#--------------- PROGRAMA ------------------------------------

import random # El modulo random se utiliza para generar numeros aleatorios 
import math # El modulo math se utiliza para realizar calculos matematicos

# Se define el grafo como un diccionario de listas de adyacencia
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']

}

def evaluar_solucion(solucion): # Esta funcion sirve para calcular la evaluacion (costo) de una solucion dada
    suma_distancias = 0 # se establece la variable la cual corresponde a la suma de distacias entre nodos en la solucion
    for i in range(len(solucion) - 1):
        suma_distancias += 1

    return suma_distancias

# Se define la siguiente funcion que genera una solucion inicial aleatoria mezclando aleatoriamente los nodos del grafo
def generar_solucion_inicial(): 
    nodos = list(grafo.keys()) # se guarda en la variable nodos la lista de los nodos del grafo
    random.shuffle(nodos) # se mezclan aleatoriamente la lista obtenida por el grafo
    return nodos # la funcion retorna la lista de los nodos ya mezclada 

#La siguiente funcion genera un vecino de una solucion dada intercambiando dos nodos al azar en la solucion
def generar_vecino(solucion): 
    vecino = solucion[:] # se cra una copia de la solucion actual 
    i, j = random.sample(range(len(vecino)), 2) # Se seleccionan 2 mueatras aleatorias de la secuencia generada por range(len(vecino))
    vecino[i], vecino[j] = vecino[j], vecino[i]
    return vecino

def temple_simulado():
    # Se establecen los parametros del algoritmo
    temperatura_inicial = 100
    temperatura_final = 0.1
    factor_enfriamiento = 0.9
    max_iteraciones  = 100
    
    # Se inicializan la solucion actual y su evaluacion con la solucion inicial generada
    mejor_solucion = generar_solucion_inicial()
    mejor_evaluacion = evaluar_solucion(mejor_solucion)
    solucion_actual = mejor_solucion
    evaluacion_actual = mejor_evaluacion
    temperatura = temperatura_inicial

    iteracion = 0

    # se genera un bucle principal que implementa el algoritmo de Temple sumulado
    while temperatura > temperatura_final and iteracion < max_iteraciones:
        # Se genera un vecino a la solucion actual
        vecino = generar_vecino(solucion_actual)
        evaluacion_vecino = evaluar_solucion(vecino)
        # si el vecino es mejor que la solucion acgtual, se acepta, 
        if evaluacion_vecino < evaluacion_actual:
            solucion_actual = vecino
            evaluacion_actual = evaluacion_vecino
            if evaluacion_vecino < mejor_evaluacion:
                mejor_solucion = vecino
                mejor_evaluacion = evaluacion_vecino
        #Si es peor, lo aceptamos con cierta probabilidad deeterminada por la temperatura y la diferencia entre las evaluaciones
        else :
            probabilidad_aceptar = math.exp((evaluacion_actual - evaluacion_vecino) / temperatura)
            if random.random() < probabilidad_aceptar:
                solucion_actual = vecino
                evaluacion_actual = evaluacion_vecino
        # se genera enfriamiento multiplicando la temperatura por el factor de enfriamiento en cada iteracion
        temperatura *= factor_enfriamiento
        iteracion += 1
    # Devolvemos la mejor solucion encontrada
    return mejor_solucion, mejor_evaluacion




solucion_optima, evaluacion_optima = temple_simulado()
print("Solucion optima: ", solucion_optima)
print("Evaluacion de la solucion optima: ", evaluacion_optima)