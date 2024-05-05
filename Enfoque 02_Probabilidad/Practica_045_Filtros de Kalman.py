#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.
#-----------------TEORIA----------------------------------------

# Los filtros de Kalman son algoritmos de estimación que se utilizan para estimar el estado de un sistema dinámico a partir de una secuencia 
# de observaciones ruidosas. Son ampliamente utilizados en una variedad de aplicaciones, incluyendo el seguimiento de objetos en movimiento, 
# la navegación, el control automático, la visión por computadora, entre otros.

# El filtro de Kalman funciona de la siguiente manera:

# 1.- Predicción del estado: El filtro de Kalman predice el estado futuro del sistema utilizando el estado actual y el modelo de transición del sistema.
#     Esto se hace multiplicando el estado actual por la matriz de transición del sistema.
# 2.- Predicción de la covarianza del error: Junto con la predicción del estado, el filtro de Kalman también predice la covarianza del error del estado futuro.
#     Esto se hace multiplicando la covarianza actual por la matriz de transición del sistema, y luego agregando la covarianza del ruido del proceso.
# 3.- Actualización del estado estimado: Cuando se recibe una nueva observación, el filtro de Kalman actualiza el estado estimado utilizando una combinación
#     de la observación actual y la predicción del estado. Esta actualización se realiza mediante la ganancia de Kalman, que se calcula utilizando la
#     covarianza del estado y la covarianza del error de la medición.
# 4.- Actualización de la covarianza del error: Después de actualizar el estado estimado, el filtro de Kalman también actualiza la covarianza del error
#     del estado. Esto se hace mediante la ganancia de Kalman y la covarianza de la observación.
 
#--------------- PROGRAMA --------------------------------------
import numpy as np

class KalmanFilter:
    def __init__(self, initial_state, initial_covariance, transition_matrix, observation_matrix, process_noise_covariance, measurement_noise_covariance):
        """
        Inicializa el filtro de Kalman con los parámetros iniciales.
        
        Args:
            initial_state (numpy.array): Estado inicial estimado.
            initial_covariance (numpy.array): Covarianza inicial del estado estimado.
            transition_matrix (numpy.array): Matriz de transición de estado.
            observation_matrix (numpy.array): Matriz de observación.
            process_noise_covariance (numpy.array): Covarianza del ruido del proceso.
            measurement_noise_covariance (numpy.array): Covarianza del ruido de la medición.
        """
        self.state = initial_state
        self.covariance = initial_covariance
        self.transition_matrix = transition_matrix
        self.observation_matrix = observation_matrix
        self.process_noise_covariance = process_noise_covariance
        self.measurement_noise_covariance = measurement_noise_covariance

    def predict(self):
        """
        Predice el siguiente estado del sistema.
        """
        # Predicción del estado
        self.state = np.dot(self.transition_matrix, self.state)
        # Predicción de la covarianza del error
        self.covariance = np.dot(np.dot(self.transition_matrix, self.covariance), self.transition_matrix.T) + self.process_noise_covariance

    def update(self, measurement):
        """
        Actualiza el estado estimado basado en la medición.
        
        Args:
            measurement (numpy.array): Medición actual.
        """
        # Innovación
        innovation = measurement - np.dot(self.observation_matrix, self.state)
        # Residual de la covarianza
        residual_covariance = np.dot(np.dot(self.observation_matrix, self.covariance), self.observation_matrix.T) + self.measurement_noise_covariance
        # Ganancia de Kalman
        kalman_gain = np.dot(np.dot(self.covariance, self.observation_matrix.T), np.linalg.inv(residual_covariance))
        # Actualización del estado estimado
        self.state += np.dot(kalman_gain, innovation)
        # Actualización de la covarianza del error
        self.covariance -= np.dot(np.dot(kalman_gain, self.observation_matrix), self.covariance)

# Ejemplo de uso
# Definición de los parámetros del filtro de Kalman
initial_state = np.array([0, 0])  # Estado inicial estimado
initial_covariance = np.eye(2)    # Covarianza inicial del estado estimado
transition_matrix = np.array([[1, 1], [0, 1]])  # Matriz de transición de estado
observation_matrix = np.eye(2)    # Matriz de observación
process_noise_covariance = np.eye(2) * 0.01  # Covarianza del ruido del proceso
measurement_noise_covariance = np.eye(2) * 0.1  # Covarianza del ruido de la medición

# Creación del filtro de Kalman
kf = KalmanFilter(initial_state, initial_covariance, transition_matrix, observation_matrix, process_noise_covariance, measurement_noise_covariance)

# Ejemplo de predicción y actualización
kf.predict()
measurement = np.array([1, 1])  # Medición
kf.update(measurement)

# Imprimir el estado estimado después de la actualización
print("Estado estimado después de la actualización:", kf.state)

#------------------------------------------------------------------------

# 1.- Se define una clase KalmanFilter que representa el filtro de Kalman. Los parámetros iniciales del filtro, como el 
#     estado inicial estimado, la covarianza inicial del estado estimado, las matrices de transición y observación, y las 
#     covarianzas del ruido del proceso y de la medición, se pasan al constructor de la clase.
# 2.- El método predict() realiza la predicción del siguiente estado del sistema utilizando las ecuaciones de predicción del filtro de Kalman.
# 3.- El método update() actualiza el estado estimado basado en la medición actual utilizando las ecuaciones de actualización del filtro de Kalman.
# 4.- En el ejemplo de uso, se crean instancias del filtro de Kalman con parámetros específicos y se realiza una predicción seguida de una 
#     actualización utilizando una medición simulada.
# 5.- Finalmente, se imprime el estado estimado después de la actualización para verificar el funcionamiento del filtro de Kalman.