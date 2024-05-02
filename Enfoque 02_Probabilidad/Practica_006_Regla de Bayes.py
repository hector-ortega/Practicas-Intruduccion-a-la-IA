#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# La Regla de Bayes es un principio fundamental en la teoría de la probabilidad que nos permite actualizar nuestras creencias 
# sobre la ocurrencia de un evento dado que hemos observado evidencia relacionada con ese evento. Este principio lleva el nombre 
# del matemático británico Thomas Bayes y es ampliamente utilizado en una variedad de campos, incluyendo la estadística, el aprendizaje automático, 
# la inteligencia artificial, la medicina, entre otros.
# El funcionamiento de un algoritmo de Regla de Bayes implica los siguientes pasos:
# 1.- Definición de las Probabilidades a Priori: Se definen las probabilidades iniciales de los eventos o hipótesis antes de observar cualquier evidencia. 
#     Estas probabilidades se denominan "probabilidades a priori".
# 2.- Observación de la Evidencia: Se observa alguna evidencia relacionada con los eventos de interés.
# 3.- Cálculo de las Probabilidades Condicionales: Se calculan las probabilidades condicionales de que ocurran los eventos dados los datos observados.
#     Estas probabilidades se denominan "probabilidades condicionales".
# 4.- Aplicación de la Regla de Bayes: Se aplica la fórmula de Bayes para actualizar las probabilidades a priori con la nueva evidencia y calcular 
#     las probabilidades a posteriori. La fórmula de Bayes es:
# P(A|B) = (P(B|A) X P(A))/P(B)
# Donde:
# P(A|B) es la probabilad posterior de que ocurra el evento A dada la evidencia B
# P(B|A) es la probabilidad de que ocurra la evidencia B dado que el evento A ha ocurrido
# P(A) es la probabilidad a priori del evento A
# P(B) es la probabilidad de que ocurra la evidencia B independientemente de si el evento A ocurre o no

#--------------- PROGRAMA ------------------------------------
def regla_de_bayes(probabilidad_enfermedad, probabilidad_positivo_dado_enfermedad, probabilidad_positivo_dado_no_enfermedad):
    # Calculamos la probabilidad de no tener la enfermedad
    probabilidad_no_enfermedad = 1 - probabilidad_enfermedad
    
    # Calculamos la probabilidad de dar positivo en la prueba utilizando la Regla de Bayes
    probabilidad_positivo = (probabilidad_enfermedad * probabilidad_positivo_dado_enfermedad) + (probabilidad_no_enfermedad * probabilidad_positivo_dado_no_enfermedad)
    
    # Calculamos la probabilidad de tener la enfermedad dado un resultado positivo en la prueba
    probabilidad_enfermedad_dado_positivo = (probabilidad_enfermedad * probabilidad_positivo_dado_enfermedad) / probabilidad_positivo
    
    return probabilidad_enfermedad_dado_positivo

# Definimos las probabilidades iniciales
probabilidad_enfermedad = 0.01  # Probabilidad a priori de tener la enfermedad
probabilidad_positivo_dado_enfermedad = 0.9  # Probabilidad de dar positivo en la prueba dado que se tiene la enfermedad
probabilidad_positivo_dado_no_enfermedad = 0.2  # Probabilidad de dar positivo en la prueba dado que no se tiene la enfermedad

# Calculamos la probabilidad de tener la enfermedad dado un resultado positivo en la prueba
probabilidad_enfermedad_dado_positivo = regla_de_bayes(probabilidad_enfermedad, probabilidad_positivo_dado_enfermedad, probabilidad_positivo_dado_no_enfermedad)

# Imprimimos el resultado
print("La probabilidad de tener la enfermedad dado un resultado positivo en la prueba es:", probabilidad_enfermedad_dado_positivo)

#----------------------------------------------------------------------------------------------------------
# 1.- Definimos una función llamada regla_de_bayes que toma como argumentos la probabilidad a priori de tener la enfermedad, 
#     la probabilidad de dar positivo en la prueba dado que se tiene la enfermedad y la probabilidad de dar positivo en la prueba dado que no se tiene la enfermedad.
# 2.- Calculamos la probabilidad de no tener la enfermedad restando la probabilidad de tener la enfermedad de 1.
# 3.- Calculamos la probabilidad de dar positivo en la prueba utilizando la Regla de Bayes, que implica calcular la probabilidad conjunta de tener 
#     la enfermedad y dar positivo en la prueba, y la probabilidad conjunta de no tener la enfermedad y dar positivo en la prueba.
# 4.- Calculamos la probabilidad de tener la enfermedad dado un resultado positivo en la prueba utilizando la fórmula de Bayes.
# 5.- Definimos las probabilidades iniciales relacionadas con el ejemplo de diagnóstico médico.
# 6.- Llamamos a la función regla_de_bayes para calcular la probabilidad de tener la enfermedad dado un resultado positivo en la prueba.
# 7.- Imprimimos el resultado que muestra la probabilidad calculada.