#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# Los agentes lógicos son una forma de agentes inteligentes que operan utilizando la lógica para razonar sobre su entorno y tomar decisiones.
# Estos agentes utilizan representaciones simbólicas y reglas de inferencia para interpretar y procesar la información.

# Funcionamiento:

# 1.- Representación del Conocimiento:
# - Los agentes lógicos representan el conocimiento utilizando lógica de primer orden, que incluye predicados, variables, 
#   cuantificadores y conectores lógicos como AND, OR y NOT.
# - El conocimiento se representa mediante reglas lógicas que establecen relaciones entre los diferentes elementos del dominio.
# 2.- Razonamiento Lógico:
# - Los agentes lógicos utilizan reglas de inferencia para realizar razonamientos lógicos sobre el conocimiento representado.
# - Pueden realizar inferencias deductivas, inductivas o abductivas para llegar a conclusiones basadas en el conocimiento disponible.
# 3.- Toma de Decisiones:
# - Basándose en las conclusiones derivadas del razonamiento lógico, los agentes lógicos pueden tomar decisiones para alcanzar sus objetivos.
# - Pueden utilizar algoritmos de planificación para generar secuencias de acciones que les permitan alcanzar un estado deseado.
# 4.- Interacción con el Entorno:
# - Los agentes lógicos pueden interactuar con su entorno mediante la adquisición de información, la realización de acciones y la observación de los resultados.
# - Utilizan la retroalimentación del entorno para ajustar su comportamiento y mejorar su desempeño en la realización de tareas.
#--------------- PROGRAMA ------------------------------------

from pyke import knowledge_engine

# Definimos una base de conocimiento básica con algunos hechos
base_conocimiento = """
es_mamifero(perro)
es_mamifero(gato)
es_mamifero(elefante)
es_mamifero(cebra)

es_reptil(lagarto)
es_reptil(tortuga)

es_carnivoro(perro)
es_carnivoro(gato)

es_herbivoro(elefante)
es_herbivoro(cebra)
"""

# Definimos una función para cargar la base de conocimiento en el motor de conocimiento
def cargar_base_conocimiento(engine):
    engine.reset()  # Reiniciamos el motor de conocimiento
    engine.activate('base_conocimiento')  # Activamos la base de conocimiento
    engine.add_kb(base_conocimiento)  # Cargamos la base de conocimiento en el motor

# Definimos una función para hacer consultas al agente lógico
def consulta(engine, query_str):
    resultado = engine.prove_1_goal('base_conocimiento.' + query_str)  # Realizamos la consulta
    return [str(x) for x in resultado]  # Convertimos el resultado a una lista de strings

# Creamos un motor de conocimiento
engine = knowledge_engine.engine(__file__)

# Cargamos la base de conocimiento en el motor
cargar_base_conocimiento(engine)

# Hacemos algunas consultas al agente lógico
print("¿El perro es un mamífero?", consulta(engine, "es_mamifero(perro)"))
print("¿La tortuga es un mamífero?", consulta(engine, "es_mamifero(tortuga)"))
print("¿El gato es carnívoro?", consulta(engine, "es_carnivoro(gato)"))

#-------------------------------------------------------------------------
# 1.- Definimos una base de conocimiento básica con algunos hechos sobre animales, como su clasificación como mamíferos, reptiles o su dieta.
# 2.- Definimos una función cargar_base_conocimiento para cargar la base de conocimiento en el motor de conocimiento.
#     Esta función reinicia el motor, activa la base de conocimiento y carga los hechos definidos.
# 3.- Definimos una función consulta para hacer consultas al agente lógico. Esta función utiliza el motor de conocimiento
#     para realizar la consulta y devuelve los resultados como una lista de strings.
# 4.- Creamos un motor de conocimiento utilizando knowledge_engine.engine(__file__).
# 5.- Cargamos la base de conocimiento en el motor llamando a la función cargar_base_conocimiento.
# 6.- Hacemos algunas consultas al agente lógico utilizando la función consulta y mostramos los resultados en la consola.