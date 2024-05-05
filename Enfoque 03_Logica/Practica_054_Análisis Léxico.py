#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# El análisis léxico es el primer paso en el proceso de compilación de un programa. Su objetivo es escanear el código fuente y dividirlo en unidades
# léxicas o tokens significativos para el compilador o intérprete. Estos tokens son elementos básicos del lenguaje de programación, como palabras clave, 
# identificadores, números, operadores y símbolos especiales.

# Funcionamiento:

# 1.- Escaneo del Código Fuente: El analizador léxico escanea el código fuente caracter por caracter, identificando tokens 
#     y agrupándolos en categorías predefinidas, como palabras clave, identificadores, números, etc.
# 2.- Definición de Reglas: El analizador léxico utiliza reglas predefinidas, generalmente expresiones regulares, 
#     para identificar patrones de caracteres que corresponden a diferentes tipos de tokens.
# 3.- Generación de Tokens: Cuando se encuentra un patrón que coincide con una regla, se genera un token que representa ese 
#     elemento léxico junto con cualquier información adicional relevante, como el valor del token y su posición en el código fuente.
# 4.- Ignorar Espacios en Blanco y Comentarios: El analizador léxico generalmente ignora los espacios en blanco y los comentarios en el código fuente,
#     ya que no son relevantes para la generación de tokens.
#--------------- PROGRAMA ------------------------------------
import re

# Definimos las expresiones regulares para identificar palabras clave y números
keyword_pattern = re.compile(r'\b(if|else|for|while|return)\b')
number_pattern = re.compile(r'\b\d+\b')

# Función para analizar el código fuente y generar la lista de tokens
def lexer(source_code):
    tokens = []
    # Dividir el código fuente en líneas y procesar cada línea
    for line_number, line in enumerate(source_code.split('\n'), start=1):
        # Buscar palabras clave en la línea
        for match in keyword_pattern.finditer(line):
            tokens.append(('KEYWORD', match.group(0), line_number))
        # Buscar números en la línea
        for match in number_pattern.finditer(line):
            tokens.append(('NUMBER', match.group(0), line_number))
    return tokens

# Código fuente de ejemplo
source_code = """
for i in range(10):
    if i % 2 == 0:
        print(i)
"""

# Ejecutar el analizador léxico y mostrar los tokens resultantes
tokens = lexer(source_code)
for token in tokens:
    print(token)

#--------------------------------------------------------------
# 1.- Importamos el módulo re para trabajar con expresiones regulares.
# 2.- Definimos dos expresiones regulares: una para identificar palabras clave y otra para identificar números.
# 3.- La función lexer recibe el código fuente como entrada y devuelve una lista de tokens.
# 4.- Dentro de la función lexer, dividimos el código fuente en líneas y procesamos cada línea individualmente.
# 5.- Para cada línea, buscamos coincidencias con las expresiones regulares de palabras clave y números.
# 6.- Por cada coincidencia encontrada, añadimos un token a la lista de tokens, que consiste en una tupla con el tipo de token 
#     ('KEYWORD' o 'NUMBER'), el valor encontrado y el número de línea.
# 7.- Finalmente, ejecutamos el analizador léxico con un ejemplo de código fuente y mostramos los tokens resultantes en la consola.