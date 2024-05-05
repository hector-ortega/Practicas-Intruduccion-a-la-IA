#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------

# Los procesos estacionarios son fundamentales en el análisis de series temporales y en diversas áreas de la ciencia e ingeniería. 
# Se utilizan para modelar y analizar el comportamiento de variables que cambian con el tiempo, como el precio de las acciones, la temperatura atmosférica,
# las señales de audio, entre otros. 

# 1.- Utilización de los Procesos Estacionarios:
# 2.- Modelado de Fenómenos Temporales: Los procesos estacionarios se utilizan para modelar fenómenos que varían con el tiempo, permitiendo comprender su comportamiento 
#     y hacer predicciones sobre su evolución futura.
# 3.- Pronósticos y Predicciones: Al analizar el comportamiento pasado de un proceso estacionario, se pueden hacer pronósticos y predicciones sobre su comportamiento futuro.
#     Esto es útil en áreas como la economía, la climatología y la ingeniería, donde es importante predecir el comportamiento futuro de variables temporales.
# 4.- Análisis de Señales: En el procesamiento de señales, los procesos estacionarios se utilizan para modelar y analizar señales temporales, como señales de audio, 
#     imágenes 
#     médicas o datos de sensores.
# 5.- Control de Procesos: En ingeniería y manufactura, los procesos estacionarios se utilizan para controlar y optimizar procesos industriales, como 
#     la producción de productos químicos o la fabricación de productos electrónicos.
#--------------- PROGRAMA ------------------------------------
import numpy as np

# Definición de la función de densidad de probabilidad objetivo (PDF)
def pdf_objetivo(x):
    # En este ejemplo, utilizaremos una distribución normal como PDF objetivo
    media = 5
    desviacion_estandar = 1
    return np.exp(-0.5 * ((x - media) / desviacion_estandar) ** 2) / (desviacion_estandar * np.sqrt(2 * np.pi))

# Algoritmo de Monte Carlo para Cadenas de Markov (MCMC)
def mcmc(num_iteraciones):
    # Inicializamos el algoritmo con una estimación inicial de x
    x_actual = np.random.normal(0, 1)
    
    # Lista para almacenar las muestras generadas por el algoritmo
    muestras = []
    
    # Iteramos el algoritmo para generar las muestras
    for _ in range(num_iteraciones):
        # Generamos una propuesta de nuevo valor para x utilizando una distribución normal centrada en x_actual
        x_propuesto = np.random.normal(x_actual, 1)
        
        # Calculamos la razón entre las probabilidades de aceptar x_propuesto y x_actual
        razon = pdf_objetivo(x_propuesto) / pdf_objetivo(x_actual)
        
        # Aceptamos el nuevo valor propuesto con una probabilidad igual a la razón
        if np.random.uniform(0, 1) < razon:
            x_actual = x_propuesto
        
        # Agregamos el valor actual de x a la lista de muestras
        muestras.append(x_actual)
    
    return muestras

# Número de iteraciones del algoritmo MCMC
num_iteraciones = 10000

# Ejecutamos el algoritmo MCMC para generar muestras de la distribución objetivo
muestras = mcmc(num_iteraciones)

# Imprimimos algunas muestras para verificar que el algoritmo funciona correctamente
print("Muestras generadas por el algoritmo MCMC:")
print(muestras[:10])

#---------------------------------------------------------------------------------------------
# 1.- Definición de la Función de Densidad de Probabilidad Objetivo (PDF): La función pdf_objetivo(x) define la distribución de probabilidad objetivo de 
#     la cual queremos generar muestras. En este ejemplo, utilizamos una distribución normal con media 5 y desviación estándar 1.
# 2.- Algoritmo de Monte Carlo para Cadenas de Markov (MCMC): La función mcmc(num_iteraciones) implementa el algoritmo de MCMC. Comenzamos 
#     con una estimación inicial de x_actual y luego generamos muestras iterativamente utilizando el método de aceptación y rechazo basado en la razón de probabilidad.
# 3.- Ejecución del Algoritmo MCMC: Ejecutamos el algoritmo MCMC con un número específico de iteraciones para generar muestras de la distribución objetivo.
# 4.- Impresión de las Muestras Generadas: Imprimimos algunas muestras generadas por el algoritmo para verificar que funcione correctamente.