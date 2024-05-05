#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# El algoritmo de Mejor Hipótesis Actual (MHA) se utiliza en el contexto del aprendizaje supervisado para encontrar la hipótesis más 
# adecuada que explique un conjunto de datos de entrenamiento observados. Este algoritmo es una forma de aprendizaje inductivo, donde
# a partir de ejemplos de entrenamiento se genera una regla general que se espera que sea válida para predecir la clasificación de nuevas instancias.

# La idea principal detrás del algoritmo de MHA es comenzar con una hipótesis inicial que sea la más general posible y luego refinarla
# iterativamente a medida que se examinan los ejemplos de entrenamiento. La hipótesis inicial puede ser una regla general que se aplique 
# a todas las instancias del problema, y luego se ajusta para adaptarse mejor a los datos observados.

# El proceso de refinamiento implica agregar características a la hipótesis inicial si están presentes en todos los ejemplos positivos,
# y eliminar características si están presentes en algún ejemplo negativo. Esto se hace para encontrar la hipótesis más específica que 
# aún sea consistente con todos los ejemplos positivos y negativos observados.

# El algoritmo de MHA es útil en la clasificación de datos cuando se tiene un conjunto de ejemplos de entrenamiento etiquetados y se 
# desea encontrar una regla general que pueda clasificar nuevas instancias correctamente.

# Funcionamiento del algoritmo:

# 1.- Comenzar con una hipótesis inicial que sea la más general posible.
# 2.- Iterar sobre los ejemplos de entrenamiento.
# 3.- Para cada ejemplo positivo, agregar características a la hipótesis si están presentes en todos los ejemplos positivos.
# 4.- Para cada ejemplo negativo, eliminar características de la hipótesis si están presentes en algún ejemplo negativo.
# 5.- Devolver la hipótesis resultante como la mejor hipótesis actual.
# #--------------- PROGRAMA ------------------------------------
def mejor_hipotesis_actual(ejemplos_positivos, ejemplos_negativos):
    # Comenzar con la hipótesis más general posible
    hipotesis = set()

    # Para cada ejemplo positivo, agregar características a la hipótesis
    for ejemplo in ejemplos_positivos:
        for caracteristica in ejemplo:
            hipotesis.add(caracteristica)

    # Para cada ejemplo negativo, eliminar características de la hipótesis
    for ejemplo in ejemplos_negativos:
        for caracteristica in ejemplo:
            if caracteristica in hipotesis:
                hipotesis.remove(caracteristica)

    return hipotesis

# Ejemplos de entrenamiento
ejemplos_positivos = [
    {"nublado", "frio", "alta_humedad"},
    {"soleado", "calido", "normal_humedad"},
    {"lluvioso", "templado", "alta_humedad"}
]

ejemplos_negativos = [
    {"soleado", "frio", "alta_humedad"},
    {"nublado", "calido", "normal_humedad"}
]

# Obtener la mejor hipótesis actual
mejor_hipotesis = mejor_hipotesis_actual(ejemplos_positivos, ejemplos_negativos)

# Imprimir la mejor hipótesis actual
print("Mejor hipótesis actual:", mejor_hipotesis)