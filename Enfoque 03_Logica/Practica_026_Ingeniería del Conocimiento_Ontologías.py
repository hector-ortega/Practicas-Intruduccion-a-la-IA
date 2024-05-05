#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------

# La Ingeniería del Conocimiento se refiere al diseño y desarrollo de sistemas que son capaces de representar, manipular y utilizar el conocimiento de manera 
# efectiva para resolver problemas en un dominio específico. Las ontologías son una parte fundamental de la Ingeniería del Conocimiento y se utilizan para 
# formalizar y estructurar el conocimiento en un dominio particular.

# Funcionamiento de un Algoritmo de Ontologías:

# 1.- Definición de la Ontología:
# - En primer lugar, se define la estructura de la ontología, incluyendo las clases, propiedades y relaciones relevantes para el dominio en cuestión. 
#   Esto se puede hacer utilizando un lenguaje de modelado ontológico como RDF (Resource Description Framework) o OWL (Web Ontology Language).

# 2.- Creación de Instancias:
# - Se crean instancias individuales de las clases definidas en la ontología y se les asignan valores para las propiedades correspondientes. 
#   Estas instancias representan entidades específicas del dominio.

# 3.- Razonamiento y Consultas:
# - Se utiliza la ontología para realizar razonamiento sobre el conocimiento representado en ella. Esto puede incluir la inferencia de 
#   nuevas relaciones entre entidades, la deducción de información implícita y la resolución de consultas sobre el conocimiento.

# 4.- Interoperabilidad y Aplicaciones:
# - La ontología se puede utilizar en diferentes aplicaciones y contextos para facilitar la interoperabilidad de datos, la integración de 
#   sistemas y el desarrollo de sistemas inteligentes que requieren un entendimiento semántico del dominio.
#--------------- PROGRAMA ------------------------------------
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS

# Creamos un nuevo grafo RDF
g = Graph()

# Definimos un espacio de nombres para nuestra ontología
onto = Namespace("http://ejemplo.org/ontologia#")

# Definimos clases y propiedades en la ontología
g.add((onto.Persona, RDF.type, RDFS.Class))
g.add((onto.Edad, RDF.type, RDFS.Property))
g.add((onto.Nombre, RDF.type, RDFS.Property))

# Creamos instancias individuales en la ontología
g.add((onto.Juan, RDF.type, onto.Persona))
g.add((onto.Juan, onto.Nombre, Literal("Juan")))
g.add((onto.Juan, onto.Edad, Literal(30)))

# Realizamos consultas sobre la ontología
for s, p, o in g.triples((None, RDF.type, onto.Persona)):
    print(f"{s} es una persona")

for s, p, o in g.triples((None, onto.Nombre, None)):
    print(f"Nombre: {o}")

for s, p, o in g.triples((None, onto.Edad, None)):
    print(f"Edad: {o}")

# Serializamos y guardamos la ontología en un archivo
g.serialize("ontologia.rdf", format="xml")

#------------------------------------------------------------------
# 1.- Importamos las clases Graph, Namespace y Literal de la biblioteca RDFLib, así como los espacios de nombres RDF y RDFS.
# 2.- Creamos un nuevo grafo RDF usando Graph().
# 3.- Definimos un espacio de nombres onto para nuestra ontología.
# 4.- Definimos clases y propiedades en la ontología utilizando el método add() del grafo. Por ejemplo, definimos la clase Persona y las propiedades Edad y Nombre.
# 5.- Creamos instancias individuales en la ontología utilizando el método add(). Por ejemplo, creamos la instancia Juan de la clase Persona y le asignamos valores para las propiedades Nombre y Edad.
# 6.- Realizamos consultas sobre la ontología utilizando el método triples(). Por ejemplo, buscamos todas las instancias de la clase Persona y sus propiedades.
# 7.- Serializamos y guardamos la ontología en un archivo utilizando el método serialize(). En este caso, la guardamos en formato XML.