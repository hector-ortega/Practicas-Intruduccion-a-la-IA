#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# El algoritmo de Eliminación de Variables es una técnica utilizada para realizar inferencia en modelos gráficos probabilísticos, como las Redes Bayesianas.
# Su objetivo principal es calcular la probabilidad de una variable de interés dadas ciertas observaciones o evidencias, eliminando las variables no relevantes 
# del cálculo. Esto permite reducir la complejidad computacional de la inferencia y hacerla más eficiente.

# Funcionamiento del algoritmo de Eliminación de Variables:
# 1.- Definición del Modelo: Se comienza con un modelo gráfico probabilístico que describe las relaciones entre las variables del problema, como una Red Bayesiana.
#     Este modelo incluye nodos que representan variables y arcos que representan relaciones de dependencia condicional entre ellas.
# 2.- Evidencia Observada: Se proporciona evidencia observada sobre ciertas variables en el modelo, es decir, se conocen sus valores. Esta evidencia puede incluir 
#     valores observados de algunas variables o restricciones sobre ciertas variables.
# 3.- Eliminación de Variables no Relevantes: El algoritmo identifica las variables que no son relevantes para la pregunta de inferencia y las elimina del cálculo. 
#     Esto se hace eliminando las variables que no están en el camino activo entre la variable de interés y las variables observadas.
# 4.- Cálculo de la Probabilidad: Una vez que se han eliminado las variables no relevantes, se calcula la probabilidad de la variable de interés dadas las observaciones
#     utilizando métodos de suma y producto sobre las probabilidades condicionales.
# 5.- Resultado de la Inferencia: Se obtiene el resultado de la inferencia, que representa la probabilidad calculada de la variable de interés dada la evidencia observada.
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

# Creamos un objeto VariableElimination para realizar inferencia
inferencia = VariableElimination(modelo)

# Realizamos inferencia para calcular P(A=1|B=0)
resultado = inferencia.query(variables=['A'], evidence={'B': 0})
print("Probabilidad de A=1 dado B=0:", resultado.values[1])
#----------------------------------------------------------------------------
# 1.- Importamos las clases y funciones necesarias de la biblioteca pgmpy para trabajar con modelos Bayesianos y realizar inferencia.
# 2.- Definimos la estructura del modelo especificando las relaciones entre las variables. En este ejemplo, tenemos dos variables A y B que influyen en una variable C.
# 3.- Creamos las tablas de distribución de probabilidad condicional (CPD) para cada variable, donde especificamos las probabilidades condicionales de cada variable dada
# la evidencia proporcionada por sus nodos padres.
# 4.- Asociamos las tablas de CPD al modelo que hemos definido.
# 5.- Creamos un objeto VariableElimination para realizar inferencia en el modelo.
# 6.- Utilizamos el método query del objeto VariableElimination para calcular la probabilidad de la variable A dado que B es igual a 0.
# 7.- Imprimimos el resultado que muestra la probabilidad calculada.