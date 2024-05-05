#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# El algoritmo de backtracking es una técnica de búsqueda sistemática que se utiliza para encontrar soluciones a problemas 
# computacionales, especialmente aquellos que involucran la generación de todas las posibles combinaciones, permutaciones o
# configuraciones de un conjunto de elementos. Este algoritmo es útil en situaciones donde se requiere explorar exhaustivamente
# todas las posibles soluciones para encontrar la óptima, o bien, para encontrar una solución que cumpla ciertas condiciones o restricciones.

# ¿Cómo funciona?
# El algoritmo de backtracking funciona de manera recursiva, explorando todas las posibles opciones en un espacio de búsqueda.
# Sigue estos pasos:

# 1.- Elección de una opción: En cada paso, se elige una opción válida para continuar la búsqueda. Esta opción puede
#     ser un elemento de un conjunto, una decisión en un problema de decisión, o una configuración parcial de la solución.
# 2.- Exploración recursiva: Se realiza una llamada recursiva para explorar todas las posibles opciones a partir de la 
#     elección actual. Se continúa explorando recursivamente hasta que se alcance una solución o hasta que ya no haya más opciones 
#     válidas para explorar.
# 3.- Retroceso (backtrack): Si la exploración no conduce a una solución válida, o si se exploraron todas las opciones sin éxito,
#     se retrocede y se deshace la última elección realizada. Luego, se continúa explorando otras opciones.
# 4.- Finalización: El proceso se repite hasta que se encuentre una solución válida o hasta que se agoten todas las opciones posibles.
#--------------- PROGRAMA ------------------------------------
def backtracking_combinaciones_suma(objetivo, numeros, combinacion_actual, suma_actual, resultado):
    """
    Función recursiva para encontrar todas las combinaciones de números que suman el objetivo.
    
    - objetivo: valor objetivo que se desea alcanzar.
    - numeros: lista de números disponibles para formar combinaciones.
    - combinacion_actual: lista que almacena la combinación actual en el proceso de búsqueda.
    - suma_actual: suma actual de los números en la combinación actual.
    - resultado: lista que almacena todas las combinaciones que suman el objetivo.
    """
    if suma_actual == objetivo:
        resultado.append(combinacion_actual[:])  # Se agrega una copia de la combinación actual al resultado
        return
    
    if suma_actual > objetivo:
        return
    
    for i in range(len(numeros)):
        numero_actual = numeros[i]
        combinacion_actual.append(numero_actual)
        suma_actual += numero_actual
        
        # Llamada recursiva para explorar nuevas combinaciones
        backtracking_combinaciones_suma(objetivo, numeros[i:], combinacion_actual, suma_actual, resultado)
        
        # Retroceder: eliminar el último número agregado a la combinación actual
        combinacion_actual.pop()
        suma_actual -= numero_actual

# Función principal para encontrar todas las combinaciones que suman el objetivo
def encontrar_combinaciones_suma(objetivo, numeros):
    resultado = []  # Lista para almacenar todas las combinaciones que suman el objetivo
    backtracking_combinaciones_suma(objetivo, numeros, [], 0, resultado)
    return resultado

# Ejemplo de uso
objetivo = 7
numeros = [2, 3, 6, 7]

print("Combinaciones que suman", objetivo, ":")
print(encontrar_combinaciones_suma(objetivo, numeros))

#-------------------------------------------------------------------------------------------------
# 1.- La función backtracking_combinaciones_suma es una función recursiva que realiza la búsqueda de todas 
#     las combinaciones posibles de números que suman el objetivo dado. Recibe como parámetros el objetivo, 
#     la lista de números disponibles, la combinación actual en el proceso de búsqueda, la suma actual de los 
#     números en la combinación actual y la lista para almacenar los resultados.
# 2.- En la función backtracking_combinaciones_suma, se comprueba si la suma actual es igual al objetivo. En caso afirmativo, 
#     se agrega la combinación actual al resultado. Si la suma actual supera el objetivo, se detiene la búsqueda.
# 3.- Se realiza un bucle sobre todos los números disponibles para agregarlos a la combinación actual. Luego, se realiza una 
#     llamada recursiva para explorar nuevas combinaciones.
# 4.- Después de cada llamada recursiva, se elimina el último número agregado a la combinación actual y se resta de la suma actual, 
#     lo que permite retroceder y probar otras combinaciones.
# 5.- La función encontrar_combinaciones_suma es una función auxiliar que llama a la función backtracking_combinaciones_suma 
#     con los parámetros adecuados y devuelve el resultado.
# 6.- Se muestra un ejemplo de uso con un objetivo y una lista de números, y se imprime el resultado de todas las 
#     combinaciones que suman el objetivo.