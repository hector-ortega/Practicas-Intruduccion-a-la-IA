#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# Los algoritmos genéticos son técnicas de búsqueda y optimización inspiradas en la evolución natural. 
# Utilizan operadores genéticos como selección, cruce y mutación para evolucionar una población de soluciones hacia soluciones óptimas.
#--------------- PROGRAMA ------------------------------------
import random # El modulo random se utiliza para realizar operacioneas aleatorias

# Se define el grafo como un diccionario de listas de adyacencia
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
# La siguiente funcion funciona para evaluar una solucion dada
def evaluar_solucion(solucion): # Toma una solucion (lista de nodos)
    suma_distancias = 0 
    for i in range(len(solucion) - 1):
        suma_distancias += 1
    return suma_distancias # devuelve una evaluacion de la solucion

def generar_solucion_inicial(): # Genera una solucion inicial aleatoria mezclando aleatoriamente los nodos del grafo
    nodos = list(grafo.keys()) # Se genera una lista copia de los nodos del grafo
    random.shuffle(nodos) # Se mezclan aleatoriamente
    return nodos # Se retorna la lista ya mezclada

def seleccionar_padres(poblacion, num_padres): 
    padres = [] # Se genera una lista donde se guardaran los padres
    for _ in range(num_padres): 
        torneo = random.sample(poblacion, 2) 
        mejor_padre = min(torneo, key=lambda x: evaluar_solucion(x))
        padres.append(mejor_padre)
    return padres

# Esta funcion realiza el cruce de dos padres para generar un hijo, toma dos padres como argumentos y devuelve un hijo resultante del cruse
def cruzar(padre1, padre2):
    punto_cruce = random.randint(1,len(padre1)- 1)
    hijo = padre1[:punto_cruce] + [nodo for nodo in padre2 if nodo not in padre1[:punto_cruce]]
    return hijo

# Esta funcion aplica una mutacion a una solucion con una cierta probabilidad. Toma una solucion y una probabilidad de mutacion como argumentos
# y con probabilidad igual a probabilidad_mutacion intercambia dos elementos aleatorios en la solucion
def mutar(solucion, probabilidad_mutacion):
    if random.random() < probabilidad_mutacion:
        idx1, idx2 = random.sample(range(len(solucion)), 2)
        solucion[idx1], solucion[idx2] = solucion[idx2], solucion[idx1]

# Esta funcion implementa el algoritmo genetico completo.
#Toma el tamaño de la poblacion, el numero de generaciones, el numero de padres para la seleccion y la probabilidad de mutacion como argumentos y devuelve la mejor solucion encontrada y su evaluacion
def algoritmo_genetico(tam_poblacion, num_generaciones, num_padres, probabilidad_mutacion):
    poblacion = [generar_solucion_inicial() for _ in range(tam_poblacion)]

    for _ in range(num_generaciones):
        padres = seleccionar_padres(poblacion, num_padres)
        hijos = []
        while len(hijos) < tam_poblacion:
            padre1, padre2 = random.sample(padres, 2)
            hijo = cruzar(padre1, padre2)
            mutar(hijo, probabilidad_mutacion)
            hijos.append(hijo)
        poblacion = hijos
    
    mejor_solucion = min(poblacion, key=lambda x: evaluar_solucion(x))
    mejor_evalucion = evaluar_solucion(mejor_solucion)
    return mejor_solucion, mejor_evalucion

tam_poblacion = 10
num_generaciones = 100
num_padres = 2
probabilidad_mutacion = 0.1
solucion_optima, evaluacion_optima = algoritmo_genetico(tam_poblacion, num_generaciones, num_padres, probabilidad_mutacion)
print("Solucción óptima:", solucion_optima)
print("Evaluación de la solución óptima:", evaluacion_optima)
