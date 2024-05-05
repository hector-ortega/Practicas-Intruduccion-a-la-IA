#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.
#-----------------TEORIA----------------------------------------

# La cinemática inversa es un concepto fundamental en robótica que se refiere al cálculo de las posiciones y 
# orientaciones de las articulaciones de un robot necesarias para lograr una posición y orientación específicas del extremo del efector, 
# como una herramienta o una pinza.

# En un sistema robótico, las articulaciones son las partes móviles del robot que permiten su movimiento. La cinemática inversa es esencial 
# para determinar cómo deben configurarse las articulaciones para alcanzar una posición y orientación deseadas del extremo del efector, lo que 
# permite al robot realizar tareas específicas de manera eficiente y precisa.

# El proceso de cinemática inversa implica encontrar las soluciones para las variables de articulación (como ángulos de rotación o longitudes de las articulaciones) 
# que satisfacen ciertas condiciones, como la posición y orientación del extremo del efector. Esto se logra utilizando principios geométricos y trigonométricos, 
# así como ecuaciones que describen la geometría del robot y sus articulaciones.

# El algoritmo de cinemática inversa toma las coordenadas del extremo del efector en el espacio (por ejemplo, coordenadas x, y, z en un sistema de coordenadas
#  tridimensional) como entrada y calcula los valores de las variables de articulación necesarias para lograr esa posición y orientación específicas. 
# Estos valores se utilizan luego para controlar los actuadores del robot y mover sus articulaciones a las posiciones deseadas.
#--------------- PROGRAMA --------------------------------------
import math

def calcular_cinemática_inversa(x, y):
    # Longitudes de los brazos del robot
    L1 = 1.0  # Longitud del primer brazo
    L2 = 1.0  # Longitud del segundo brazo
    
    # Calcular el ángulo theta2
    D = (x**2 + y**2 - L1**2 - L2**2) / (2 * L1 * L2)
    theta2 = math.atan2(-math.sqrt(1 - D**2), D)
    
    # Calcular el ángulo theta1
    theta1 = math.atan2(y, x) - math.atan2((L2 * math.sin(theta2)), (L1 + L2 * math.cos(theta2)))
    
    return theta1, theta2

# Coordenadas del punto final (efector final)
x = 0.5
y = 0.5

# Calcular los ángulos de las articulaciones usando cinemática inversa
theta1, theta2 = calcular_cinemática_inversa(x, y)

# Imprimir los resultados

print("Ángulo theta1:", math.degrees(theta1))
print("Ángulo theta2:", math.degrees(theta2))

#_-----------------------------------------------------------------------
# 1.- import math: Importa el módulo math de Python, que se utilizará para funciones matemáticas como atan2.
# 2.- def calcular_cinemática_inversa(x, y): Define una función llamada calcular_cinemática_inversa que toma las coordenadas 
#     x y y del punto final (efector final) como argumentos.
# 3.- L1 y L2: Definen las longitudes de los brazos del robot.
# 4.- Dentro de la función calcular_cinemática_inversa:
# 5.- Calculamos el ángulo theta2 utilizando la fórmula de cinemática inversa.
# 6.- Calculamos el ángulo theta1 utilizando la fórmula de cinemática inversa.
# 7.- Finalmente, la función devuelve los ángulos theta1 y theta2.
# 8.- x y y: Definen las coordenadas del punto final (efector final) del robot.
# 9.- Llamamos a la función calcular_cinemática_inversa con las coordenadas x y y.
# 10.- Imprimimos los ángulos theta1 y theta2