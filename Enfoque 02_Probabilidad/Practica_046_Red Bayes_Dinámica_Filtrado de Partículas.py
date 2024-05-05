#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.
#-----------------TEORIA----------------------------------------
#  El algoritmo de Red Bayesiana Dinámica, también conocido como filtro de partículas, es un método de estimación de estado que
# utiliza una colección de muestras llamadas partículas para aproximar la distribución de probabilidad del estado de un sistema dinámico. 
# Se utiliza en situaciones donde el modelo del sistema es no lineal, no gaussiano o donde la distribución de probabilidad del estado no
# puede ser representada de manera analítica.

# El algoritmo funciona de la siguiente manera:

# 1.- Inicialización: En el inicio del algoritmo, se generan un conjunto de partículas aleatorias que representan posibles estados del sistema. 
#     Cada partícula tiene asociado un peso que indica la probabilidad de que esa partícula sea el verdadero estado del sistema.
# 2.- Predicción del estado siguiente: Se utiliza un modelo de transición para predecir el próximo estado del sistema a partir del estado actual.
#     Esta predicción se hace para cada partícula, agregando algún tipo de ruido para representar la incertidumbre en la predicción.
# 3.- Actualización de los pesos: Se utiliza un modelo de medición para calcular la probabilidad de observar los datos actuales dados los estados
#     predichos por cada partícula. Estas probabilidades se utilizan para actualizar los pesos de las partículas, asignando pesos más altos a las 
#     partículas que son más consistentes con las observaciones actuales.
# 4.- Re-muestreo: Las partículas se re-muestrean de acuerdo a sus pesos. Las partículas con pesos más altos tienen una mayor probabilidad de ser seleccionadas, 
#     mientras que las partículas con pesos más bajos tienen una menor probabilidad de ser seleccionadas.
# 5.- Estimación del estado actual: Se estima el estado actual del sistema utilizando las partículas con sus pesos actualizados. 
#     Esto puede hacerse calculando una media ponderada de las posiciones de las partículas o seleccionando la partícula con el peso 
#     más alto como la estimación del estado.
#--------------- PROGRAMA --------------------------------------

import numpy as np

def transition_model(x):
    """Modelo de transición: predice el próximo estado a partir del estado actual."""
    # En este ejemplo, asumimos un movimiento aleatorio con una pequeña perturbación gaussiana
    return x + np.random.normal(0, 1, size=x.shape)

def measurement_model(x):
    """Modelo de medición: calcula la probabilidad de una observación dada un estado."""
    # En este ejemplo, asumimos una distribución gaussiana centrada en el estado actual
    return np.exp(-0.5 * np.sum(x**2))

def resample(weights):
    """Re-muestreo de las partículas basado en sus pesos normalizados."""
    n = len(weights)
    indices = np.random.choice(n, size=n, p=weights)
    return indices

def particle_filter(num_particles, num_steps):
    """Implementación del filtro de partículas."""
    # Inicialización: generar partículas aleatorias y asignarles pesos uniformes
    particles = np.random.normal(0, 1, size=(num_particles, 2))
    weights = np.ones(num_particles) / num_particles
    
    for t in range(num_steps):
        # Predicción del estado siguiente
        particles = transition_model(particles.T).T
        
        # Calcula los pesos de cada partícula basados en la probabilidad de la medición actual
        weights *= measurement_model(particles.T)
        
        # Normaliza los pesos
        weights /= np.sum(weights)
        
        # Re-muestreo de las partículas
        indices = resample(weights)
        particles = particles[indices]
        weights = np.ones(num_particles) / num_particles
        
        # Imprimir el estado estimado
        estimated_state = np.mean(particles, axis=0)
        print(f"Step {t+1}: Estimated state = {estimated_state}")
        

# Parámetros del filtro de partículas
num_particles = 1000  # Número de partículas
num_steps = 10  # Número de pasos de tiempo

# Ejecutar el filtro de partículas
particle_filter(num_particles, num_steps)

#--------------------------------------------------------------
# 1.- transition_model(x): Esta función define el modelo de transición, que predice el próximo estado del sistema a partir del estado actual.
#     En este ejemplo, simplemente agregamos ruido gaussiano al estado actual.
# 2.- measurement_model(x): Esta función define el modelo de medición, que calcula la probabilidad de una observación dada un estado. Aquí, 
#     asumimos una distribución gaussiana centrada en el estado actual.
# 3.- resample(weights): Esta función realiza el re-muestreo de las partículas basado en sus pesos normalizados. Se seleccionan las
#     partículas con mayor peso para replicarlas y las partículas con menor peso se eliminan.
# 4.- particle_filter(num_particles, num_steps): Esta función implementa el filtro de partículas. En cada paso de tiempo, predice el próximo estado, 
#     actualiza los pesos de las partículas basados en la probabilidad de la medición actual, normaliza los pesos, realiza el re-muestreo y 
#     finalmente estima el estado actual.
# 5.- Parámetros del filtro de partículas: Definimos el número de partículas y el número de pasos de tiempo.
# 6.- Ejecución del filtro de partículas: Llamamos a la función particle_filter con los parámetros especificados para ejecutar el algoritmo.