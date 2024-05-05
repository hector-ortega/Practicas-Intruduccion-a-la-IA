#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------

# La ambigüedad en el procesamiento del lenguaje natural se refiere a situaciones en las que una palabra o una frase pueden 
# tener múltiples interpretaciones o significados. Esto puede surgir debido a diferentes razones, como la estructura gramatical
# de la oración, la polisemia de las palabras, la falta de contexto o la presencia de errores ortográficos o gramaticales.

# Los algoritmos diseñados para manejar la ambigüedad en el procesamiento del lenguaje natural tienen como objetivo identificar
# y resolver estas situaciones para mejorar la comprensión y el análisis del texto. Algunas aplicaciones comunes de estos algoritmos
# incluyen la corrección ortográfica, la desambiguación léxica y sintáctica, la traducción automática y la generación de resúmenes.

# Uno de los enfoques para manejar la ambigüedad es el uso de algoritmos de análisis y procesamiento probabilístico, como el algoritmo
# de Viterbi, que se utiliza en el ejemplo que te proporcioné anteriormente. Este algoritmo calcula la probabilidad de diferentes 
# interpretaciones o significados de una palabra o una frase y elige la interpretación más probable en función de ciertos criterios,
# como la frecuencia de ocurrencia de las palabras o la coherencia gramatical.

#--------------- PROGRAMA ------------------------------------
import numpy as np

def viterbi_correccion(texto, palabras_conocidas):
    # Dividimos el texto en palabras
    palabras = texto.split()
    num_palabras = len(palabras)
    
    # Inicializamos la matriz Viterbi
    V = np.zeros((len(palabras_conocidas), num_palabras))
    for i, palabra in enumerate(palabras):
        # Calculamos la probabilidad de cada palabra en función de la distancia Levenshtein
        for j, palabra_conocida in enumerate(palabras_conocidas):
            distancia = distancia_levenshtein(palabra, palabra_conocida)
            probabilidad = 1 / (distancia + 1)  # A mayor distancia, menor probabilidad
            V[j, i] = probabilidad
    
    # Inicializamos el camino más probable
    camino = np.argmax(V, axis=0)
    
    # Reconstruimos el texto corregido
    texto_corregido = ' '.join(palabras_conocidas[i] for i in camino)
    
    return texto_corregido

def distancia_levenshtein(palabra1, palabra2):
    # Creamos una matriz para almacenar las distancias parciales
    matriz = np.zeros((len(palabra1)+1, len(palabra2)+1))
    
    # Inicializamos la primera fila y la primera columna de la matriz
    for i in range(len(palabra1)+1):
        matriz[i, 0] = i
    for j in range(len(palabra2)+1):
        matriz[0, j] = j
    
    # Calculamos la distancia de Levenshtein
    for i in range(1, len(palabra1)+1):
        for j in range(1, len(palabra2)+1):
            if palabra1[i-1] == palabra2[j-1]:
                costo = 0
            else:
                costo = 1
            matriz[i, j] = min(matriz[i-1, j]+1, matriz[i, j-1]+1, matriz[i-1, j-1]+costo)
    
    return matriz[len(palabra1), len(palabra2)]

# Ejemplo de uso
texto_ambiguo = "Tengamos un encuentro mañana en el café."
palabras_conocidas = ["tengamos", "tenemos", "un", "uno", "encuentro", "encuentro", "mañana", "manana", "en", "el", "cafe", "café"]
texto_corregido = viterbi_correccion(texto_ambiguo, palabras_conocidas)

print("Texto original:")
print(texto_ambiguo)
print("\nTexto corregido:")
print(texto_corregido)

#------------------------------------------------------------------------
# 1.-Importamos la biblioteca numpy para trabajar con matrices y cálculos numéricos.
# 2.- Definimos una función viterbi_correccion que toma como entrada un texto y una lista de palabras conocidas.
#      Esta función implementa el algoritmo de Viterbi para encontrar el camino más probable a través de la matriz de probabilidades.
# 3.- Dividimos el texto en palabras y calculamos la longitud del texto y el número de palabras.
# 4.- Inicializamos la matriz Viterbi con ceros, donde las filas representan las palabras conocidas y las columnas representan las palabras del texto.
# 5.- Calculamos la probabilidad de cada palabra en función de la distancia Levenshtein entre la palabra del texto y las palabras conocidas.
# 6.- Inicializamos el camino más probable como el índice de la palabra conocida con la probabilidad más alta para cada palabra del texto.
# 7.- Reconstruimos el texto corregido utilizando las palabras conocidas correspondientes al camino más probable.
# 8.- Definimos una función distancia_levenshtein que calcula la distancia de Levenshtein entre dos palabras.
# 9.- Ejecutamos un ejemplo de uso con un texto ambiguo y una lista de palabras conocidas.
# 10.- Imprimimos el texto original y el texto corregido para demostrar el funcionamiento del algoritmo.