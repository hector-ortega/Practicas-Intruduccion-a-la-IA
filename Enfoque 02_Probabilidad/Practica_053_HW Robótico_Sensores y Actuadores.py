#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.
#-----------------TEORIA----------------------------------------
# Los algoritmos de "HW Robótico: Sensores y Actuadores" se utilizan en el campo de la robótica para controlar el 
# comportamiento de los robots físicos. Estos algoritmos son responsables de interactuar con el entorno del robot a través de sensores y actuadores.

# 1.- Sensores: Los sensores son dispositivos que permiten a un robot percibir su entorno. Estos pueden incluir sensores de proximidad, cámaras,
#     micrófonos, acelerómetros, entre otros. Los datos recopilados por los sensores se utilizan para que el robot tome decisiones informadas sobre su 
#     comportamiento y su interacción con el entorno.
# 2.- Actuadores: Los actuadores son dispositivos que permiten que el robot realice acciones físicas en su entorno. Estos pueden incluir motores, servomotores, 
#     pistones hidráulicos, entre otros. Los actuadores reciben señales de control del robot y realizan acciones específicas, como moverse, manipular objetos o
#     realizar tareas específicas.

# Los algoritmos de "HW Robótico: Sensores y Actuadores" se encargan de procesar la información de los sensores y generar comandos para los actuadores,
# lo que permite al robot interactuar de manera efectiva con su entorno. Estos algoritmos suelen involucrar técnicas de procesamiento de señales, fusión sensorial,
# planificación de movimientos y control de sistemas en tiempo real.
#--------------- PROGRAMA --------------------------------------
import numpy as np

class Robot:
    def __init__(self, x, y):
        self.x = x  # Posición x inicial del robot
        self.y = y  # Posición y inicial del robot

    def move(self, dx, dy):
        # Método para mover el robot en el espacio bidimensional
        self.x += dx
        self.y += dy

    def sense_obstacle(self, obstacle_x, obstacle_y, radius):
        # Método para simular el sensor del robot que detecta obstáculos
        distance = np.sqrt((self.x - obstacle_x) ** 2 + (self.y - obstacle_y) ** 2)
        if distance <= radius:
            return True  # Hay un obstáculo cerca
        else:
            return False  # No hay obstáculo cerca

# Creamos un objeto robot en la posición inicial (0, 0)
robot = Robot(0, 0)

# Definimos las posiciones del objetivo y del obstáculo
target_x, target_y = 5, 5
obstacle_x, obstacle_y = 2, 3
obstacle_radius = 1

# Simulamos el movimiento del robot hacia el objetivo evitando el obstáculo
while True:
    # Calculamos las diferencias en las coordenadas x e y hacia el objetivo
    dx = target_x - robot.x
    dy = target_y - robot.y
    
    # Verificamos si hay un obstáculo cerca antes de mover el robot
    if robot.sense_obstacle(obstacle_x, obstacle_y, obstacle_radius):
        print("¡Cuidado! Hay un obstáculo cerca.")
        # Aquí podríamos implementar una estrategia para evitar el obstáculo, como cambiar de dirección
        
    # Movemos el robot hacia el objetivo
    robot.move(dx, dy)
    
    # Imprimimos la nueva posición del robot
    print(f"Posición actual del robot: ({robot.x}, {robot.y})")
    
    # Verificamos si el robot ha alcanzado el objetivo
    if robot.x == target_x and robot.y == target_y:
        print("¡El robot ha llegado al objetivo!")
        break  # Salimos del bucle

#-------------------------------------------------------------------------
# 1.- Creamos una clase Robot que representa al robot. El método __init__ inicializa la posición del robot, 
#     y los métodos move y sense_obstacle simulan el movimiento del robot y la detección de obstáculos, respectivamente.
# 2.- Creamos una instancia de la clase Robot con posición inicial en (0, 0).
# 3.- Definimos las posiciones del objetivo y del obstáculo, así como el radio del obstáculo.
# 4.- Dentro de un bucle infinito, calculamos las diferencias en las coordenadas x e y hacia el objetivo.
# 5.- Verificamos si hay un obstáculo cerca utilizando el método sense_obstacle.
# 6.- Movemos el robot hacia el objetivo utilizando el método move.
# 7.- Imprimimos la nueva posición del robot en cada iteración.
# 8.- Verificamos si el robot ha alcanzado el objetivo y, de ser así, salimos del bucle.