#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.
#-----------------TEORIA----------------------------------------
# El campo de la dinámica y el control en la robótica se centra en el estudio del movimiento y la interacción de los sistemas robóticos con su entorno,
# así como en el diseño de algoritmos y controladores para regular y supervisar este movimiento. Aquí hay una explicación más detallada sobre la teoría
# y aplicación de estos conceptos:

# Dinámica en Robótica:
# La dinámica en robótica se refiere al estudio del movimiento y la interacción de los robots con su entorno. Incluye el análisis de las fuerzas y momentos 
# que afectan el movimiento del robot, así como la cinemática y la cinética de los sistemas mecánicos. La dinámica también considera factores como la masa,
# la inercia, la fricción y la gravedad para predecir el comportamiento del robot bajo diferentes condiciones.

# En la dinámica de robots, se utilizan modelos matemáticos para describir el movimiento y la interacción del robot con su entorno.
# Estos modelos pueden ser simples o complejos, dependiendo de la aplicación y la precisión requerida. Los modelos dinámicos son fundamentales 
# para el diseño y control de robots, ya que proporcionan información sobre cómo el robot responderá a las entradas del controlador y las condiciones del entorno.

# Control en Robótica:
# El control en robótica se refiere al diseño y la implementación de algoritmos y sistemas que regulan y supervisan el comportamiento y el 
# movimiento del robot. El objetivo del control es lograr que el robot alcance ciertos objetivos o siga trayectorias específicas, mientras 
# se minimiza el error y se mantienen las restricciones del sistema.

# Existen diferentes enfoques de control en robótica, entre ellos:

# 1.- Control Clásico: Utiliza técnicas como el control proporcional-integral-derivativo (PID) y el control de retroalimentación lineal para regular el movimiento del robot.
# 2.- Control Basado en Modelos: Emplea modelos matemáticos del robot y su entorno para predecir y controlar su comportamiento.
# 3.- Control Robusto: Diseña controladores que pueden manejar perturbaciones y variaciones en el entorno de manera efectiva.
# 4.- Control de Trayectorias: Planifica y sigue trayectorias específicas en el espacio de configuración del robot.

#--------------- PROGRAMA --------------------------------------
class PIDController:
    def __init__(self, kp, ki, kd, target):
        self.kp = kp  # Ganancia proporcional
        self.ki = ki  # Ganancia integral
        self.kd = kd  # Ganancia derivativa
        self.target = target  # Valor objetivo
        self.prev_error = 0  # Error previo
        self.integral = 0  # Término integral acumulado

    def update(self, current):
        # Calcular el error proporcional
        error = self.target - current
        
        # Calcular el término integral
        self.integral += error
        
        # Calcular el término derivativo
        derivative = error - self.prev_error
        
        # Calcular la salida del controlador
        output = self.kp * error + self.ki * self.integral + self.kd * derivative
        
        # Actualizar el error previo
        self.prev_error = error
        
        return output


# Ejemplo de uso del controlador PID
if __name__ == "__main__":
    # Definir parámetros del controlador
    kp = 0.5
    ki = 0.1
    kd = 0.2
    target = 10
    
    # Crear instancia del controlador PID
    pid_controller = PIDController(kp, ki, kd, target)
    
    # Simular el proceso de control
    current_value = 0
    for _ in range(20):
        # Calcular la salida del controlador
        control_output = pid_controller.update(current_value)
        
        # Simular el proceso físico (por ejemplo, un motor)
        current_value += control_output
        
        # Imprimir valores para mostrar el funcionamiento del controlador
        print("Current Value:", current_value)

#-----------------------------------------------------------------------------------
# 1.- La clase PIDController tiene un constructor __init__ que toma las ganancias del controlador (kp, ki, kd) y el valor objetivo.
# 2.- El método update calcula la salida del controlador PID en función del error actual, el error acumulado (integral) y el cambio en el error (derivada).
# 3.- La parte principal del programa crea una instancia del controlador PID, define los parámetros y simula el proceso de control durante 20 iteraciones.
# 4.- En cada iteración, se actualiza el controlador PID con la salida del controlador y se simula el proceso físico (por ejemplo, el movimiento de un motor).
# 5.- Se imprimen los valores actuales en cada iteración para demostrar el funcionamiento del controlador.