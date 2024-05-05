#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# El algoritmo de Ponderación de Verosimilitud (Likelihood Weighting en inglés) es un método utilizado en la inferencia bayesiana para estimar la 
# distribución de probabilidad posterior de los parámetros de un modelo estadístico, dados los datos observados. Este algoritmo es particularmente 
# útil cuando no es posible calcular la distribución posterior de manera analítica, como ocurre en modelos muy complejos o con datos no lineales.


# Funcionamiento del Algoritmo de Ponderación de Verosimilitud:
# 1.- Definición del Modelo Estadístico: Se define el modelo estadístico que describe la relación entre los datos observados y 
# los parámetros del modelo. Esto incluye la especificación de la función de verosimilitud, que describe la probabilidad de los datos 
# observados dado un conjunto de parámetros.
# 2.- Generación de Muestras Ponderadas: Se generan muestras aleatorias de los parámetros del modelo utilizando una distribución previa. 
# Cada muestra se pondera por la verosimilitud de los datos observados dado ese conjunto de parámetros.
# 3.- Cálculo de la Distribución Posterior: Se calcula la distribución de probabilidad posterior de los parámetros del modelo sumando las 
# ponderaciones de las muestras que caen en cada rango de valores de los parámetros.
# 4 .-Estimación de la Incertidumbre: A partir de la distribución posterior de los parámetros, se puede estimar la incertidumbre asociada 
# con cada parámetro y realizar inferencias sobre el modelo.

#--------------- PROGRAMA ------------------------------------

import numpy as np

# Definición de la función de verosimilitud
def verosimilitud(parametro, datos):
    # Calcular la verosimilitud utilizando una distribución normal
    media = parametro
    desviacion_estandar = 1
    verosimilitud = np.prod(1 / (np.sqrt(2 * np.pi) * desviacion_estandar) * np.exp(-(datos - media)**2 / (2 * desviacion_estandar**2)))
    return verosimilitud

# Definición de la función de ponderación de verosimilitud
def ponderacion_verosimilitud(parametros_propuestos, datos):
    # Calcular la verosimilitud para cada parámetro propuesto
    verosimilitudes = [verosimilitud(parametro, datos) for parametro in parametros_propuestos]
    
    # Calcular las ponderaciones como las verosimilitudes normalizadas
    suma_verosimilitudes = np.sum(verosimilitudes)
    ponderaciones = [verosimilitud / suma_verosimilitudes for verosimilitud in verosimilitudes]
    
    return ponderaciones

# Datos observados
datos = np.array([1.2, 2.5, 3.8, 4.1, 5.5])

# Parámetros propuestos
parametros_propuestos = np.array([2.0, 3.0, 4.0, 5.0, 6.0])

# Calcular las ponderaciones de verosimilitud
ponderaciones = ponderacion_verosimilitud(parametros_propuestos, datos)

# Imprimir las ponderaciones
print("Ponderaciones de Verosimilitud:", ponderaciones)
#--------------------------------------------------------------
# 1.- Definición de la función de verosimilitud: La función verosimilitud calcula la verosimilitud de los datos observados dado un parámetro utilizando 
#     una distribución normal con media igual al parámetro y desviación estándar igual a 1. Se utiliza la función np.prod para calcular el producto de todas 
#     las verosimilitudes individuales.
# 2.- Definición de la función de ponderación de verosimilitud: La función ponderacion_verosimilitud calcula las ponderaciones de verosimilitud para una lista de 
#     parámetros propuestos. Para cada parámetro propuesto, se calcula su verosimilitud utilizando la función anterior, y luego se normaliza dividiendo cada verosimilitud 
#     por la suma total de todas las verosimilitudes.
# 3.- Datos observados y parámetros propuestos: Se definen los datos observados y los parámetros propuestos para el modelo.
# 4.- Cálculo de las ponderaciones de verosimilitud: Se llama a la función ponderacion_verosimilitud para calcular las ponderaciones de verosimilitud para los 
#     parámetros propuestos dados los datos observados.
# 5.- Impresión de las ponderaciones: Se imprime el resultado final, que son las ponderaciones de verosimilitud calculadas.