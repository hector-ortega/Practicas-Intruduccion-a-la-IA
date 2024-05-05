#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.
#-----------------TEORIA----------------------------------------
# La incertidumbre es una parte inherente de muchos sistemas del mundo real, especialmente en el campo de la inteligencia artificial y la robótica. 
# Los algoritmos de incertidumbre, como los filtros de Kalman, se utilizan para manejar y mitigar la incertidumbre en los sistemas, permitiendo así
# tomar decisiones más informadas.

# ¿Para qué se utiliza?

# 1.- Estimación de estado: Los algoritmos de incertidumbre se utilizan para estimar el estado de un sistema basándose en observaciones o mediciones, 
#     incluso cuando estas mediciones están sujetas a ruido o perturbaciones.
# 2.- Predicción: También se utilizan para predecir el estado futuro de un sistema, incorporando tanto la dinámica del sistema (modelo de proceso) 
#     como las mediciones recientes.

# Funcionamiento:

# 1.- Modelo de proceso: El algoritmo de incertidumbre utiliza un modelo de proceso que describe cómo evoluciona el estado del sistema con el tiempo.
#     Este modelo puede ser una representación matemática de las leyes físicas que gobiernan el sistema.
# 2.- Modelo de medición: Además del modelo de proceso, el algoritmo utiliza un modelo de medición que describe cómo se relacionan las observaciones 
#     con el estado del sistema. Este modelo puede estar sujeto a errores y ruido.
# 3.- Predicción: El algoritmo comienza con una estimación inicial del estado del sistema y su incertidumbre asociada. Luego, utiliza el modelo de
#     proceso para predecir el próximo estado del sistema y su covarianza.
# 4.- Actualización: Una vez que se obtienen nuevas mediciones, el algoritmo las utiliza para corregir la predicción anterior y mejorar la estimación del
#     estado del sistema. Esto se logra mediante un proceso de fusión de información que tiene en cuenta tanto la predicción del modelo de proceso como 
#     las mediciones reales.
# 5.- Iteración: El algoritmo itera entre los pasos de predicción y actualización en cada paso de tiempo, continuamente refinando la estimación del 
#     estado del sistema a medida que llegan nuevas mediciones.
#--------------- PROGRAMA --------------------------------------
import numpy as np

class KalmanFilter:
    def __init__(self, initial_state_mean, initial_state_covariance, process_noise_covariance, measurement_noise_covariance):
        self.state_mean = initial_state_mean
        self.state_covariance = initial_state_covariance
        self.process_noise_covariance = process_noise_covariance
        self.measurement_noise_covariance = measurement_noise_covariance

    def predict(self, control_input=None):
        # Predict state mean using the process model
        self.state_mean = np.dot(self.process_model, self.state_mean)
        # Predict state covariance
        self.state_covariance = np.dot(np.dot(self.process_model, self.state_covariance), self.process_model.T) + self.process_noise_covariance

    def update(self, measurement):
        # Calculate Kalman gain
        kalman_gain = np.dot(np.dot(self.state_covariance, self.measurement_model.T), np.linalg.inv(np.dot(np.dot(self.measurement_model, self.state_covariance), self.measurement_model.T) + self.measurement_noise_covariance))
        # Update state mean
        self.state_mean = self.state_mean + np.dot(kalman_gain, (measurement - np.dot(self.measurement_model, self.state_mean)))
        # Update state covariance
        self.state_covariance = self.state_covariance - np.dot(np.dot(kalman_gain, self.measurement_model), self.state_covariance)

# Example usage
# Define initial state mean and covariance
initial_state_mean = np.array([0., 0.])
initial_state_covariance = np.array([[1., 0.], [0., 1.]])
# Define process noise covariance and measurement noise covariance
process_noise_covariance = np.array([[0.1, 0.], [0., 0.1]])
measurement_noise_covariance = np.array([[0.1, 0.], [0., 0.1]])
# Create Kalman filter object
kalman_filter = KalmanFilter(initial_state_mean, initial_state_covariance, process_noise_covariance, measurement_noise_covariance)
# Define process model and measurement model
kalman_filter.process_model = np.array([[1., 1.], [0., 1.]])
kalman_filter.measurement_model = np.array([[1., 0.]])
# Perform prediction step
kalman_filter.predict()
# Perform update step with a measurement
measurement = np.array([1.5])
kalman_filter.update(measurement)
# Print estimated state mean and covariance
print("Estimated state mean:", kalman_filter.state_mean)
print("Estimated state covariance:", kalman_filter.state_covariance)

#------------------------------------------------------------------------
# 1.- Importamos la biblioteca numpy para manipulación numérica eficiente.
# 2.- Definimos una clase KalmanFilter que representa un filtro de Kalman. En el inicializador (__init__), 
#     inicializamos los parámetros del filtro: la media inicial del estado, la covarianza inicial del estado, la covarianza 
#     del ruido del proceso y la covarianza del ruido de la medición.
# 3.- La función predict predice el siguiente estado del sistema utilizando el modelo de proceso.
# 4.- La función update actualiza la estimación del estado utilizando una nueva medición.
# 5.- Creamos una instancia del filtro de Kalman con los parámetros iniciales.
# 6.- Definimos el modelo de proceso y el modelo de medición.
# 7.- Realizamos una predicción inicial.
# 8.- Actualizamos la estimación del estado con una nueva medición.
# 9.- Imprimimos la media estimada del estado y la covarianza estimada del estado después de la actualización.