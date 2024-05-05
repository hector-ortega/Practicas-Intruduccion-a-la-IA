#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.
#-----------------TEORIA----------------------------------------
# La "Recuperación de Datos" se refiere al proceso de encontrar y obtener información relevante a partir de grandes conjuntos de datos o bases de datos. 
# Este proceso es fundamental en una variedad de aplicaciones, incluyendo sistemas de búsqueda en la web, sistemas de recomendación de contenido, sistemas
# de recuperación de información, entre otros.

# En el contexto de la Inteligencia Artificial, la recuperación de datos se utiliza para encontrar documentos, registros o elementos de datos que sean relevantes 
# para una consulta específica o un conjunto de criterios de búsqueda. Los algoritmos de recuperación de datos se diseñan para analizar y comparar los datos disponibles 
# con la consulta del usuario, con el objetivo de identificar y presentar los resultados más relevantes de manera eficiente.

# El funcionamiento de un algoritmo de recuperación de datos puede variar según la técnica utilizada. Sin embargo, en términos generales, el proceso implica los 
# siguientes pasos:

# 1.- Indexación: Primero, se crea un índice de los datos disponibles para facilitar la búsqueda rápida y eficiente. Esto puede implicar la creación de estructuras de 
# datos como árboles de búsqueda, tablas hash o índices invertidos, que permiten acceder rápidamente a los datos relevantes.
# 2.- Preprocesamiento de Consultas: Antes de realizar la búsqueda, se preprocesa la consulta del usuario para limpiarla, normalizarla y transformarla en una forma
# adecuada para la comparación con los datos indexados. Esto puede incluir la eliminación de palabras irrelevantes (stopwords), la lematización o el stemming de 
# las palabras, y la conversión a minúsculas, entre otras técnicas.
# 3.- Búsqueda y Comparación: Una vez que la consulta está lista, se utiliza para buscar y comparar con los datos indexados. Dependiendo del algoritmo y la técnica utilizada,
# esta búsqueda puede involucrar la comparación de términos de consulta con los términos indexados, el cálculo de similitud o relevancia entre la consulta 
# y los documentos, o la recuperación de datos basada en vectores de características.
# 4.- Clasificación y Presentación de Resultados: Finalmente, los resultados de la búsqueda se clasifican y se presentan al usuario de acuerdo con su relevancia.
# Esto puede implicar el uso de algoritmos de clasificación, como el ordenamiento por similitud o la ponderación de términos, para determinar qué documentos 
# son más relevantes para la consulta del usuario.
#--------------- PROGRAMA --------------------------------------
def buscar_documentos(termino, documentos):
    """
    Función para buscar documentos que contienen un término dado.
    
    Args:
    - termino: El término que se busca en los documentos.
    - documentos: Una lista de documentos representados como cadenas de texto.
    
    Returns:
    - Una lista de índices de los documentos que contienen el término.
    """
    resultados = []  # Lista para almacenar los índices de los documentos que contienen el término
    
    # Iterar sobre cada documento y buscar el término
    for i, documento in enumerate(documentos):
        if termino in documento:
            resultados.append(i)  # Agregar el índice del documento a los resultados
    
    return resultados


# Ejemplo de uso
if __name__ == "__main__":
    # Definir una lista de documentos
    documentos = [
        "Este es un ejemplo de documento",
        "Otro documento que contiene información relevante",
        "Documento final para probar la recuperación de datos"
    ]
    
    # Término a buscar
    termino_busqueda = "documento"
    
    # Buscar documentos que contienen el término especificado
    resultados = buscar_documentos(termino_busqueda, documentos)
    
    # Imprimir los resultados
    if resultados:
        print(f"Se encontraron documentos que contienen el término '{termino_busqueda}':")
        for indice in resultados:
            print(f"Documento {indice}: {documentos[indice]}")
    else:
        print(f"No se encontraron documentos que contengan el término '{termino_busqueda}'")

