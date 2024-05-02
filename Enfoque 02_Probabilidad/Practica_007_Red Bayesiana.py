#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# Una Red Bayesiana es un modelo probabilístico que representa las relaciones entre un conjunto de variables aleatorias mediante un grafo dirigido acíclico.
# Cada nodo en el grafo representa una variable aleatoria, y las aristas representan relaciones causales o dependencias probabilísticas entre las variables.
# Se utiliza para modelar la incertidumbre y realizar inferencias sobre las probabilidades condicionales de las variables dadas ciertas evidencias observadas.

# Funcionamiento de una Red Bayesiana:
# El funcionamiento de una Red Bayesiana se basa en dos conceptos fundamentales:

# Estructura del Grafo: La estructura del grafo define las relaciones causales o dependencias probabilísticas entre las variables. Cada nodo en el 
# grafo representa una variable aleatoria y las aristas representan las dependencias entre las variables. La dirección de las aristas indica la dirección 
# de la influencia causal.
# Probabilidades Condicionales: Cada nodo en la Red Bayesiana está asociado con una tabla de distribución de probabilidad condicional (CPD), que especifica 
# la probabilidad de cada estado de la variable dado el estado de sus nodos padres. Estas probabilidades condicionales permiten realizar inferencias sobre las 
# probabilidades de las variables dadas ciertas evidencias observadas.
#--------------- PROGRAMA ------------------------------------
from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Definimos la estructura de la Red Bayesiana
modelo = BayesianModel([('clima', 'jugar_tenis')])

# Definimos las probabilidades condicionales
cpd_clima = TabularCPD(variable='clima', variable_card=2, values=[[0.7], [0.3]])
cpd_jugar_tenis = TabularCPD(variable='jugar_tenis', variable_card=2, 
                              values=[[0.9, 0.6],  # P(jugar_tenis=0|clima=0), P(jugar_tenis=0|clima=1)
                                      [0.1, 0.4]], # P(jugar_tenis=1|clima=0), P(jugar_tenis=1|clima=1)
                              evidence=['clima'], evidence_card=[2])

# Asociamos las probabilidades condicionales al modelo
modelo.add_cpds(cpd_clima, cpd_jugar_tenis)

# Verificamos si el modelo es válido
print("¿El modelo es válido?", modelo.check_model())

# Creamos un objeto de inferencia basado en eliminación de variables
inferencia = VariableElimination(modelo)

# Calculamos la probabilidad de jugar al tenis dado el clima
resultado = inferencia.query(variables=['jugar_tenis'], evidence={'clima': 0})
print("Probabilidad de jugar al tenis dado que el clima es malo:", resultado.values[1])

#---------------------------------------------------------------------------------------------------
# 1.- Importamos las clases y funciones necesarias de pgmpy para trabajar con Redes Bayesianas.
# 2.- Definimos la estructura de la Red Bayesiana especificando las relaciones entre las variables. En este caso, 
#     solo hay dos variables: el clima y si se juega al tenis.
# 3.- Creamos las tablas de distribución de probabilidad condicional (CPD) para cada variable. Las CPD especifican la
#     probabilidad de cada estado de la variable dada la evidencia proporcionada por sus nodos padres.
# 4.- Agregamos las tablas de CPD al modelo.
# 5.- Verificamos si el modelo es válido, es decir, si las CPD especificadas satisfacen todas las restricciones de la Red Bayesiana.
# 6.- Creamos un objeto de inferencia basado en la eliminación de variables para realizar consultas probabilísticas en el modelo.
# 7.- Realizamos una consulta para calcular la probabilidad de jugar al tenis dado que el clima es malo.
# 8.- Imprimimos el resultado que muestra la probabilidad calculada.