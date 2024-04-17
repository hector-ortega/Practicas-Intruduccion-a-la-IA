#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# La búsqueda tabú es una técnica de optimización que se utiliza para buscar soluciones en espacios de búsqueda grandes. 
# Se basa en mantener una lista de soluciones recientes visitadas (llamadas lista tabú) para evitar explorar las mismas soluciones nuevamente.
#--------------- PROGRAMA ------------------------------------

import random # Importa el modulo 'random' que se utilizara para generar numeros aleatorios

# Se define el grafo a utilizar como un diccionario de listas adyacentes.
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Define una funcion para evaluar una solucion dada (una secuancia de nodos )
def evaluar_solucion(solucion):
    suma_distancias = 0

    #Cuenta el numero de nodos en la solucion
    for i in range (len(solucion) - 1):
        suma_distancias +=1
    
    return suma_distancias

#Define una funcion para generar una solucion inicial aleatoria
def generar_solucion_inicial():
    # Se mezclan aleatoriamente los nodos del grafo y devuelve una lista que representa esta solucion
    nodos = list(grafo.keys()) 
    random.shuffle(nodos)
    return nodos

# Encuentra el vecindario de una solucion dada.
def encontrar_vecindario(solucion):
    vecindario = []
    # El vecindario esta formado por todas la soluciones que se obtiennen al intercambiar dos nodos en la solucion actuual
    for i in range(len(solucion)):
        for j in range(i + 1, len(solucion)):
            vecino = solucion[:i] + [solucion[j]] + solucion[i+1:j] + [solucion[i]] + solucion[j+1:]
            vecindario.append(vecino)

        return vecindario

# Se implementa la funcion principal que implementa el algoritmo tabu
def busqueda_tabu():
    max_iteraciones = 1000 # se determina el numero maximo de iteraciones
    tam_tabu = 5 # Se determina el tamaño del tabu

    mejor_solucion = generar_solucion_inicial() # Se inicializa la mejor solucion
    mejor_evaluacion = evaluar_solucion(mejor_solucion) # Se evalua la mejor soluciona
    lista_tabu = [] # Se declara la lista tabu como una lista vacia

    iteracion = 0

    while iteracion < max_iteraciones: 
        #Se busca el mejor vecino dentro del vecindario que no este en la lista tabu y tenga la mejor evaluacion
        vecindario = encontrar_vecindario(mejor_solucion)
        mejor_vecino = None
        mejor_evaluacion_vecino = float('inf')

        for vecino in vecindario:
            evaluacion_vecino = evaluar_solucion(vecino)
            if vecino not in lista_tabu and evaluacion_vecino < mejor_evaluacion_vecino:
                mejor_vecino = vecino
                mejor_evaluacion_vecino = evaluacion_vecino

            if mejor_vecino is None:
                break

            #Se actualiza la lista tabu y la mejor solucion si se encuentra un vecino mejor
            lista_tabu.append(mejor_vecino)
            if len(lista_tabu) > tam_tabu:
                lista_tabu.pop(0)

            mejor_solucion = mejor_vecino
            mejor_evaluacion = mejor_evaluacion_vecino

            iteracion += 1
        
    return mejor_solucion, mejor_evaluacion

solucion_optima, evaluacion_optima = busqueda_tabu()
print("Solucion optima: ", solucion_optima)
print("Evaluacion de la solucion optima: ", evaluacion_optima)
