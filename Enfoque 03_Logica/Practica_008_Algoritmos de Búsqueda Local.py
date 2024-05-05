#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# Los algoritmos de búsqueda local son heurísticas utilizadas para encontrar soluciones aproximadas a
# problemas de optimización en espacios de búsqueda grandes o complejos. A diferencia de los algoritmos 
# de búsqueda exhaustiva, que exploran todo el espacio de búsqueda para encontrar la solución óptima, los algoritmos 
# de búsqueda local comienzan desde una solución inicial y realizan movimientos locales para mejorar gradualmente la
# solución hasta alcanzar un óptimo local. Estos algoritmos son particularmente útiles cuando el espacio de búsqueda es 
# demasiado grande para ser explorado completamente o cuando no es posible encontrar una solución óptima en un tiempo razonable.

# El funcionamiento de un algoritmo de búsqueda local varía dependiendo del enfoque específico utilizado, pero en general sigue estos pasos:

# 1.- Inicialización: Se comienza con una solución inicial, que puede ser generada aleatoriamente o mediante algún método heurístico.
# 2.- Generación de vecinos: Se genera un conjunto de soluciones vecinas a partir de la solución actual realizando pequeños cambios 
#     o movimientos locales. Estos cambios pueden ser intercambios, adiciones, eliminaciones, entre otros, dependiendo del problema específico.
# 3.- Evaluación: Se evalúa cada solución vecina utilizando una función objetivo que mide la calidad de la solución. Esta función 
#     puede ser una función de costo que se busca minimizar o una función de beneficio que se busca maximizar.
# 4.- Selección de la mejor solución: Se selecciona la mejor solución vecina en función de su evaluación según la función objetivo.
# 5.- Actualización: Se actualiza la solución actual con la mejor solución vecina encontrada en el paso anterior.
# 6.- Convergencia: Se repiten los pasos 2 al 5 hasta que se alcance un criterio de convergencia, como un número máximo de iteraciones, 
#     una mejora mínima en la solución, o la ausencia de cambios significativos en varias iteraciones consecutivas.
#--------------- PROGRAMA ------------------------------------

import random

def funcion_objetivo(solucion):
    """
    Función objetivo que calcula el valor a minimizar o maximizar.
    En este caso, la función simplemente suma los valores de la solución.
    """
    return sum(solucion)

def generar_solucion_aleatoria(n):
    """Genera una solución aleatoria para el problema."""
    return [random.randint(0, 100) for _ in range(n)]

def generar_vecino(solucion):
    """
    Genera un vecino de la solución actual realizando un pequeño cambio en un elemento.
    En este caso, se selecciona un elemento al azar y se le suma o resta un valor aleatorio.
    """
    vecino = solucion[:]  # Copia de la solución actual
    indice = random.randint(0, len(vecino) - 1)  # Selecciona un índice al azar
    vecino[indice] += random.choice([-1, 1])  # Suma o resta un valor aleatorio al elemento seleccionado
    return vecino

def hill_climbing(funcion_objetivo, generar_solucion_aleatoria, generar_vecino, max_iter):
    """Implementa el algoritmo de Hill Climbing para encontrar un óptimo local."""
    mejor_solucion = generar_solucion_aleatoria(len(funcion_objetivo.__code__.co_varnames))  # Genera una solución aleatoria
    mejor_valor = funcion_objetivo(mejor_solucion)  # Calcula el valor de la mejor solución
    for _ in range(max_iter):
        vecino = generar_vecino(mejor_solucion)  # Genera un vecino de la mejor solución
        valor_vecino = funcion_objetivo(vecino)  # Calcula el valor del vecino
        if valor_vecino > mejor_valor:  # Si el vecino es mejor que la mejor solución actual
            mejor_solucion = vecino  # Actualiza la mejor solución
            mejor_valor = valor_vecino  # Actualiza el mejor valor
    return mejor_solucion, mejor_valor

# Ejemplo de uso
random.seed(42)  # Fijar la semilla aleatoria para reproducibilidad
solucion, valor = hill_climbing(funcion_objetivo, generar_solucion_aleatoria, generar_vecino, max_iter=1000)
print("Solución encontrada:", solucion)
print("Valor de la solución:", valor)

#--------------------------------------------------------------------------------------------------
# 1.- Se define la función funcion_objetivo, que representa la función que queremos maximizar o minimizar. En este caso, 
#     simplemente suma los valores de la solución, pero en problemas reales podría ser una función más compleja.
# 2.- Se define la función generar_solucion_aleatoria, que genera una solución aleatoria para el problema. Esta función 
#     se utiliza para inicializar la búsqueda.
# 3.- Se define la función generar_vecino, que genera un vecino de una solución dada realizando un pequeño cambio en un elemento. 
#     Este es uno de los pasos clave del algoritmo de Hill Climbing.
# 4.- Se define la función hill_climbing, que implementa el algoritmo de Hill Climbing propiamente dicho. Comienza 
#     con una solución aleatoria, genera vecinos y se mueve hacia el vecino que mejora el valor de la función objetivo.
#     El algoritmo termina después de un número máximo de iteraciones especificado por max_iter.
# 5.- En el ejemplo de uso, se fija la semilla aleatoria para reproducibilidad, se llama a la función hill_climbing 
#     y se imprime la solución encontrada y su valor.