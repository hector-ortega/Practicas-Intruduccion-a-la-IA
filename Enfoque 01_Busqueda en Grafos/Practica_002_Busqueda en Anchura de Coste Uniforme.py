from queue import PriorityQueue

#Grafo con costos (Representado como un diccionario de adyacencia)
grafo_costos = {
    'A':{'B':2, 'C':4},
    'B':{'D':1, 'E':3},
    'C':{'F':5},
    'D':{},
    'E':{},
    'F':{}
}

def ucs(grafo, comienzo, objetivo):
    visitado = set() #conjunto para almacenar los nodos visitados
    cola = PriorityQueue() #Cola de prioridad para ordenar por costo 
    cola.put((0,comienzo)) #Inicializamos la cola con el nodo inicial y costo 0

    while not cola.empty():
        costo, nodo_actual = cola.get() #Tomamos el nodo con menor costo

        print(f"\nnodo actual: {nodo_actual} costo: {costo}, visitado: {visitado}\n")

        if nodo_actual == objetivo:
            print(f"Camino optimo desde {comienzo} a {objetivo} : {visitado}")
            return costo
            break

        if nodo_actual not in visitado:
            visitado.add(nodo_actual)

            #agregaamos los vecinos no visitador a la cola con su costo acumulado

            for vecino, margen_costo in grafo[nodo_actual].items():
                if vecino not in visitado:
                    cola.put((costo + margen_costo,vecino))

nodo_inicio ='A'
nodo_objetivo = 'F'
print(f"Calculando camino optimo desde {nodo_inicio} a {nodo_objetivo}...")
costo = ucs(grafo_costos,nodo_inicio,nodo_objetivo)
print(f"costo {costo}")