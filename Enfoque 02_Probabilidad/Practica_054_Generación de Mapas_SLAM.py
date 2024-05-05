#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.
#-----------------TEORIA----------------------------------------
# SLAM (Simultaneous Localization and Mapping) es un problema fundamental en robótica que consiste en que un robot, al moverse en un entorno desconocido,
# debe crear un mapa de dicho entorno al mismo tiempo que localiza su propia posición en ese mapa. Este proceso implica fusionar datos de sensores
# (como lidar, cámaras, odómetros, etc.) para estimar la posición del robot y la distribución de los obstáculos en el entorno.
#--------------- PROGRAMA --------------------------------------
import numpy as np
import matplotlib.pyplot as plt

# Definir funciones para la propagación del estado y la observación
def motion_model(x, u):
    # Modelo de movimiento simple: el robot se mueve en línea recta con velocidad constante
    return x + u

def observation_model(x, m):
    # Modelo de observación simple: la observación es la distancia entre el robot y un punto de referencia fijo
    return np.linalg.norm(x - m)

# Inicializar el entorno y la posición del robot
landmarks = np.array([[5, 5], [10, 5], [15, 10]])  # Posiciones conocidas de puntos de referencia
robot_position = np.array([0, 0])  # Posición inicial del robot
num_landmarks = landmarks.shape[0]

# Definir el movimiento del robot
num_steps = 20
motion_cmd = np.array([1, 0])  # Movimiento hacia adelante
motion_noise = 0.1

# Ejecutar el algoritmo SLAM
for t in range(num_steps):
    # Generar observaciones simuladas
    observations = []
    for i in range(num_landmarks):
        true_distance = observation_model(robot_position, landmarks[i])
        measured_distance = true_distance + np.random.normal(0, 0.1)  # Agregar ruido a las observaciones
        observations.append(measured_distance)
    
    # Actualizar el estado del robot utilizando las observaciones
    # Aquí, omitimos el proceso de actualización del filtro de Kalman completo y simplemente actualizamos la posición del robot directamente
    for i in range(num_landmarks):
        landmark_position = landmarks[i]
        # Realizar una estimación de la posición del robot utilizando la observación actual y la posición conocida del punto de referencia
        estimated_distance = observation_model(robot_position, landmark_position)
        error = estimated_distance - observations[i]
        # Actualizar la posición del robot usando el gradiente descendente simple
        robot_position -= 0.1 * error * (robot_position - landmark_position) / np.linalg.norm(robot_position - landmark_position)
    
    # Mover el robot
    motion_cmd_with_noise = motion_cmd + np.random.normal(0, motion_noise, size=motion_cmd.shape)
    robot_position = motion_model(robot_position, motion_cmd_with_noise)
    
# Visualizar el resultado
plt.figure(figsize=(8, 6))
plt.plot(landmarks[:, 0], landmarks[:, 1], 'ko', markersize=10, label='Landmarks')
plt.plot(robot_position[0], robot_position[1], 'ro', markersize=10, label='Robot Position')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('SLAM: Mapa Generado')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()