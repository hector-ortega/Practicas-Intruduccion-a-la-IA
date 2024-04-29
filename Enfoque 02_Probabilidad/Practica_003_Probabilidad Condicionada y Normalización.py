#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------

# La probabilidad condicionada nos permite calcular la probabilidad de un evento dada cierta información adicional o evidencia observada.
# Esto es fundamental en situaciones donde queremos hacer inferencias o tomar decisiones basadas en datos observados.

# Normalización:
# La normalización se refiere al proceso de ajustar las probabilidades para que sumen 1 después de tener en cuenta ciertas condiciones. 
# En muchos casos, después de calcular las probabilidades condicionadas para diferentes eventos, es necesario normalizar estas probabilidades 
# para garantizar que representen una distribución de probabilidad válida.

#--------------- PROGRAMA ------------------------------------
# Definimos una función para calcular la probabilidad condicionada
def calcular_probabilidad_condicionada(probabilidad_A, probabilidad_B_dado_A, probabilidad_B_dado_no_A):
    # Calculamos la probabilidad de B dado no A
    probabilidad_no_A = 1 - probabilidad_A
    # Calculamos la probabilidad de B usando el teorema de Bayes
    probabilidad_B = (probabilidad_A * probabilidad_B_dado_A) + (probabilidad_no_A * probabilidad_B_dado_no_A)
    # Calculamos la probabilidad condicionada de A dado B
    probabilidad_A_dado_B = (probabilidad_A * probabilidad_B_dado_A) / probabilidad_B
    return probabilidad_A_dado_B

# Definimos las probabilidades iniciales
probabilidad_enfermedad = 0.01  # Probabilidad a priori de que un paciente tenga la enfermedad
probabilidad_sintoma_dado_enfermedad = 0.9  # Probabilidad de que el paciente tenga el síntoma dado que tiene la enfermedad
probabilidad_sintoma_dado_no_enfermedad = 0.2  # Probabilidad de que el paciente tenga el síntoma dado que no tiene la enfermedad

# Calculamos la probabilidad condicionada de que el paciente tenga la enfermedad dado que tiene el síntoma
probabilidad_enfermedad_dado_sintoma = calcular_probabilidad_condicionada(probabilidad_enfermedad, probabilidad_sintoma_dado_enfermedad, probabilidad_sintoma_dado_no_enfermedad)

# Imprimimos el resultado
print("Probabilidad de que el paciente tenga la enfermedad dado que tiene el síntoma:", probabilidad_enfermedad_dado_sintoma)

#-------------------------------------------------------------------------
