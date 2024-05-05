#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.
#-----------------TEORIA----------------------------------------

# Los algoritmos de movimiento son utilizados en inteligencia artificial para simular y modelar el desplazamiento de objetos en un entorno,
# ya sea en un espacio bidimensional o tridimensional. Estos algoritmos son fundamentales en diversas áreas, como la animación por computadora,
# la robótica, los videojuegos, la simulación de fenómenos físicos y muchas otras aplicaciones.

# La idea básica detrás de un algoritmo de movimiento es calcular la posición de un objeto en cada paso de tiempo, basándose en su posición inicial,
# velocidad y aceleración. Dependiendo del contexto y de los requisitos específicos de la aplicación, existen diferentes enfoques para modelar el 
# movimiento de los objetos. Algunos de los conceptos clave en estos algoritmos son:

# Posición: La ubicación actual del objeto en el espacio, representada típicamente por coordenadas cartesianas (x, y, z) en un sistema de coordenadas.

# Velocidad: La tasa de cambio de la posición del objeto en el tiempo. La velocidad puede ser constante o cambiar con el tiempo, dependiendo de factores 
# como la aceleración y la resistencia del medio.

# Aceleración: La tasa de cambio de la velocidad del objeto en el tiempo. La aceleración puede ser positiva (aumentando la velocidad), 
# negativa (disminuyendo la velocidad) o cero (movimiento uniforme).
#--------------- PROGRAMA --------------------------------------

import numpy as np
import matplotlib.pyplot as plt

def simulate_motion(position, velocity, acceleration, num_steps):
    """Simula el movimiento de un objeto en un plano bidimensional."""
    positions = [position]  # Lista para almacenar las posiciones en cada paso de tiempo
    
    # Iterar sobre cada paso de tiempo
    for _ in range(num_steps):
        velocity += acceleration  # Actualizar la velocidad con la aceleración
        position += velocity      # Actualizar la posición con la velocidad
        positions.append(position)  # Agregar la nueva posición a la lista
    
    return positions

# Definir los parámetros del movimiento
initial_position = np.array([0, 0])    # Posición inicial (x, y)
initial_velocity = np.array([2, 3])    # Velocidad inicial en dirección (x, y)
constant_acceleration = np.array([0.1, -0.05])  # Aceleración constante en dirección (x, y)
num_steps = 50  # Número de pasos de tiempo

# Simular el movimiento
trajectory = simulate_motion(initial_position, initial_velocity, constant_acceleration, num_steps)

# Extraer las coordenadas x e y de la trayectoria
x_coords = [point[0] for point in trajectory]
y_coords = [point[1] for point in trajectory]

# Visualizar la trayectoria
plt.figure(figsize=(8, 6))
plt.plot(x_coords, y_coords, marker='o', linestyle='-')
plt.title('Simulación de Movimiento')
plt.xlabel('Posición en x')
plt.ylabel('Posición en y')
plt.grid(True)
plt.show()

#--------------------------------------------------------------------------------

# 1.- Importamos las bibliotecas necesarias: numpy para operaciones numéricas y matplotlib para visualización.
# 2.- Definimos la función simulate_motion que simula el movimiento de un objeto. Recibe la posición inicial, la velocidad inicial, 
#     la aceleración constante y el número de pasos de tiempo como entrada. Devuelve una lista de posiciones en cada paso de tiempo.
# 3.- Inicializamos los parámetros del movimiento, como la posición inicial, la velocidad inicial y la aceleración constante.
# 4.- Llamamos a la función simulate_motion para simular el movimiento y almacenar la trayectoria resultante.
# 5.- Extraemos las coordenadas x e y de la trayectoria para la visualización.
# 6.- Visualizamos la trayectoria utilizando matplotlib.