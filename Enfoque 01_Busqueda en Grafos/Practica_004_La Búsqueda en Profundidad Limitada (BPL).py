#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# La Búsqueda en Profundidad Limitada (BPL) es una variante de la Búsqueda en Profundidad (BP) que establece un límite de profundidad máxima que 
#puede alcanzar durante la exploración del árbol de búsqueda. Esto se hace para evitar que el algoritmo entre en un bucle infinito o se pierda en ramas 
#profundas y potencialmente infinitas del árbol.

# La Búsqueda en Profundidad Limitada es útil cuando tienes un espacio de búsqueda muy grande y no deseas explorar todas las posibilidades,
# o cuando deseas controlar la profundidad de búsqueda por razones de eficiencia o para garantizar la completitud del algoritmo.

#--------------- PROGRAMA ------------------------------------
#La siguiente funcion se encarga de setear los nodos visitados y el contados  para realizar la busqueda limitada.
#Toma el grafo, el noo de inicio, el nodo objetivo y el limite de profundidad como argumentos.
def profundidad_limitada(grafo, inicio, objetivo, profundidad):
    print(f"profundidad 1 {profundidad}")
    visitado = set()
    conteo = 0
    return dls_recursivo(grafo, inicio, objetivo, visitado, profundidad, conteo)

def dls_recursivo(grafo, nodo_actual, objetivo, visitado, profundidad, conteo):

    if nodo_actual == objetivo:#Comprueba si el nodo actual es el nodo objetivo. si es así, se devuelve True
        print("Meta alcanzada: ", nodo_actual)
        print(f"En un conteo de {conteo} iteraciones.")
        return True
    
    elif profundidad == 0: #Comprueba si se ha alcanzado el limite de profundidad, y si es así devuelve False
    
        return False 
    
    else: #En otro caso se agrega el nodo actual al conjunto de nodos visitados
        conteo = conteo + 1
        visitado.add(nodo_actual)
        print(f"Visitado: {visitado}")
        # if nodo_actual not in grafo:
        #     return False
        
    for vecino in grafo[nodo_actual]:# Explora los nodos vecinos del nodo actual
        print(f"vecino{vecino}")
        if vecino not in visitado: # Se llama recursivamente a dls recursivo con un limite de profundidad reducido
            print ("Si hace algo 1")
            if dls_recursivo(grafo, vecino, objetivo, visitado, profundidad -1, conteo):
                print(f"Si hace algo 2 {profundidad}")
                return True
        print(f"profundidad{profundidad}")
    return False
# se declara ell grafo, representado como un diccionario de listas de adyacencia
grafo = {
    'A': ['B','C'],
    'B': ['D'],
    'C': ['E'],
    'D': ['F'],
    'E': [],
    'F': []
}

nodo_inicial = 'A'# Se decide el nodo inicial en el que se realizará la busqueda limitada
nodo_obj = 'F' # Se define el nodo al que queremos llegar 
limite = 3 #Se define el nomero de  iteraciones que queremos hacer para poder llegar a nuestro objetivo

encontrado = profundidad_limitada(grafo, nodo_inicial, nodo_obj, limite)
if not encontrado:
    print(f"No se encontró: {nodo_obj}")