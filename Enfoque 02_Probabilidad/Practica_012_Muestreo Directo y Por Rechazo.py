#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# Muestreo Directo (Direct Sampling):
# El muestreo directo, también conocido como muestreo exacto, es un método utilizado para generar muestras de una distribución de probabilidad dada 
# utilizando las probabilidades condicionales directamente. Este método es adecuado cuando la distribución de probabilidad objetivo se puede calcular directamente y las muestras se pueden generar de manera eficiente.

# Funcionamiento:

# 1.- Se calcula la distribución de probabilidad objetivo.
# 2.- Se generan muestras de manera aleatoria según la distribución objetivo.
# 3.- Las muestras generadas se aceptan o rechazan según la probabilidad de la distribución objetivo.
# 4.- Se repiten los pasos 2 y 3 hasta obtener el número deseado de muestras.

# Muestreo por Rechazo (Rejection Sampling):
# El muestreo por rechazo es un método utilizado para generar muestras de una distribución de probabilidad dada utilizando una distribución auxiliar
# y un criterio de aceptación. Este método es útil cuando no se puede generar muestras directamente de la distribución objetivo, pero se puede generar
# muestras de una distribución auxiliar relacionada.

# Funcionamiento:

# 1.- Se define una distribución auxiliar que se pueda muestrear de manera eficiente.
# 2.- Se generan muestras de la distribución auxiliar.
# 3.- Se calcula la razón entre la probabilidad de la muestra bajo la distribución objetivo y la probabilidad de la muestra bajo la distribución auxiliar.
# 4.- Se acepta la muestra con una probabilidad proporcional a esta razón.
# 5.- Se repiten los pasos 2-4 hasta obtener el número deseado de muestras
#--------------- PROGRAMA ------------------------------------
import random

# Definimos la distribución de probabilidad objetivo P(X)
def distribucion_objetivo(x):
    return 0.5 * x if x >= 0 and x <= 10 else 0

# Definimos la distribución auxiliar Q(X) (en este caso, una distribución uniforme)
def distribucion_auxiliar():
    return random.uniform(0, 10)

# Muestreo Directo
def muestreo_directo(num_muestras):
    muestras = []
    for _ in range(num_muestras):
        x = random.uniform(0, 10)  # Generamos una muestra de X
        p = distribucion_objetivo(x)  # Calculamos la probabilidad de la muestra
        if random.uniform(0, 1) < p:  # Aceptamos la muestra con probabilidad p
            muestras.append(x)
    return muestras

# Muestreo por Rechazo
def muestreo_por_rechazo(num_muestras):
    muestras = []
    for _ in range(num_muestras):
        while True:
            x = distribucion_auxiliar()  # Generamos una muestra de X utilizando la distribución auxiliar
            p = distribucion_objetivo(x) / 0.5  # Calculamos la probabilidad de la muestra
            q = 1 / 10  # Calculamos la probabilidad de la muestra bajo la distribución auxiliar
            if random.uniform(0, 1) < p / q:  # Aceptamos la muestra con probabilidad p / q
                muestras.append(x)
                break
    return muestras

# Ejemplo de uso
num_muestras = 1000

# Muestreo Directo
muestras_directo = muestreo_directo(num_muestras)
print("Muestreo Directo:", muestras_directo[:10])

# Muestreo por Rechazo
muestras_rechazo = muestreo_por_rechazo(num_muestras)
print("Muestreo por Rechazo:", muestras_rechazo[:10])
#---------------------------------------------------------------------------
# 1.- Definimos la función distribucion_objetivo(x) que representa la distribución de probabilidad objetivo que queremos muestrear. 
#     En este caso, es una distribución triangular con base en [0, 10] y altura máxima en x=5.
# 2.- Definimos la función distribucion_auxiliar() que representa la distribución auxiliar que utilizaremos en el método de Muestreo por Rechazo.
#     En este caso, es una distribución uniforme en el intervalo [0, 10].
# 3.- Implementamos la función muestreo_directo(num_muestras) que realiza el muestreo directo generando muestras de la distribución objetivo y aceptándolas 
#     según la probabilidad de la distribución.
# 4.- Implementamos la función muestreo_por_rechazo(num_muestras) que realiza el muestreo por rechazo utilizando una distribución auxiliar y un criterio de
#     aceptación basado en la razón entre la probabilidad de la muestra bajo la distribución objetivo y la probabilidad bajo la distribución auxiliar.
# 5.- Ejecutamos ambos métodos y mostramos las primeras 10 muestras generadas por cada método.
