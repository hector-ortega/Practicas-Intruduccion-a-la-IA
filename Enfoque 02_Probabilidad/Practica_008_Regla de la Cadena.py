#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# La Regla de la Cadena es un principio fundamental en la teoría de la probabilidad que nos permite calcular la probabilidad conjunta de un conjunto 
# de variables aleatorias descomponiéndola en una serie de probabilidades condicionales más simples. Este principio es esencial para calcular la probabilidad 
# conjunta de eventos que dependen de otros eventos en una secuencia.
# l funcionamiento de la Regla de la Cadena implica los siguientes conceptos clave:

# 1.-Probabilidades Condicionales: La Regla de la Cadena se basa en el cálculo de probabilidades condicionales. Cada variable en la secuencia tiene una 
#     probabilidad condicional asociada que representa la probabilidad de la variable dada la ocurrencia de las variables anteriores en la secuencia.
# 2.- Multiplicación de Probabilidades Condicionales: Para calcular la probabilidad conjunta de un conjunto de variables aleatorias, simplemente multiplicamos 
#     las probabilidades condicionales de cada variable dada la ocurrencia de las variables anteriores en la secuencia. Esto se conoce como "encadenamiento" de las 
#     probabilidades condicionales.
# 3.- Probabilidad Conjunta: La probabilidad conjunta de todas las variables en la secuencia es el producto de todas las probabilidades condicionales en la secuencia. 
#     Esto nos da la probabilidad de que ocurran todos los eventos en la secuencia en conjunto.
#--------------- PROGRAMA ------------------------------------
# Definimos las probabilidades condicionales P(A), P(B|A) y P(C|B)
probabilidad_A = 0.6
probabilidad_B_dado_A = 0.7
probabilidad_C_dado_B = 0.8

# Calculamos la probabilidad conjunta P(A, B, C) utilizando la Regla de la Cadena
probabilidad_conjunta = probabilidad_A * probabilidad_B_dado_A * probabilidad_C_dado_B

# Imprimimos el resultado
print("La probabilidad conjunta de A, B y C es:", probabilidad_conjunta)
#---------------------------------------------------------------------------------------
# 1.- Definimos las probabilidades condicionales P(A), P(B|A) y P(C|B). Estas representan la probabilidad de cada variable aleatoria dada 
#     la ocurrencia de las variables anteriores en la secuencia.
# 2.- Calculamos la probabilidad conjunta P(A, B, C) utilizando la Regla de la Cadena, que es simplemente el producto de las 
#     probabilidades condicionales de cada variable dada la ocurrencia de las anteriores.
# 3.- Imprimimos el resultado que muestra la probabilidad conjunta calculada.