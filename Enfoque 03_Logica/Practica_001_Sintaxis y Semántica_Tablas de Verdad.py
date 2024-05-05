#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# Claro, la teoría detrás de los algoritmos de Sintaxis y Semántica, específicamente las tablas de verdad, es fundamental en el campo 
# de la lógica y la computación. Estos algoritmos se utilizan para analizar y comprender la estructura y el significado de las expresiones lógicas.

# ¿Cómo funciona un algoritmo de Tablas de Verdad?
# 1.- Generación de la tabla de verdad: El algoritmo comienza generando todas las posibles combinaciones de valores de verdad para 
#     las variables presentes en la expresión lógica. Esto se hace utilizando técnicas como la combinación de permutaciones o la función 
#     de producto cartesiano.
# 2.- Evaluación de la expresión: Para cada combinación de valores de verdad en la tabla de verdad, la expresión lógica se evalúa 
#     utilizando esos valores. Esto se puede hacer utilizando técnicas de evaluación de expresiones booleanas.
# 3.- Visualización de la tabla de verdad: Una vez que se han evaluado todas las combinaciones de valores de verdad, se muestra la 
#     tabla de verdad resultante. Esto proporciona una representación visual de cómo la expresión lógica se comporta en función de 
#     los valores de sus variables.
# 4.- Análisis de la tabla de verdad: Finalmente, se analiza la tabla de verdad para extraer información sobre el comportamiento
#     de la expresión lógica. Esto puede incluir la identificación de valores de verdad contradictorios, la demostración de 
#     equivalencias lógicas o la verificación de la validez de argumentos.
#--------------- PROGRAMA ------------------------------------
import itertools

def generar_tabla_verdad(variables):
    """Genera una tabla de verdad para las variables dadas."""
    tabla = []
    # Generar todas las posibles combinaciones de valores de verdad para las variables
    for valores in itertools.product([False, True], repeat=len(variables)):
        fila = dict(zip(variables, valores))
        tabla.append(fila)
    return tabla

def evaluar_expresion(expresion, tabla):
    """Evalúa una expresión lógica en cada fila de la tabla de verdad."""
    valores_expresion = []
    for fila in tabla:
        # Evaluar la expresión lógica en el contexto de la fila actual
        valor = eval(expresion, fila)
        valores_expresion.append(valor)
    return valores_expresion

def imprimir_tabla(tabla):
    """Imprime la tabla de verdad en formato legible."""
    # Imprimir encabezado de la tabla
    encabezado = " | ".join(tabla[0].keys())
    print(encabezado)
    print("-" * len(encabezado))
    # Imprimir filas de la tabla
    for fila in tabla:
        valores = [str(valor) for valor in fila.values()]
        fila_str = " | ".join(valores)
        print(fila_str)

# Variables de ejemplo y expresión lógica
variables = ['A', 'B']
expresion = "(A and B) or (not A)"

# Generar tabla de verdad
tabla_verdad = generar_tabla_verdad(variables)

# Evaluar expresión en la tabla de verdad
valores_expresion = evaluar_expresion(expresion, tabla_verdad)

# Imprimir tabla de verdad y valores de la expresión
print("Tabla de Verdad:")
imprimir_tabla(tabla_verdad)
print("\nValores de la Expresión:", expresion)
print(valores_expresion)

#--------------------------------------------------------------------
# 1.- import itertools: Importamos el módulo itertools para generar todas las posibles combinaciones de valores de verdad para las variables.
# 2.- def generar_tabla_verdad(variables): Definimos una función llamada generar_tabla_verdad que toma una lista de variables y 
#   devuelve una tabla de verdad que contiene todas las posibles combinaciones de valores de verdad para esas variables.
# 3.- tabla = []: Creamos una lista vacía para almacenar las filas de la tabla de verdad.
# 4.- for valores in itertools.product([False, True], repeat=len(variables)):: Usamos itertools.product para generar todas
#      las posibles combinaciones de valores de verdad (False y True) para las variables dadas.
# 5.- fila = dict(zip(variables, valores)): Creamos un diccionario que mapea cada variable a su valor de verdad en la fila actual.
# 6.- tabla.append(fila): Agregamos la fila al final de la tabla de verdad.
# 7.- return tabla: Devolvemos la tabla de verdad completa.
# 8.- def evaluar_expresion(expresion, tabla): Definimos una función llamada evaluar_expresion que toma una expresión lógica y una tabla de verdad, y devuelve una lista de los valores de la expresión para cada fila de la tabla.
# 9.- valores_expresion = []: Creamos una lista vacía para almacenar los valores de la expresión para cada fila de la tabla de verdad.
# 10.- for fila in tabla:: Iteramos sobre cada fila de la tabla de verdad.
# 11.- valor = eval(expresion, fila): Evaluamos la expresión lógica en el contexto de la fila actual utilizando la función eval.
# 12.- valores_expresion.append(valor): Agregamos el valor de la expresión a la lista de valores de expresión.
# 13.- return valores_expresion: Devolvemos la lista de valores de expresión completa.
# 14.- def imprimir_tabla(tabla): Definimos una función llamada imprimir_tabla que toma una tabla de verdad y la imprime en formato legible.
# 15.- encabezado = " | ".join(tabla[0].keys()): Creamos una cadena que contiene los nombres de las variables separados por barras verticales para el encabezado de la tabla.
# 16.- print(encabezado): Imprimimos el encabezado de la tabla.
# 17.- print("-" * len(encabezado)): Imprimimos una línea de guiones para separar el encabezado de las filas.
# 18.- for fila in tabla:: Iteramos sobre cada fila de la tabla de verdad.
# 19.- valores = [str(valor) for valor in fila.values()]: Convertimos los valores de verdad de la fila en cadenas.
# 20.- fila_str = " | ".join(valores): Creamos una cadena que contiene los valores de la fila separados por barras verticales.
# 21.- print(fila_str): Imprimimos la fila de la tabla de verdad.
# 22.- variables = ['A', 'B']: Definimos una lista de variables para nuestro ejemplo.
# 23.- expresion = "(A and B) or (not A)": Definimos una expresión lógica para nuestro ejemplo.
# 24.- tabla_verdad = generar_tabla_verdad(variables): Generamos la tabla de verdad para las variables dadas.
# 25.- valores_expresion = evaluar_expresion(expresion, tabla_verdad): Evaluamos la expresión lógica en la tabla de verdad.
# 26.- print("Tabla de Verdad:"): Imprimimos un mensaje para indicar que estamos imprimiendo la tabla de verdad.
# 27.- imprimir_tabla(tabla_verdad): Imprimimos la tabla de verdad.
# 28.- print("\nValores de la Expresión:", expresion): Imprimimos un mensaje para indicar que estamos imprimiendo los valores de la expresión.
# 29.- print(valores_expresion): Imprimimos los valores de la expresión.