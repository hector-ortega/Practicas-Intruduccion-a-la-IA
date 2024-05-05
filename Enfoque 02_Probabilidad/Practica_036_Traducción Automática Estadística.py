#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.
#-----------------TEORIA----------------------------------------

# La Traducción Automática Estadística (TAE) es un enfoque dentro del campo del procesamiento del lenguaje natural (PLN) que se utiliza para traducir 
# automáticamente el texto de un idioma de origen a otro idioma de destino. Este enfoque se basa en el análisis estadístico de grandes conjuntos 
# de datos lingüísticos para encontrar patrones y regularidades que permitan realizar traducciones precisas.

# Funcionamiento:
# - Colección de datos: En primer lugar, se recopilan grandes cantidades de datos de texto en ambos idiomas de interés. Estos datos 
#   pueden ser corpus de texto paralelo, que consisten en textos que están alineados entre los dos idiomas, o corpus comparables, que contienen
#   textos en los dos idiomas pero no necesariamente alineados.
# - Preprocesamiento de datos: Los datos recopilados se someten a un proceso de preprocesamiento, que puede incluir la tokenización, eliminación 
#   de signos de puntuación, conversión a minúsculas, etc.
# - Extracción de características: A partir de los datos preprocesados, se extraen características lingüísticas relevantes, como palabras, n-gramas,
#   oraciones, etc. Estas características se utilizan para construir modelos estadísticos.
# - Entrenamiento del modelo: Se entrenan modelos estadísticos utilizando algoritmos de aprendizaje automático, como modelos de lenguaje, modelos de 
#   traducción, modelos de alineación, etc. Estos modelos utilizan las características extraídas de los datos de entrenamiento para aprender las
#   asociaciones entre las palabras y las estructuras de las frases en ambos idiomas.
# - Generación de traducciones: Una vez que los modelos están entrenados, se pueden utilizar para generar traducciones de texto de un idioma de
#   origen a un idioma de destino. Durante este proceso, se utilizan técnicas como la búsqueda del mejor camino o la decodificación del modelo 
#   para seleccionar la secuencia de palabras de destino que mejor se adapte al texto de origen.
# - Evaluación y refinamiento: Las traducciones generadas se evalúan utilizando métricas de evaluación automáticas o mediante la revisión humana. 
#   Si es necesario, los modelos se refinan utilizando técnicas como el ajuste de hiperparámetros, la adición de datos de entrenamiento adicionales, etc.

#--------------- PROGRAMA --------------------------------------
# Definimos un diccionario de traducción
diccionario_traduccion = {
    'hello': 'hola',
    'world': 'mundo',
    'cat': 'gato',
    'dog': 'perro',
    'good': 'bueno',
    'morning': 'mañana',
    'how': 'cómo',
    'are': 'estás',
    'you': 'tú'
}

def traduccion_estadistica(frase, diccionario):
    palabras = frase.split()  # Dividir la frase en palabras
    traduccion = []  # Lista para almacenar las palabras traducidas
    
    # Iterar sobre cada palabra de la frase
    for palabra in palabras:
        if palabra in diccionario:  # Verificar si la palabra está en el diccionario
            traduccion.append(diccionario[palabra])  # Agregar la traducción al resultado
        else:
            traduccion.append(palabra)  # Mantener la palabra sin traducir si no está en el diccionario
    
    return ' '.join(traduccion)  # Unir las palabras traducidas en una frase

# Ejemplo de uso
frase_original = "hello world, how are you?"
print("Frase original:", frase_original)

# Realizar la traducción
frase_traducida = traduccion_estadistica(frase_original, diccionario_traduccion)
print("Frase traducida:", frase_traducida)

#-----------------------------------------------------------------------------
# 1.- Definimos un diccionario de traducción llamado diccionario_traduccion, donde las claves son palabras en inglés y los valores son sus traducciones en español.
# 2.- Creamos una función llamada traduccion_estadistica que toma una frase en inglés y el diccionario de traducción como entrada y devuelve la frase traducida.
# 3.- Dividimos la frase en palabras utilizando el método split() y almacenamos las palabras en la lista palabras.
# 4.- Iteramos sobre cada palabra de la lista palabras.
# 5.- Verificamos si la palabra está en el diccionario de traducción.
# 6.- Si la palabra está en el diccionario, agregamos su traducción a la lista traduccion.
# 7.- Si la palabra no está en el diccionario, mantenemos la palabra sin cambios.
# 8.- Finalmente, unimos las palabras traducidas en una frase utilizando el método join() y la retornamos.