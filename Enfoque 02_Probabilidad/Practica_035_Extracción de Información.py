#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.
#-----------------TEORIA----------------------------------------
# La "Extracción de Información" (EI) es un proceso crucial en el campo del procesamiento del lenguaje natural (PLN) y la inteligencia artificial (IA)
# que se utiliza para identificar y extraer información estructurada y relevante de un conjunto de datos no estructurado o semiestructurado, como documentos 
# de texto, páginas web, correos electrónicos, entre otros.

# La EI se utiliza para transformar grandes volúmenes de datos sin procesar en información más accesible y comprensible, lo que facilita la búsqueda, 
# la recuperación de información, el análisis de datos y la toma de decisiones automatizada en diversos dominios, como la minería de texto, la inteligencia 
# mpresarial, la extracción de conocimiento, la recuperación de información y la generación de resúmenes, entre otros.

# El proceso de Extracción de Información generalmente implica varias etapas:

# Preprocesamiento de datos: En esta etapa, los datos de entrada se limpian y normalizan para eliminar ruido, caracteres especiales y formatos no deseados.
# Análisis lingüístico: Se realizan tareas de análisis lingüístico, como tokenización, análisis morfológico, lematización y análisis sintáctico, 
# para comprender la estructura y el significado del texto.
# Identificación de entidades: Se identifican y se clasifican entidades relevantes en el texto, como nombres de personas, organizaciones, ubicaciones, 
# fechas, cantidades, entre otros.
# Relación de extracción: Se extraen relaciones entre las entidades identificadas para comprender la estructura y la semántica del texto.
# Resumen y presentación de resultados: Finalmente, se resumen y presentan los resultados de manera comprensible y útil para el usuario final, 
# como tablas, gráficos, informes o respuestas a consultas específicas.

#--------------- PROGRAMA --------------------------------------
import re  # Importar el módulo de expresiones regulares

def extraer_informacion(texto):
    # Definir patrones de búsqueda usando expresiones regulares
    patron_nombre = r'[A-Z][a-z]+ [A-Z][a-z]+'  # Patrón para nombres de personas
    patron_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'  # Patrón para direcciones de correo electrónico

    # Buscar nombres y direcciones de correo electrónico en el texto
    nombres = re.findall(patron_nombre, texto)
    emails = re.findall(patron_email, texto)

    # Imprimir los resultados encontrados
    print("Nombres encontrados:")
    for nombre in nombres:
        print(nombre)
    
    print("\nDirecciones de correo electrónico encontradas:")
    for email in emails:
        print(email)

# Texto de ejemplo
texto_ejemplo = """
Hola, mi nombre es Juan Pérez y mi dirección de correo electrónico es juan.perez@example.com.
Puedes contactarme en esa dirección si tienes alguna pregunta.
Además, también puedes escribir a maria.gonzalez@example.com.
"""

# Llamar a la función de extracción de información con el texto de ejemplo
extraer_informacion(texto_ejemplo)

#------------------------------------------------------------------------------------------
# 1.- Importar el módulo de expresiones regulares (re): import re importa el módulo re, que proporciona funciones para trabajar con expresiones regulares en Python.
# 2.- Definir patrones de búsqueda: Se definen dos patrones de búsqueda utilizando expresiones regulares. patron_nombre busca nombres de personas 
#     y patron_email busca direcciones de correo electrónico.
# 3.- Buscar nombres y direcciones de correo electrónico: re.findall() busca todas las coincidencias de los patrones definidos en el texto dado.
# 4.- Imprimir los resultados encontrados: Los nombres y direcciones de correo electrónico encontrados se imprimen en la consola.
# 5.- Texto de ejemplo: Se proporciona un texto de ejemplo que contiene nombres y direcciones de correo electrónico.
# 6.- Llamar a la función de extracción de información: Se llama a la función extraer_informacion() con el texto de ejemplo como argumento.