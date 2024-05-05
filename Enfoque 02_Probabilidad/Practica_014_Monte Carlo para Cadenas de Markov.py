#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# Funcionamiento del Algoritmo de MCMC:
# El algoritmo de MCMC genera muestras de una distribución de probabilidad desconocida utilizando una cadena de Markov. La idea básica es simular una cadena de estados,
# donde cada estado representa una posible configuración de las variables del sistema. La cadena se construye de tal manera que las probabilidades estacionarias de
# los estados coinciden con la distribución de probabilidad deseada.

# El algoritmo funciona de la siguiente manera:

# 1.- Inicialización: Se elige un estado inicial de manera aleatoria o determinística.
# 2.- Proposición de Movimiento: Se propone un nuevo estado de la cadena utilizando una regla de transición que depende del estado actual. Esto se hace típicamente
#     de forma aleatoria.
# 3.- Aceptación o Rechazo: Se decide si se acepta o se rechaza la propuesta de movimiento basándose en una regla de aceptación que depende de la probabilidad de 
#     transición y de la distribución objetivo.
# 4.- Iteración: Se repiten los pasos 2 y 3 un número suficiente de veces para que la cadena de Markov alcance su distribución estacionaria. Durante esta iteración, 
#     se recogen las muestras generadas por la cadena.
# 5.- Estabilización y Convergencia: Se realiza un análisis para determinar si la cadena ha convergido a su distribución estacionaria y si se ha estabilizado.
# 6.- Obtención de las Muestras: Las muestras generadas por la cadena de Markov se utilizan para estimar la distribución de probabilidad deseada y realizar 
#     inferencias sobre el sistema.

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
#----------------------------------------------------------------------------------------------------
# 1.- Definición de la Función de Densidad de Probabilidad Objetivo (PDF): La función pdf_objetivo(x) define la distribución de probabilidad objetivo de la cual 
#     queremos generar muestras. En este ejemplo, utilizamos una distribución normal con media 5 y desviación estándar 1.
# 3.- Algoritmo de Monte Carlo para Cadenas de Markov (MCMC): La función mcmc(num_iteraciones) implementa el algoritmo de MCMC. Comenzamos con una estimación inicial
#     de x_actual y luego generamos muestras iterativamente utilizando el método de aceptación y rechazo basado en la razón de probabilidad.
# 4.- Ejecución del Algoritmo MCMC: Ejecutamos el algoritmo MCMC con un número específico de iteraciones para generar muestras de la distribución objetivo.
# 5.- Impresión de las Muestras Generadas: Imprimimos algunas muestras generadas por el algoritmo para verificar que funcione correctamente.