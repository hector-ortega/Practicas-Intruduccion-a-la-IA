#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.
#-----------------TEORIA----------------------------------------
# La Localización Monte Carlo es útil cuando el robot no tiene información precisa sobre su posición exacta en un entorno desconocido.
# En lugar de depender de modelos matemáticos complejos del entorno, MCL estima la posición del robot utilizando una técnica probabilística que
#se basa en muestras aleatorias y mediciones sensoriales.

# Funcionamiento:
# 1.- Inicialización de muestras: Se generan inicialmente un conjunto de muestras aleatorias que representan posibles ubicaciones del robot en el entorno.
# 2.- Simulación de movimiento: Se simula el movimiento del robot. En algunos casos, el robot puede no moverse físicamente, pero se puede simular 
#     n movimiento para tener en cuenta la incertidumbre en la posición actual.
# 3.- Simulación del sensor: Se realizan mediciones sensoriales desde la posición estimada del robot y se comparan con las mediciones reales del entorno.
#     Estas mediciones se utilizan para calcular la probabilidad de que el robot se encuentre en cada una de las posibles ubicaciones representadas por las muestras.
# 4.- Actualización de las muestras: Se actualizan las muestras basadas en las mediciones del sensor y las probabilidades calculadas. Las muestras con 
#     una alta probabilidad de coincidencia con las mediciones del sensor se mantienen, mientras que las muestras con baja probabilidad se descartan. 
#     Esto se puede hacer mediante técnicas de resampling (muestreo con reemplazo), donde las muestras se seleccionan nuevamente con una probabilidad
#     proporcional a su peso.
# 5.- Iteración: Los pasos 2 a 4 se repiten varias veces para mejorar la precisión de la estimación de la posición del robot.
# 6.- Estimación final de la posición: Después de un número de iteraciones, se obtiene una distribución de probabilidad sobre las posibles 
#     ubicaciones del robot. La ubicación final estimada del robot se puede determinar mediante diferentes métodos, como el cálculo de la media
#     ponderada de las muestras restantes.
#--------------- PROGRAMA --------------------------------------
import numpy as np

# Definición de la función de simulación del sensor
def simular_sensor(ubicacion_robot, ubicaciones_referencia):
    # Simulación de la medida del sensor basada en la distancia euclidiana
    distancias = np.linalg.norm(ubicaciones_referencia - ubicacion_robot, axis=1)
    # Agregar ruido para simular mediciones sensoriales inciertas
    medidas = distancias + np.random.normal(0, 0.1, distancias.shape)
    return medidas

# Función para generar muestras aleatorias de ubicaciones del robot
def generar_muestras_aleatorias(espacio_estado, num_muestras):
    return np.random.choice(espacio_estado, size=(num_muestras, espacio_estado.shape[1]))

# Algoritmo de localización Monte Carlo
def localizacion_monte_carlo(num_muestras, num_iteraciones):
    # Definir el espacio de estado (posibles ubicaciones del robot)
    espacio_estado = np.array([[x, y] for x in range(10) for y in range(10)])
    
    # Inicialización uniforme de las muestras
    muestras = generar_muestras_aleatorias(espacio_estado, num_muestras)
    
    for _ in range(num_iteraciones):
        # Simulación de movimiento del robot (en este ejemplo, no se realiza movimiento)
        
        # Simulación del sensor para obtener medidas
        medidas = simular_sensor([5, 5], espacio_estado)
        
        # Calcular la probabilidad de cada muestra dada la medida del sensor
        probabilidades = np.exp(-0.5 * (medidas - simular_sensor(muestras, espacio_estado))**2)
        
        # Normalizar las probabilidades para obtener una distribución de probabilidad válida
        probabilidades /= np.sum(probabilidades)
        
        # Resampling (muestreo con reemplazo) basado en las probabilidades calculadas
        indices_muestras_seleccionadas = np.random.choice(np.arange(num_muestras), size=num_muestras, p=probabilidades)
        muestras = muestras[indices_muestras_seleccionadas]
        
    return muestras

# Ejemplo de uso del algoritmo de localización Monte Carlo
if __name__ == "__main__":
    # Parámetros del algoritmo
    num_muestras = 1000
    num_iteraciones = 10
    
    # Ejecutar el algoritmo
    ubicaciones_estimadas = localizacion_monte_carlo(num_muestras, num_iteraciones)
    
    # Imprimir las ubicaciones estimadas
    print("Ubicaciones estimadas del robot:")
    print(ubicaciones_estimadas)

#-------------------------------------------------------------------------------
# 1.- Se importa la biblioteca NumPy, que se utilizará para realizar cálculos numéricos eficientes.
# 2.- Se define una función simular_sensor que simula las mediciones del sensor del robot. En este ejemplo, se utiliza una medida basada en 
#     la distancia euclidiana con algo de ruido añadido para simular mediciones inciertas.
# 3.- Se define una función generar_muestras_aleatorias que genera un número específico de muestras aleatorias dentro del espacio de estado 
#     (posibles ubicaciones del robot).
# 4.- Se define la función principal localizacion_monte_carlo, que implementa el algoritmo de Localización Monte Carlo. Se inicializan las 
#     muestras de ubicación de manera uniforme, y luego se realizan iteraciones donde se simulan el movimiento del robot, las mediciones del sensor, 
#     se calculan las probabilidades de las muestras y se realiza el resampling (muestreo con reemplazo) basado en estas probabilidades.
# 5.- En el ejemplo principal, se especifican los parámetros del algoritmo (num_muestras y num_iteraciones) y se llama a la función localizacion_monte_carlo. 
#     Se imprimen las ubicaciones estimadas del robot después de la ejecución del algoritmo.