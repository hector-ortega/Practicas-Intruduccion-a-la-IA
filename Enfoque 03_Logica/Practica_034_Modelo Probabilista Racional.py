#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# El Modelo Probabilista Racional (MPR) es un marco teórico utilizado en inteligencia artificial y toma de decisiones para modelar el comportamiento 
# humano en situaciones donde la incertidumbre es un factor importante. Este modelo se basa en la teoría de la probabilidad y la toma de decisiones
# bajo incertidumbre para determinar la acción más óptima en una determinada situación.

# Funcionamiento del Modelo Probabilista Racional:
 
# 1.- Estimación de Probabilidades:
# - En primer lugar, se estiman las probabilidades de los posibles resultados de las acciones. Esto puede implicar el uso de datos históricos,
#   expertos humanos o modelos estadísticos para calcular las probabilidades de los diferentes resultados.

# 2.- Evaluación de Utilidades:
# - Se evalúan las utilidades o valores asociados con los diferentes resultados posibles. Esto implica asignar valores a los resultados en función
#   de su importancia o preferencia en la toma de decisiones.

# 3.- Cálculo de la Decisión Óptima:
# - Utilizando las probabilidades estimadas y las utilidades asociadas, se calcula la acción óptima que maximiza la utilidad esperada o minimiza
#   el riesgo esperado. Esto se hace utilizando técnicas de optimización basadas en la teoría de la decisión.

# 4.- Actualización de las Decisiones:
# - A medida que se obtiene nueva información o cambian las circunstancias, se actualizan las estimaciones de probabilidad y las evaluaciones de utilidad, 
#   lo que puede llevar a cambios en las decisiones tomadas.
#--------------- PROGRAMA ------------------------------------
import random

def modelo_probabilista_racional(probabilidad_lluvia):
    # Si la probabilidad de lluvia es alta, llevar un paraguas con alta probabilidad
    if probabilidad_lluvia > 0.5:
        decision = 'Llevar un paraguas'
    # Si la probabilidad de lluvia es baja, no llevar un paraguas con alta probabilidad
    else:
        decision = 'No llevar un paraguas'
    return decision

def simular_condiciones_meteorologicas():
    # Simular la probabilidad de lluvia (entre 0 y 1)
    probabilidad_lluvia = random.random()
    return probabilidad_lluvia

def main():
    # Simular las condiciones meteorológicas
    probabilidad_lluvia = simular_condiciones_meteorologicas()
    print("Probabilidad de lluvia:", probabilidad_lluvia)

    # Tomar una decisión utilizando el Modelo Probabilista Racional
    decision = modelo_probabilista_racional(probabilidad_lluvia)
    print("Decisión:", decision)

if __name__ == "__main__":
    main()

#-----------------------------------------------------------------------

# 1.- Definimos una función modelo_probabilista_racional(probabilidad_lluvia) que toma como entrada la probabilidad de lluvia y decide 
#     si llevar un paraguas o no. Si la probabilidad es mayor que 0.5, se decide llevar un paraguas, de lo contrario, no llevarlo.
# 2.- Creamos una función simular_condiciones_meteorologicas() que simula la probabilidad de lluvia. Utilizamos la función random.random()
#     de la biblioteca random para generar un número aleatorio entre 0 y 1 que representa la probabilidad de lluvia.
# 3.- En la función main(), simulamos las condiciones meteorológicas y luego tomamos una decisión utilizando el Modelo Probabilista Racional.
# 4.- Ejecutamos el programa principal dentro de la condición if __name__ == "__main__": para asegurarnos de que se ejecute solo cuando el script 
#     se ejecuta directamente y no cuando se importa como un módulo.