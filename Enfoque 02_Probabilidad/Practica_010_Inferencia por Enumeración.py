#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# La Inferencia por Enumeración es un método exacto para calcular la probabilidad de una variable en un modelo gráfico probabilístico, 
# como una Red Bayesiana. Se utiliza para responder preguntas probabilísticas sobre el modelo, como calcular la probabilidad de que una variable 
# tome cierto valor dado ciertos valores observados de otras variables en el modelo.

# Funcionamiento de la Inferencia por Enumeración:
# El funcionamiento de la Inferencia por Enumeración implica los siguientes pasos:

# 1.- Definición del Modelo: Se define un modelo gráfico probabilístico que describe las relaciones entre las variables del problema. Esto incluye especificar 
#     las variables, sus estados posibles y las probabilidades condicionales entre ellas.
# 2.- Evidencia Observada: Se proporciona evidencia observada sobre ciertas variables en el modelo. Esto puede incluir valores observados de algunas variables o
#     restricciones sobre ciertas variables.
# 3.- Cálculo de Probabilidades: Se calcula la probabilidad de interés utilizando el algoritmo de Inferencia por Enumeración. Este algoritmo recorre todas las 
#     posibles combinaciones de valores de las variables no observadas, calcula la probabilidad conjunta de todas las variables dadas las observaciones y realiza sumas y productos para calcular la probabilidad deseada.
# 4.- Resultado: Se obtiene el resultado que indica la probabilidad calculada de la variable de interés dada la evidencia observada.
#--------------- PROGRAMA ------------------------------------
from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Definimos la estructura del modelo
modelo = BayesianModel([('A', 'C'), ('B', 'C')])

# Definimos las probabilidades condicionales
cpd_a = TabularCPD(variable='A', variable_card=2, values=[[0.6], [0.4]])
cpd_b = TabularCPD(variable='B', variable_card=2, values=[[0.7], [0.3]])
cpd_c = TabularCPD(variable='C', variable_card=2, 
                   values=[[0.8, 0.3, 0.2, 0.1],  # P(C|A=0,B=0), P(C|A=0,B=1), P(C|A=1,B=0), P(C|A=1,B=1)
                           [0.2, 0.7, 0.8, 0.9]], # P(C|A=0,B=0), P(C|A=0,B=1), P(C|A=1,B=0), P(C|A=1,B=1)
                   evidence=['A', 'B'], evidence_card=[2, 2])

# Asociamos las probabilidades condicionales al modelo
modelo.add_cpds(cpd_a, cpd_b, cpd_c)

# Verificamos si el modelo es válido
print("¿El modelo es válido?", modelo.check_model())

# Realizamos inferencia por enumeración para calcular P(A=1|B=0)
inferencia = VariableElimination(modelo)
resultado = inferencia.query(variables=['A'], evidence={'B': 0})
print("Probabilidad de A=1 dado B=0:", resultado.values[1])
#------------------------------------------------------------------------------------------------
# 1.- Importamos las clases y funciones necesarias de la biblioteca pgmpy para trabajar con modelos Bayesianos.
# 2.- Definimos la estructura del modelo especificando las relaciones entre las variables. En este ejemplo, tenemos dos variables A y B que influyen en una variable C.
# 3.- Creamos las tablas de distribución de probabilidad condicional (CPD) para cada variable, donde especificamos las probabilidades 
#     condicionales de cada variable dada la evidencia proporcionada por sus nodos padres.
# 4.- Asociamos las tablas de CPD al modelo que hemos definido.
# 5.- Verificamos si el modelo es válido, es decir, si las CPD especificadas satisfacen todas las restricciones del modelo.
# 6.- Utilizamos la inferencia por enumeración para calcular la probabilidad de la variable A dado que B es igual a 0.
# 7.- Imprimimos el resultado que muestra la probabilidad calculada.