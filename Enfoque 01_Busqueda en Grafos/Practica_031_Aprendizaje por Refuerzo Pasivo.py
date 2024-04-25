#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------


#--------------- PROGRAMA ------------------------------------
# Definición del grafo mediante un diccionario en Python
grafo = {
    'a': [('p', 4), ('j', 15), ('b', 1)],
    'p': [('a', 4), ('j', 7)],
    'j': [('a', 15), ('p', 7), ('b', 5)],
    'b': [('a', 1), ('j', 5)]
}

def dfs_prl(grafo, inicio):
    visitados = set()  # Conjunto para almacenar los vértices visitados
    pila = [inicio]  # Pila para seguir la ruta

    while pila:
        vertice_actual = pila.pop()  # Tomamos el vértice superior de la pila
        if vertice_actual not in visitados:
            print(f'Visitando vértice: {vertice_actual}')
            visitados.add(vertice_actual)

            # Agregamos los vértices adyacentes no visitados a la pila
            for vecino, peso in grafo[vertice_actual]:
                if vecino not in visitados:
                    pila.append(vecino)
                    # Aquí es donde aplicamos PRL:
                    # Actualizamos los valores de recompensa y valor del vértice según los pesos
    print(visitados)

# Ejemplo de uso
inicio = 'a'
dfs_prl(grafo, inicio)
print(grafo)
