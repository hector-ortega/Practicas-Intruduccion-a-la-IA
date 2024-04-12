#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#----------------------------TEORIA----------------------------------------


#-------------------------- PROGRAMA ------------------------------------

#Esta funcion realiza la busqueda en proofundidad limitada, con un limite dado
def busqueda_prof_lim(grafo, comienzo, objetivo, limite_profundidad):
    visitado = set()
    return dls_recursivo(grafo, comienzo, objetivo, visitado, limite_profundidad)

#Esta funcion realiza la busqueda en profundidad limitada de manera recursiva. Toma el grafo
#el nodo actual, el nodo objetivo, un conjunto de nodos visitados y el limite de produndidad 
#como argumentoas
def dls_recursivo(grafo, nodo_actual, objetivo, visitado, limite_profundidad):
    if nodo_actual == objetivo: #comprueba si el nodo actual es el objetivo

        print("Meta alcanzada, nodo: ", nodo_actual)
        return True
    
    elif limite_profundidad == 0: #Comprueba si se ha alcanzado el limite de profundidad
        return False

    else:
        visitado.add(nodo_actual) # se agrefa el nodo actual al conjunto de nodos visitados.
        print(f"nodo visitado: {visitado}")
        if nodo_actual not in grafo: 
            return False
        
        for vecino in grafo[nodo_actual]:#Explora los nodos vecinos del nodo actual
            print(f"El vecino del nodo: {nodo_actual} es: {vecino}") 
            if vecino not in visitado:
                if dls_recursivo(grafo, vecino, objetivo, visitado, limite_profundidad - 1): # hace una llamada recursiva a "dls_recursivo" con un limite de profundidad reducido
                    return True
    return False # Si encuentra una solucion en alguna de las ramas , devuelve True. De lo contrario devuelve false


def busqueda_profunda_iterativa(grafo, comienzo, objetivo):
    limite_profundidad = 0
    while True:
        encontrado = busqueda_prof_lim(grafo, comienzo, objetivo, limite_profundidad)
        if encontrado:
            return
        else:
            limite_profundidad += 1
            print(f"\n\nlimite de profundidad: {limite_profundidad}")

grafo = {
    'A':['B','C','D'],
    'B':['D'],
    'C':['E'],
    'D':['F'],
    'E':[],
    'F':[]
}

nodo_inicial ='A'
nodo_objetivo ='F'

busqueda_profunda_iterativa(grafo,nodo_inicial,nodo_objetivo)

