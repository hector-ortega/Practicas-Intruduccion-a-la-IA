#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------

# La lógica temporal es una extensión de la lógica formal que se utiliza para razonar sobre el tiempo y las relaciones temporales entre eventos.
# Se utiliza para expresar proposiciones acerca de cuándo ciertas condiciones son verdaderas o falsas a lo largo del tiempo, y para realizar 
# razonamientos sobre secuencias de eventos y su orden temporal.

# Funcionamiento: 

# 1.- Operadores Temporales:
# - La lógica temporal introduce operadores temporales que permiten expresar relaciones temporales entre eventos y estados a lo largo del tiempo.
# - Estos operadores incluyen operadores como "antes que", "después que", "al mismo tiempo que", "en algún momento", "siempre", "hasta", etc.

# 2.- Modelado de Eventos y Estados:
# - En la lógica temporal, los eventos y estados se modelan como puntos en el tiempo o intervalos de tiempo durante los cuales ciertas condiciones son verdaderas.
# - Se utilizan fórmulas temporales para expresar proposiciones sobre la ocurrencia de eventos y la evolución temporal de estados.

# 3.- Semántica Temporal:
# - La lógica temporal tiene una semántica formal que define el significado de las fórmulas temporales en términos de modelos temporales y relaciones
#   temporales entre eventos y estados.
# - Esta semántica permite interpretar las fórmulas temporales y realizar razonamientos sobre su verdad o falsedad en un contexto temporal dado.

# 4.- Verificación Formal:
# - Se utilizan algoritmos de verificación formal para verificar la validez de fórmulas temporales y para comprobar si un sistema cumple ciertas propiedades
#   temporales especificadas.
# - Estos algoritmos pueden basarse en técnicas de model checking, teoría de grafos, lógica modal temporal, etc.
#--------------- PROGRAMA ------------------------------------
class Regla:
    """
    Clase que representa una regla en el sistema de lógica no monótona.
    """
    def __init__(self, antecedente, consecuente):
        self.antecedente = antecedente  # Parte izquierda de la regla
        self.consecuente = consecuente  # Parte derecha de la regla

    def __str__(self):
        return f"{self.antecedente} => {self.consecuente}"


class SistemaLogicaNoMonotona:
    """
    Clase que representa un sistema de lógica no monótona.
    """
    def __init__(self):
        self.reglas = []  # Lista de reglas en el sistema

    def agregar_regla(self, regla):
        """
        Agrega una regla al sistema.
        """
        self.reglas.append(regla)

    def aplicar_reglas(self, hecho):
        """
        Aplica las reglas del sistema para derivar conclusiones.
        """
        conclusiones = []  # Lista de conclusiones derivadas
        
        # Itera sobre cada regla en el sistema
        for regla in self.reglas:
            # Verifica si el antecedente de la regla está presente en los hechos
            if regla.antecedente in hecho:
                conclusiones.append(regla.consecuente)  # Agrega la conclusión a la lista
                
        return conclusiones


# Creamos un sistema de lógica no monótona
sistema = SistemaLogicaNoMonotona()

# Definimos algunas reglas por defecto
regla1 = Regla("p", "q")  # Si p es verdadero, entonces q es verdadero por defecto
regla2 = Regla("q", "r")  # Si q es verdadero, entonces r es verdadero por defecto

# Agregamos las reglas al sistema
sistema.agregar_regla(regla1)
sistema.agregar_regla(regla2)

# Definimos algunos hechos iniciales
hechos = ["p"]  # Se asume inicialmente que p es verdadero

# Aplicamos las reglas para derivar conclusiones
conclusiones = sistema.aplicar_reglas(hechos)

# Imprimimos las conclusiones derivadas
print("Conclusiones derivadas:")
for conclusion in conclusiones:
    print(conclusion)

#----------------------------------------------------------------
# Este código implementa un sistema de lógica no monótona simple utilizando el principio de "default logic". La clase Regla representa 
# una regla con un antecedente y un consecuente, mientras que la clase SistemaLogicaNoMonotona representa el sistema de lógica no monótona en sí.

# El programa crea un sistema de lógica no monótona, define algunas reglas por defecto, agrega las reglas al sistema, y luego define 
# algunos hechos iniciales. Luego, aplica las reglas del sistema a los hechos iniciales para derivar conclusiones.