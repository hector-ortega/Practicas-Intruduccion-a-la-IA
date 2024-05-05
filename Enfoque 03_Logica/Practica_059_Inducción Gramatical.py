#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------

# La inducción gramatical es un proceso mediante el cual se analizan ejemplos de lenguaje natural para inferir reglas gramaticales que describan 
# la estructura y el significado de las frases en ese idioma. Este proceso es fundamental en el campo del procesamiento del lenguaje natural (PLN)
# y tiene varias aplicaciones importantes:

# 1.- Modelado de lenguaje: La inducción gramatical puede utilizarse para aprender modelos de lenguaje probabilísticos que ayudan a predecir 
#     la probabilidad de ocurrencia de palabras o secuencias de palabras en un determinado contexto.
# 2.- Traducción automática: Al analizar grandes cantidades de texto en diferentes idiomas, la inducción gramatical puede ayudar a identificar
#     patrones gramaticales y construir modelos que faciliten la traducción automática entre idiomas.
# 3.- Generación de lenguaje natural: La capacidad de inferir reglas gramaticales a partir de ejemplos permite
#     a los sistemas de inteligencia artificial generar texto coherente y gramaticalmente correcto de manera automática.
# 4.- Extracción de información: En aplicaciones como la minería de texto, la inducción gramatical puede utilizarse para 
#     identificar entidades y relaciones clave en un corpus de texto, lo que facilita la extracción de información útil.
# 5.- Análisis de sentimientos: Al comprender la estructura gramatical de las frases, los algoritmos de inducción gramatical 
#     pueden ayudar en el análisis de sentimientos, identificando las opiniones y emociones expresadas en el texto.


#--------------- PROGRAMA ------------------------------------
import re

def induce_grammar(sentences):
    grammar = {}
    for sentence in sentences:
        # Tokenizar la oración en palabras
        words = re.findall(r'\b\w+\b', sentence)
        if len(words) >= 3:
            # Extraer la estructura sujeto-verbo-objeto (SVO)
            subject, verb, obj = words[:3]
            if subject not in grammar:
                grammar[subject] = {}
            if verb not in grammar[subject]:
                grammar[subject][verb] = []
            grammar[subject][verb].append(obj)
    return grammar

# Ejemplos de oraciones
sentences = [
    "The cat eats fish",
    "The dog chases the cat",
    "The bird sings a song"
]

# Obtener la gramática inducida
induced_grammar = induce_grammar(sentences)

# Imprimir la gramática inducida
print("Gramática Inducida:")
for subject, verbs in induced_grammar.items():
    print(f"{subject}:")
    for verb, objects in verbs.items():
        print(f"  {verb}: {', '.join(objects)}")

#--------------------------------------------------------
# 1.- Importamos el módulo re para trabajar con expresiones regulares, que nos ayudará a tokenizar las oraciones.
# 2.- Definimos la función induce_grammar que toma una lista de oraciones como entrada y devuelve la gramática inducida.
# 3.- Iteramos sobre cada oración en la lista de oraciones.
# 4.- Usamos una expresión regular para tokenizar la oración en palabras.
# 5.- Verificamos si la oración tiene al menos tres palabras para extraer la estructura SVO.
# 6.- Extraemos el sujeto, verbo y objeto de la oración.
# 7.- Construimos la estructura de la gramática inducida.
# 8.- Devolvemos la gramática inducida al final de la función.
# 9.- Definimos una lista de oraciones de ejemplo.
# 10.- Llamamos a la función induce_grammar con la lista de oraciones de ejemplo para obtener la gramática inducida.
# 11.- Imprimimos la gramática inducida.