#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# La programación lógica es un paradigma de programación que se basa en el uso de reglas lógicas y en la inferencia para resolver problemas. 
# Dos de los lenguajes más populares utilizados en la programación lógica son Prolog y CLIPS.

# Funcionamiento:

# 1.- Prolog:
# - En Prolog, los programas se escriben en términos de relaciones lógicas entre objetos. Estas relaciones se expresan en términos de predicados y cláusulas.
# - Un programa Prolog consiste en una base de conocimiento que contiene hechos y reglas. Los hechos son proposiciones que se consideran verdaderas,
#   mientras que las reglas son implicaciones lógicas que se pueden inferir a partir de los hechos.
# - Prolog utiliza el algoritmo de resolución para realizar inferencias sobre la base de conocimiento. Este algoritmo busca unificación entre las
#   cláusulas de la base de conocimiento y las metas de la consulta para demostrar si una consulta es verdadera o no.

# 2.- CLIPS:
# - En CLIPS, los programas se construyen a partir de hechos, reglas y acciones. Los hechos representan datos sobre el estado del mundo, las reglas 
#   representan conocimientos sobre relaciones entre estos datos, y las acciones representan los efectos de aplicar esas reglas.
# - CLIPS utiliza un sistema de inferencia basado en reglas de producción. Las reglas de producción son expresiones condicionales que especifican 
#   condiciones que deben cumplirse para que se dispare la regla, así como acciones que se deben tomar si se cumple la condición.
# - El motor de inferencia de CLIPS evalúa las reglas de producción y dispara aquellas cuyas condiciones se cumplen. Esto permite que el sistema 
#   realice inferencias sobre la base de conocimiento y tome decisiones basadas en esas inferencias.
#--------------- PROGRAMA ------------------------------------
from pyke import knowledge_engine

# Definimos las reglas en forma de strings
reglas = """
papa(X, Y) :- padre(X, Y).
papa(X, Y) :- esposo(X, Z), madre(Z, Y).

mama(X, Y) :- madre(X, Y).
mama(X, Y) :- esposa(X, Z), padre(Z, Y).

padre(juan, maria).
madre(ana, maria).
esposo(juan, ana).
esposa(ana, juan).
"""

# Definimos una función para cargar las reglas en el motor de conocimiento
def cargar_reglas(engine):
    engine.reset()  # Reiniciamos el motor de conocimiento
    engine.activate('reglas')  # Activamos la base de conocimiento 'reglas'
    engine.add_kb(reglas)  # Cargamos las reglas en el motor de conocimiento

# Definimos una función para hacer consultas
def consulta(engine, consulta_str):
    resultado = engine.prove_1_goal('reglas.' + consulta_str)  # Realizamos la consulta
    return [str(x) for x in resultado]  # Convertimos el resultado a una lista de strings

# Creamos un motor de conocimiento
engine = knowledge_engine.engine(__file__)

# Cargamos las reglas en el motor de conocimiento
cargar_reglas(engine)

# Hacemos algunas consultas
print("Padres de maria:", consulta(engine, "papa(X, maria)"))
print("Madres de maria:", consulta(engine, "mama(X, maria)"))

#-----------------------------------------------------------------------------
# 1.- Importamos la biblioteca pyke.knowledge_engine para utilizar el motor de conocimiento de PyKE.
# 2.- Definimos nuestras reglas en forma de strings. En este ejemplo, definimos reglas para inferir la relación padre-hijo y madre-hijo.
# 3.- Definimos una función cargar_reglas para cargar las reglas en el motor de conocimiento.
# 4.- Definimos una función consulta para realizar consultas al motor de conocimiento. La función prove_1_goal nos permite realizar una consulta y obtener el resultado.
# 5.- Creamos un motor de conocimiento usando knowledge_engine.engine(__file__).
# 6.- Cargamos las reglas en el motor de conocimiento llamando a la función cargar_reglas.
# 7.- Hacemos algunas consultas sobre las relaciones padre-hijo y madre-hijo y mostramos los resultados en la consola.