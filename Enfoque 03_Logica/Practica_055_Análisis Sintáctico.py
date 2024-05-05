#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# El análisis sintáctico, también conocido como parsing, es una etapa fundamental en el proceso de compilación de un programa.
# Su objetivo principal es analizar la estructura gramatical del código fuente y determinar si cumple con las reglas sintácticas 
# del lenguaje de programación. Para lograr esto, el análisis sintáctico utiliza una gramática formal que define la
# estructura sintáctica del lenguaje.

# Existen diferentes tipos de análisis sintáctico, como el análisis sintáctico descendente (top-down),
# el análisis sintáctico ascendente (bottom-up) y el análisis sintáctico LR. Cada tipo de análisis tiene 
# sus propias características y se utiliza en diferentes contextos dependiendo del lenguaje y de los requisitos del compilador.

# En términos generales, el análisis sintáctico se lleva a cabo en varias etapas:

# 1.- Tokenización: En esta etapa, el código fuente se divide en tokens o lexemas, que son las unidades básicas de la sintaxis 
#     del lenguaje. Esto implica reconocer palabras clave, identificadores, literales, operadores, etc.
# 2.- Construcción del Árbol Sintáctico: Una vez que se han identificado los tokens, se utiliza la gramática del 
#     lenguaje para construir un árbol sintáctico que representa la estructura jerárquica del programa. Este árbol 
#     se utiliza para representar la relación entre las distintas partes del código y facilitar su análisis posterior.
# 3.- Verificación de la Gramática: Durante esta etapa, se verifican las reglas gramaticales del lenguaje para asegurarse 
#     de que el código fuente cumple con ellas. Esto incluye comprobar que las declaraciones estén correctamente formadas,
#     que los tipos de datos sean consistentes y que no haya ambigüedades en la estructura del programa.
# 4.- Generación de Errores: Si se encuentran errores sintácticos en el código fuente, se generan mensajes de error 
#     que indican la ubicación y la naturaleza del problema. Estos mensajes son útiles para que el programador pueda 
#     corregir los errores y mejorar la calidad del código.
#--------------- PROGRAMA ------------------------------------
def analisis_sintactico(cadena):
    pila = []  # Creamos una pila para almacenar los paréntesis abiertos
    
    for caracter in cadena:
        if caracter == '(':
            pila.append(caracter)  # Si encontramos un paréntesis abierto, lo agregamos a la pila
        elif caracter == ')':
            if not pila:  # Si la pila está vacía y encontramos un paréntesis cerrado, la secuencia está desequilibrada
                return False
            else:
                pila.pop()  # Si hay un paréntesis abierto en la pila, lo eliminamos
            
    return not pila  # Si la pila está vacía al final, la secuencia está equilibrada

# Ejemplo de uso
cadena1 = "()()((()))"
cadena2 = "(()"
cadena3 = "())"

print("Cadena 1:", analisis_sintactico(cadena1))  # Debería devolver True
print("Cadena 2:", analisis_sintactico(cadena2))  # Debería devolver False
print("Cadena 3:", analisis_sintactico(cadena3))  # Debería devolver False

#-----------------------------------------------------------------------------------
# 1.- Definimos una función analisis_sintactico que toma una cadena como entrada y devuelve True 
#     si la secuencia de paréntesis está correctamente equilibrada, y False en caso contrario.
# 2.- Creamos una pila para almacenar los paréntesis abiertos.
# 3.- Iteramos sobre cada caracter de la cadena. Si encontramos un paréntesis abierto, lo agregamos a la pila. 
#     Si encontramos un paréntesis cerrado, verificamos si la pila está vacía. Si está vacía, significa que la 
#     secuencia está desequilibrada. Si hay un paréntesis abierto en la pila, lo eliminamos.
# 4.- Al final, si la pila está vacía, significa que la secuencia está correctamente equilibrada y devolvemos True.
#     En caso contrario, devolvemos False.
# 5.- Finalmente, probamos la función con algunas cadenas de ejemplo e imprimimos los resultados en la consola.