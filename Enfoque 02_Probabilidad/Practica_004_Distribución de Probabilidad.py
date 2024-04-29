#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# La distribución de probabilidad es un concepto fundamental en la teoría de la probabilidad y se utiliza para describir 
# la probabilidad de ocurrencia de cada valor en un conjunto de datos. Los algoritmos de distribución de probabilidad se 
# utilizan para calcular esta distribución de probabilidad para un conjunto de datos dado.

# Utilización de la Distribución de Probabilidad:
# La distribución de probabilidad se utiliza en una amplia variedad de aplicaciones en diferentes campos, incluyendo:

# 1.- Estadística Descriptiva: En estadística, la distribución de probabilidad proporciona una descripción completa de los datos, lo que permite comprender
#     la tendencia central, la dispersión y la forma de la distribución de los datos.
# 2.- Inferencia Estadística: En inferencia estadística, la distribución de probabilidad se utiliza para realizar inferencias sobre poblaciones y muestras,
# calcular intervalos de confianza y realizar pruebas de hipótesis.
# 3.- Modelado y Simulación: En modelado y simulación, la distribución de probabilidad se utiliza para generar datos sintéticos que sigan ciertas características
# de distribución de probabilidad. Esto es útil para simular sistemas complejos y realizar análisis de riesgos.
# 4.- Aprendizaje Automático: En aprendizaje automático, la distribución de probabilidad se utiliza en algoritmos de modelado generativo para generar muestras de 
# datos que sean consistentes con la distribución de los datos de entrenamiento.
# 5.- Procesamiento de Señales y Procesamiento de Imágenes: En el procesamiento de señales y el procesamiento de imágenes, la distribución de probabilidad se 
# utiliza para modelar y analizar características de los datos, como el ruido y la variabilidad.
#--------------- PROGRAMA ------------------------------------
# Función para calcular la distribución de probabilidad
def calcular_distribucion_probabilidad(datos):
    distribucion = {}  # Creamos un diccionario para almacenar los conteos de cada valor en los datos
    total_datos = len(datos)  # Calculamos el total de datos en el conjunto
    
    # Iteramos sobre cada valor en los datos
    for valor in datos:
        if valor in distribucion:
            # Si el valor ya está en el diccionario, incrementamos su conteo
            distribucion[valor] += 1
        else:
            # Si el valor no está en el diccionario, lo inicializamos con un conteo de 1
            distribucion[valor] = 1
    
    # Calculamos la probabilidad de cada valor dividiendo su conteo por el total de datos
    for valor, conteo in distribucion.items():
        distribucion[valor] = conteo / total_datos
    
    return distribucion

# Datos de ejemplo
datos = [1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5]

# Calculamos la distribución de probabilidad de los datos
distribucion_probabilidad = calcular_distribucion_probabilidad(datos)

# Imprimimos la distribución de probabilidad
print("Distribución de probabilidad de los datos:")
for valor, probabilidad in distribucion_probabilidad.items():
    print(f"Valor: {valor}, Probabilidad: {probabilidad}")

#------------------------------------------------------------------------
# 1.- Definimos una función llamada calcular_distribucion_probabilidad que toma unalista de datos como entrada
#     y devuelve un diccionario que representa la distribución de probabilidad de los datos.
# 2.- Creamos un diccionario vacío llamado distribucion para almacenar los conteos de cada valor en los datos.
# 3.- Calculamos el total de datos en el conjunto utilizando la función len().
# 4.- Iteramos sobre cada valor en los datos utilizando un bucle for.
# 5.- Para cada valor, verificamos si ya está presente en el diccionario distribucion. Si lo está, incrementamos su conteo en 1;
#     de lo contrario, lo inicializamos con un conteo de 1.
# 6.- Una vez que hemos contado todas las ocurrencias de cada valor, calculamos la probabilidad de cada valor dividiendo su conteo por el total de datos.
# 7.- Devolvemos el diccionario distribucion que contiene la distribución de probabilidad calculada.
# 8.- Definimos una lista de datos de ejemplo.
# 9.- Calculamos la distribución de probabilidad de los datos de ejemplo utilizando la función calcular_distribucion_probabilidad.
# 10.- Imprimimos la distribución de probabilidad calculada, mostrando cada valor y su probabilidad correspondiente.