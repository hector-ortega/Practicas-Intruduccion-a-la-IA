#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.
#-----------------TEORIA----------------------------------------
# Utilización del Algoritmo FPSE:
# 1.- Filtrado: En la etapa de filtrado, el algoritmo utiliza las observaciones disponibles hasta el momento para estimar el estado actual del sistema. 
#     Esto se hace teniendo en cuenta tanto el modelo dinámico del sistema como las mediciones realizadas. El resultado es una estimación del estado actual
#     del sistema, junto con una medida de incertidumbre asociada.
# 2.- Predicción: En la etapa de predicción, el algoritmo utiliza el estado estimado en el paso anterior para predecir el estado del sistema en el siguiente
#     paso de tiempo. Esto se hace teniendo en cuenta el modelo dinámico del sistema y las posibles perturbaciones del proceso. La predicción proporciona una 
#     estimación del estado futuro del sistema, junto con una medida de incertidumbre asociada.
# 3.- Suavizado: En la etapa de suavizado, el algoritmo utiliza tanto las observaciones pasadas como las futuras para mejorar la estimación del estado del sistema 
#     en cada paso de tiempo. Esto se hace utilizando una técnica recursiva que combina las estimaciones filtradas y las predicciones suavizadas para producir una 
#     estimación más precisa del estado del sistema.
# 4.- Explicación: En la etapa de explicación, el algoritmo proporciona información adicional sobre el comportamiento del sistema, como la covarianza del estado estimado,
#     la covarianza de la predicción y la ganancia de Kalman. Esta información puede ser útil para comprender cómo se realizan las estimaciones y cuánto 
#     se puede confiar en ellas.

# Funcionamiento del Algoritmo FPSE:
# El algoritmo de FPSE se basa en el filtro de Kalman, que utiliza un modelo probabilístico lineal para estimar el estado de un sistema dinámico. 
# El proceso se lleva a cabo en dos etapas principales: predicción y actualización.

# -- Predicción: En esta etapa, se utiliza el modelo dinámico del sistema para predecir el estado futuro del sistema, dado el estado actual. Esto se hace 
#     calculando la predicción del estado y la covarianza de la predicción.
# -- Actualización: En esta etapa, se combinan las observaciones disponibles con la predicción del estado para producir una estimación actualizada del estado
#     del sistema. Esto se hace calculando la ganancia de Kalman, que determina cómo se deben ponderar las observaciones y la predicción en la estimación final del
#     estado.
#--------------- PROGRAMA ------------------------------------
import numpy as np

def filtro_kalman(y, A, H, Q, R, mu_0, Sigma_0):
    """
    Implementación del filtro de Kalman.
    
    Argumentos:
    - y: Observaciones.
    - A: Matriz de transición de estado.
    - H: Matriz de observación.
    - Q: Covarianza del ruido del proceso.
    - R: Covarianza del ruido de la medición.
    - mu_0: Media inicial del estado.
    - Sigma_0: Covarianza inicial del estado.
    
    Retorna:
    - mu: Medias filtradas.
    - Sigma: Covarianzas filtradas.
    """
    # Inicialización
    T = len(y)  # Número de pasos de tiempo
    mu = [mu_0]  # Lista para almacenar medias filtradas
    Sigma = [Sigma_0]  # Lista para almacenar covarianzas filtradas
    mu_pred = mu_0  # Inicialización de la media predictiva
    Sigma_pred = Sigma_0  # Inicialización de la covarianza predictiva
    
    # Fase de predicción y actualización
    for t in range(T):
        # Predicción
        mu_pred = A.dot(mu[-1])  # Predicción de la media
        Sigma_pred = A.dot(Sigma[-1]).dot(A.T) + Q  # Predicción de la covarianza
        
        # Actualización
        K = Sigma_pred.dot(H.T).dot(np.linalg.inv(H.dot(Sigma_pred).dot(H.T) + R))  # Ganancia de Kalman
        mu_act = mu_pred + K.dot(y[t] - H.dot(mu_pred))  # Actualización de la media
        Sigma_act = (np.eye(len(mu_0)) - K.dot(H)).dot(Sigma_pred)  # Actualización de la covarianza
        
        # Almacenar las medias y covarianzas filtradas
        mu.append(mu_act)
        Sigma.append(Sigma_act)
        
    return mu, Sigma

# Definición de parámetros
A = np.array([[1, 1], [0, 1]])  # Matriz de transición de estado
H = np.array([[1, 0]])  # Matriz de observación
Q = np.array([[0.01, 0], [0, 0.01]])  # Covarianza del ruido del proceso
R = np.array([[0.1]])  # Covarianza del ruido de la medición
mu_0 = np.array([0, 0])  # Media inicial del estado
Sigma_0 = np.eye(2)  # Covarianza inicial del estado

# Generación de datos sintéticos
np.random.seed(0)
T = 100
y = np.random.normal(0, 1, size=(T, 1))

# Aplicación del filtro de Kalman
mu_filt, Sigma_filt = filtro_kalman(y, A, H, Q, R, mu_0, Sigma_0)

# Impresión de las medias filtradas
print("Medias filtradas:")
print(mu_filt)

#----------------------------------------------------------------------------------------------
# 1- Iías: Importamos la librería numpy para realizar operaciones matriciales.
# 2.- Definición de la función filtro_kalman: Esta función implementa el filtro de Kalman. Toma como entrada las observaciones y, las matrices A y H, 
#     las covarianzas Q y R, y las medias y covarianzas iniciales del estado. Devuelve las medias y covarianzas filtradas.
# 3.- Inicialización de variables: Inicializamos las variables necesarias para el filtro de Kalman.
# 4.- Fase de predicción y actualización: Iteramos a través de cada paso de tiempo. En cada paso, realizamos la fase de predicción para estimar el estado siguiente 
#     y luego la fase de actualización para corregir la estimación utilizando la observación actual.
# 5.- Definición de parámetros: Definimos los parámetros del modelo de filtro de Kalman, incluyendo la matriz de transición de estado A, la matriz de observación H, 
#     las covarianzas del ruido del proceso Q y de la medición R, y las medias y covarianzas iniciales del estado.
# 6.- Generación de datos sintéticos: Generamos datos sintéticos y para demostrar el funcionamiento del filtro de Kalman.
# 7.- Aplicación del filtro de Kalman: Llamamos a la función filtro_kalman con los datos sintéticos y los parámetros definidos.
# 8.- Impresión de las medias filtradas: Imprimimos las medias filtradas del estado para verificar el funcionamiento del algoritmo.mportación de librer