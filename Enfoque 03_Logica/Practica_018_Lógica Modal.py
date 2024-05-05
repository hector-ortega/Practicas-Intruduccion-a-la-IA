#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------

# La lógica modal es una extensión de la lógica proposicional y de primer orden que introduce modalidades para expresar nociones como posibilidad, 
# necesidad, conocimiento, creencia, obligación, entre otras. Se utiliza para razonar sobre estados posibles del mundo y las relaciones entre ellos, 
# permitiendo modelar situaciones complejas donde es importante considerar diferentes niveles de certeza o modalidades.

# Funcionamiento:

# 1.-Operadores Modales:
# - La lógica modal introduce operadores modales, como □ (necesidad) y ◇ (posibilidad), que permiten expresar relaciones entre estados posibles del mundo.
# - Estos operadores se aplican a fórmulas lógicas para indicar que una proposición es necesaria o posible en un conjunto de mundos posibles.

# 2.- Semántica de Mundos Posibles:
# - En la lógica modal, se utiliza la semántica de mundos posibles para interpretar las fórmulas modales.
# - Cada mundo posible representa un estado o situación posible del mundo, y las relaciones entre estos mundos determinan la validez de las modalidades.

# 3.- Reglas de Inferencia:
# - Se utilizan reglas de inferencia específicas para la lógica modal que permiten derivar nuevas proposiciones basadas en las relaciones modales entre
#   los mundos posibles.
# - Estas reglas permiten realizar razonamientos válidos sobre modalidades y alcanzar conclusiones sobre el conocimiento y las creencias de los agentes.

# 4.- Sintaxis y Semántica Formal:
# - La lógica modal tiene una sintaxis formal para expresar proposiciones modales y una semántica formal para interpretar el significado de estas
#   proposiciones en términos de mundos posibles y relaciones modales.
#--------------- PROGRAMA ------------------------------------
class Mundo:
    """
    Clase que representa un mundo en el sistema de lógica modal.
    """
    def __init__(self, nombre):
        self.nombre = nombre
        self.proposiciones = set()  # Conjunto de proposiciones verdaderas en este mundo
    
    def agregar_proposicion(self, proposicion):
        """
        Agrega una proposición verdadera a este mundo.
        """
        self.proposiciones.add(proposicion)

    def __str__(self):
        return f"Mundo {self.nombre}: {self.proposiciones}"


class Agente:
    """
    Clase que representa un agente en el sistema de lógica modal.
    """
    def __init__(self, nombre):
        self.nombre = nombre

    def cree_en(self, mundo, proposicion):
        """
        Verifica si el agente cree en una proposición en un mundo dado.
        """
        return proposicion in mundo.proposiciones

    def __str__(self):
        return f"Agente {self.nombre}"


# Creamos algunos mundos
mundo1 = Mundo("M1")
mundo1.agregar_proposicion("p")
mundo2 = Mundo("M2")
mundo2.agregar_proposicion("p")
mundo2.agregar_proposicion("q")

# Creamos un agente
agente1 = Agente("A1")

# Verificamos si el agente cree en una proposición en un mundo dado
print(f"{agente1} cree en 'p' en {mundo1}: {agente1.cree_en(mundo1, 'p')}")
print(f"{agente1} cree en 'p' en {mundo2}: {agente1.cree_en(mundo2, 'p')}")
print(f"{agente1} cree en 'q' en {mundo2}: {agente1.cree_en(mundo2, 'q')}")

#--------------------------------------------------------------------------
# Este código define dos clases: Mundo y Agente, que representan mundos posibles y agentes respectivamente en un sistema de lógica modal. 
# Los mundos pueden tener un conjunto de proposiciones verdaderas, y los agentes pueden creer en ciertas proposiciones en ciertos mundos.

# El programa crea dos mundos (mundo1 y mundo2) con diferentes conjuntos de proposiciones y un agente (agente1). Luego, el programa 
# verifica si el agente cree en ciertas proposiciones en cada uno de los mundos utilizando el método cree_en de la clase Agente.