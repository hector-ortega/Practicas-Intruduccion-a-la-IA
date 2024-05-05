#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.
#-----------------TEORIA----------------------------------------
# El software robótico (SW) es esencial para controlar y coordinar las acciones de los robots. Este tipo de software se utiliza para una variedad de 
# propósitos en la robótica, que van desde el control de movimiento hasta la planificación de tareas complejas. Aquí hay una descripción general de 
# cómo funciona y para qué se utiliza:

# Funciones y aplicaciones del software robótico:
# 1.- Control de movimiento: El software robótico se utiliza para controlar el movimiento de los robots, ya sea en un entorno físico o simulado. Esto 
#     implica convertir comandos de alto nivel (como "moverse hacia adelante") en señales de control que los motores del robot pueden entender.
# 2.- Percepción del entorno: Los algoritmos de percepción permiten a los robots interpretar la información de sus sensores 
#     (como cámaras, sensores de distancia, etc.) para comprender su entorno. Esto incluye la detección de objetos, la identificación de obstáculos 
#     y la estimación de la posición relativa de los objetos.
# 3.- Planificación de trayectorias: Los robots deben ser capaces de planificar rutas seguras y eficientes para alcanzar sus objetivos. El software 
#     robótico incluye algoritmos de planificación de trayectorias que tienen en cuenta las restricciones del entorno, como obstáculos y limitaciones de movimiento.
# 4.- Interacción con el entorno: Los robots a menudo necesitan interactuar físicamente con su entorno, ya sea para recoger objetos, manipular herramientas 
#     o realizar tareas específicas. El software robótico controla estos movimientos y acciones para lograr los objetivos deseados.
# 5.- Aprendizaje y adaptación: Algunos sistemas robóticos utilizan técnicas de aprendizaje automático y adaptación para mejorar su rendimiento con el tiempo. 
#     Esto puede implicar el ajuste de parámetros de control, la mejora de modelos de percepción o la optimización de estrategias de planificación.
#--------------- PROGRAMA --------------------------------------
class Robot:
    def __init__(self):
        self.x = 0  # Posición inicial en el eje x
        self.y = 0  # Posición inicial en el eje y

    def move_forward(self, distance):
        self.y += distance  # Mover hacia adelante en el eje y

    def move_backward(self, distance):
        self.y -= distance  # Mover hacia atrás en el eje y

    def move_left(self, distance):
        self.x -= distance  # Mover hacia la izquierda en el eje x

    def move_right(self, distance):
        self.x += distance  # Mover hacia la derecha en el eje x

# Función para imprimir la posición actual del robot
def print_robot_position(robot):
    print(f"Posición actual del robot: ({robot.x}, {robot.y})")

# Crear una instancia del robot
robot = Robot()

# Movimientos del robot
robot.move_forward(5)
robot.move_left(3)
robot.move_backward(2)
robot.move_right(4)

# Imprimir la posición final del robot
print_robot_position(robot)

#-----------------------------------------------------------------------------
# 1.- Definimos una clase Robot que representa al robot. Tiene métodos para mover el robot hacia adelante, hacia atrás, hacia la izquierda y hacia la derecha,
#     así como atributos para almacenar la posición del robot en los ejes x e y.
# 2.- Creamos una función print_robot_position que imprime la posición actual del robot.
# 3.- Creamos una instancia de la clase Robot llamada robot.
# 4.- Llamamos a los métodos de movimiento del robot para simular su movimiento en diferentes direcciones.
# 5.- Finalmente, imprimimos la posición final del robot llamando a la función print_robot_position.
