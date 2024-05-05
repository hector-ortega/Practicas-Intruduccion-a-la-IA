#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# El análisis semántico es una fase esencial en la compilación de programas y se utiliza para verificar que las estructuras 
# sintácticas de un programa tienen un significado coherente y válido según las reglas del lenguaje de programación. 
# A diferencia del análisis léxico y sintáctico, que se centran en la estructura y la gramática del programa, el análisis
# semántico se enfoca en el significado de las construcciones del programa.

# Aquí hay algunos aspectos clave sobre el análisis semántico y cómo funciona:

# 1.- Verificación de Tipos: Una de las tareas principales del análisis semántico es garantizar que los tipos de datos 
#     utilizados en el programa sean consistentes y compatibles entre sí. Por ejemplo, se verifica que no se realicen 
#     operaciones aritméticas entre tipos incompatibles, como sumar un número entero con una cadena de texto.
# 2.- Resolución de Identificadores: El análisis semántico se encarga de resolver las referencias a variables y funciones, 
#     asegurándose de que estén definidas antes de ser utilizadas y manejando los ámbitos de visibilidad adecuadamente.
# 3.- Coherencia de Estructuras: Se verifica que las estructuras del programa, como las sentencias de control de flujo 
#     (if, while, for), las definiciones de funciones y las llamadas a funciones, estén correctamente anidadas y estructuradas.
# 4.- Constantes y Literales: Se asegura de que las constantes y literales utilizados en el programa tengan un significado 
#     semántico válido y estén dentro de los límites permitidos por el lenguaje.
# 5.- Otras Reglas Semánticas: Además de los aspectos mencionados anteriormente, el análisis semántico también puede 
#     incluir la verificación de otras reglas semánticas específicas del lenguaje, como el manejo de punteros,
#     la asignación de memoria, la gestión de excepciones, entre otros.
#--------------- PROGRAMA ------------------------------------
def analyze_semantics(expression):
    # Diccionario para almacenar las variables y sus valores
    variables = {}

    # Expresión evaluada
    evaluated_expression = ""

    # Tokenizamos la expresión
    tokens = expression.split()

    # Recorremos los tokens
    for token in tokens:
        # Si el token es un número
        if token.isdigit():
            evaluated_expression += token + " "
        # Si el token es una variable
        elif token.isalpha():
            # Si la variable está definida en el diccionario
            if token in variables:
                evaluated_expression += str(variables[token]) + " "
            # Si no está definida, lanzamos un error
            else:
                raise ValueError("Variable '{}' no definida".format(token))
        # Si el token es un operador
        elif token in ['+', '-', '*', '/']:
            evaluated_expression += token + " "
        # Si no reconocemos el token, lanzamos un error
        else:
            raise ValueError("Token '{}' no reconocido".format(token))

    # Devolvemos la expresión evaluada
    return evaluated_expression.strip()

# Ejemplo de expresión a analizar
expression = "3 + x * 5"

# Definimos el valor de la variable 'x'
variables = {'x': 2}

try:
    # Realizamos el análisis semántico
    result = analyze_semantics(expression, variables)
    print("Expresión evaluada:", result)
except ValueError as e:
    print("Error:", e)

#-------------------------------------------------
# 1.- La función analyze_semantics toma una expresión como entrada y devuelve la misma expresión evaluada, 
#     con las variables sustituidas por sus valores correspondientes.
# 2.- Creamos un diccionario variables para almacenar las variables y sus valores.
# 3.- evaluated_expression es una cadena que contendrá la expresión evaluada.
# 4.- Dividimos la expresión en tokens usando el método split() y los almacenamos en la lista tokens.
# 5.- Iteramos sobre cada token en la lista tokens.
# 6.- Si el token es un número (isdigit()), lo agregamos a la expresión evaluada.
# 7.- Si el token es una variable (isalpha()), verificamos si está definida en el diccionario de variables y 
#     la sustituimos por su valor.
# 8.- Si el token es un operador, lo agregamos a la expresión evaluada.
# 9.- Si encontramos un token que no reconocemos, lanzamos un error.
# 10.- Finalmente, devolvemos la expresión evaluada, eliminando los posibles espacios en blanco al principio y al final.
# 11.- Definimos la expresión a analizar y los valores de las variables en el diccionario variables.
# 12.- Llamamos a la función analyze_semantics con la expresión y el diccionario de variables como argumentos.
# 13.- Imprimimos el resultado o el mensaje de error si ocurre algún problema durante el análisis semántico