#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# El algoritmo de Proceso de Decisión de Markov (MDP) es una herramienta fundamental en la teoría de la decisión y la inteligencia artificial 
# para modelar y resolver problemas de toma de decisiones secuenciales en entornos estocásticos. Un MDP es un modelo matemático que describe un 
# sistema donde un agente toma decisiones en una serie de estados, donde las acciones tomadas por el agente afectan el estado del sistema y generan recompensas. 
# El objetivo del agente es encontrar la política óptima, es decir, la secuencia de acciones que maximiza la recompensa esperada a largo plazo.

# El algoritmo de Proceso de Decisión de Markov aborda este problema al calcular la política óptima, que es una estrategia que determina qué acción 
# debe tomar el agente en cada estado para maximizar la recompensa esperada. Este algoritmo se basa en la idea de la programación dinámica y utiliza 
# la ecuación de Bellman para calcular el valor esperado de cada estado y acción, iterativamente actualizando la política hasta que converge a la solución óptima.
#--------------- PROGRAMA ------------------------------------ 
# Importamos la librería numpy para cálculos numéricos
import numpy as np

# Definimos los estados (E) y acciones (A)
estados = ['A', 'B', 'C'] #Contiene los estados posibles (A, B, C) en los que se encuentra el agente.
acciones = ['Izquierda', 'Derecha'] # Contiene las acciones disponibles (Izquierda, Derecha) que el agente puede tomar en cada estado.

# Creamos un diccionario llamado recompensas que asigna una recompensa a cada par estado-acción. Por ejemplo:
# Desde el estado A, si vamos a la izquierda, la recompensa es -1.
# Desde el estado A, si vamos a la derecha, la recompensa es 1.
# Y así sucesivamente para los otros estados y acciones.
recompensas = {
    ('A', 'Izquierda'): -1,
    ('A', 'Derecha'): 1,
    ('B', 'Izquierda'): 2,
    ('B', 'Derecha'): -2,
    ('C', 'Izquierda'): 0,
    ('C', 'Derecha'): 0
}

# Creamos otro diccionario llamado transiciones que describe las probabilidades de pasar de un estado al siguiente después de ejecutar una acción. Por ejemplo:
# Desde A, si vamos a la izquierda, hay un 80% de probabilidad de permanecer en A y un 20% de ir a B.
# Desde A, si vamos a la derecha, hay un 20% de probabilidad de permanecer en A y un 80% de ir a B.
# Y así sucesivamente para los otros estados y acciones.
transiciones = {
    ('A', 'Izquierda'): {'A': 0.8, 'B': 0.2},
    ('A', 'Derecha'): {'A': 0.2, 'B': 0.8},
    ('B', 'Izquierda'): {'A': 0.1, 'B': 0.9},
    ('B', 'Derecha'): {'B': 1.0},
    ('C', 'Izquierda'): {'A': 0.3, 'C': 0.7},
    ('C', 'Derecha'): {'C': 1.0}
}

# Establecemos el factor de descuento (γ) en 0.9. Este valor pondera las recompensas futuras en la función de valor.
gamma = 0.9

# Creamos un diccionario llamado V que representa la función de valor. Inicializamos todos los valores en 0 para cada estado.
V = {estado: 0 for estado in estados}

# Realizamos 100 iteraciones para encontrar la función de valor óptima utilizando la ecuación de Bellman. Aquí está el proceso:
# Para cada estado, calculamos el valor para cada acción posible.
# Sumamos la recompensa actual y el valor futuro ponderado pora
for _ in range(100):
    V_nuevo = {}
    for estado in estados:
        valores = []
        for accion in acciones:
            valor_accion = recompensas.get((estado, accion), 0)
            for estado_siguiente, probabilidad in transiciones.get((estado, accion), {}).items():
                valor_accion += gamma * probabilidad * V[estado_siguiente]
            valores.append(valor_accion)
        V_nuevo[estado] = max(valores)
    V = V_nuevo

# Imprimimos la función de valor óptima
print("Función de valor óptima:")
for estado, valor in V.items():
    print(f"{estado}: {valor:.2f}")