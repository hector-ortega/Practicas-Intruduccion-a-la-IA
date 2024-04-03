from collections import deque

#Grafo de amigos (representado como un diccionario de adyacencia)
grafo_amigos = {
    'Alicia':["Roberto","Carlos"],
    'Roberto':["Alicia","David"],
    'Carlos':["Alicia","Eve"],
    "David":["Roberto","Francisco"],
    "Eve":['Carlos','Graciela'],
    'Francisco':['David'],
    'Graciela':['Eve']

}

def bfs_amigos_comun(grafo,usuario_1,usuario_2):
    visitado = set() #Conjunto para almacenar los usuarios visitados
    cola = deque([usuario_1]) #Iniciamos la cola con el primer usuario

    amigos_comun = set() #Conjunto para almacenar amigos en comun

    while cola:
        usuario_actual = cola.popleft() # Tomamos el primer usuario de la cola
        if usuario_actual not in visitado:
            visitado.add(usuario_actual)

            #Si el usuario actual es amigo de ambos, lo agregamos al conjunto de amigos en comun

            if usuario_2 in grafo[usuario_actual]:
                amigos_comun.add(usuario_actual)

            #Agregamos los amigos no visitados a la cola
            for  amigo in grafo[usuario_actual]:
                if amigo not in visitado:
                    cola.append(amigo)
    
    return amigos_comun
    

usuario_1 = 'Alicia'
usuario_2 = 'Eve'
amigos_comun = bfs_amigos_comun(grafo_amigos,usuario_1,usuario_2)
print(f"Amigos en comun entre {usuario_1} y {usuario_2}: {amigos_comun}")

