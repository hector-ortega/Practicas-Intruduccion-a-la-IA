#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# Claro, un algoritmo de incertidumbre se utiliza para abordar situaciones en las que no se tiene información completa
# o exacta sobre un sistema o fenómeno. En muchos casos, especialmente en el mundo real, la información disponible es limitada, 
# incompleta o puede estar sujeta a variabilidad. Los algoritmos de incertidumbre se utilizan para modelar y tomar decisiones en
# tales situaciones, teniendo en cuenta la incertidumbre asociada.

# Un ejemplo clásico de incertidumbre se encuentra en el campo de la inteligencia artificial, específicamente en el área de la 
# probabilidad y la estadística. En situaciones donde hay datos incompletos o ruidosos, los algoritmos de incertidumbre pueden ayudar a
# hacer predicciones más robustas y tomar decisiones más informadas.
#--------------- PROGRAMA ------------------------------------
import random

# Función para simular el lanzamiento de un dado cargado
def lanzamiento_dado_cargado(probabilidad_cargado):
    if random.random() < probabilidad_cargado:
        return random.randint(1, 6)  # Dado cargado, retorna un número entre 1 y 6
    else:
        return random.randint(1, 6)  # Dado justo, retorna un número entre 1 y 6

# Función para realizar la actualización de la probabilidad usando Inferencia Bayesiana
def actualizar_probabilidad(probabilidad_previa, resultado_lanzamiento, hipotesis_cargado, probabilidad_cargado, probabilidad_justo):
    if resultado_lanzamiento == hipotesis_cargado:
        # Si el resultado del lanzamiento coincide con la hipótesis de que el dado está cargado,
        # actualizamos la probabilidad multiplicando por la probabilidad de que el dado esté cargado y dividiendo
        # por la probabilidad total de obtener ese resultado.
        return (probabilidad_previa * probabilidad_cargado) / ((probabilidad_previa * probabilidad_cargado) + ((1 - probabilidad_previa) * probabilidad_justo))
    else:
        # Si el resultado del lanzamiento no coincide con la hipótesis de que el dado está cargado,
        # actualizamos la probabilidad multiplicando por la probabilidad de que el dado esté justo y dividiendo
        # por la probabilidad total de obtener ese resultado.
        return (probabilidad_previa * (1 - probabilidad_cargado)) / ((probabilidad_previa * (1 - probabilidad_cargado)) + ((1 - probabilidad_previa) * probabilidad_justo))

# Probabilidad inicial de que el dado esté cargado
probabilidad_cargado = 0.5
# Probabilidad de obtener cualquier número en un dado justo
probabilidad_justo = 1 / 6

# Realizamos algunos lanzamientos del dado y actualizamos la probabilidad en cada iteración
for _ in range(10):
    # Simulamos un lanzamiento del dado
    resultado_lanzamiento = lanzamiento_dado_cargado(probabilidad_cargado)
    # Actualizamos la probabilidad basada en el resultado del lanzamiento
    probabilidad_cargado = actualizar_probabilidad(probabilidad_cargado, resultado_lanzamiento, 6, 0.7, probabilidad_justo)
    # Imprimimos la probabilidad actualizada
    print("Probabilidad de que el dado esté cargado:", probabilidad_cargado)

#----------------------------------------------------------------------------------------------
# 1.-import random: Importamos el módulo random de Python para generar números aleatorios.
# 2.-def lanzamiento_dado_cargado(probabilidad_cargado): Definimos una función llamada lanzamiento_dado_cargado que simula el lanzamiento 
# de un dado cargado. Recibe como argumento la probabilidad de que el dado esté cargado.
# 3.-def actualizar_probabilidad(probabilidad_previa, resultado_lanzamiento, hipotesis_cargado, probabilidad_cargado, probabilidad_justo): 
# Definimos una función llamada actualizar_probabilidad que realiza la actualización de la probabilidad utilizando el algoritmo de Inferencia 
# Bayesiana. Recibe como argumentos la probabilidad previa, el resultado del lanzamiento, la hipótesis de que el dado está cargado,
# la probabilidad de que el dado esté cargado y la probabilidad de obtener cualquier número en un dado justo.
# 4.-probabilidad_cargado = 0.5: Inicializamos la probabilidad de que el dado esté cargado en 0.5, lo que significa que tenemos una incertidumbre 
# igual sobre si el dado está cargado o no.
# 5.-probabilidad_justo = 1 / 6: Calculamos la probabilidad de obtener cualquier número en un dado justo. Como hay 6 
# caras en un dado justo, la probabilidad es 1/6.
# 6.-for _ in range(10):: Iniciamos un bucle que simulará 10 lanzamientos del dado y actualizará la probabilidad en cada iteración.
# 7.-resultado_lanzamiento = lanzamiento_dado_cargado(probabilidad_cargado): Simulamos un lanzamiento del dado y almacenamos el resultado.
# 8.-probabilidad_cargado = actualizar_probabilidad(probabilidad_cargado, resultado_lanzamiento, 6, 0.7, probabilidad_justo): 
# Actualizamos la probabilidad de que el dado esté cargado basada en el resultado del lanzamiento utilizando la función actualizar_probabilidad.
# 9.-print("Probabilidad de que el dado esté cargado:", probabilidad_cargado): Imprimimos la probabilidad actualizada después de 
# cada lanzamiento del dado.