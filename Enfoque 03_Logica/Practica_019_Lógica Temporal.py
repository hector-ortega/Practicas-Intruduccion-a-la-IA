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
class Evento:
    """
    Clase que representa un evento en el sistema de lógica temporal.
    """
    def __init__(self, nombre, tiempo):
        self.nombre = nombre
        self.tiempo = tiempo

    def __str__(self):
        return f"Evento '{self.nombre}' en el tiempo {self.tiempo}"


# Creamos algunos eventos
evento1 = Evento("A", 1)
evento2 = Evento("B", 2)
evento3 = Evento("C", 3)

# Verificamos relaciones temporales entre eventos
print(f"{evento1} sucede antes que {evento2}: {evento1.tiempo < evento2.tiempo}")
print(f"{evento2} sucede antes que {evento3}: {evento2.tiempo < evento3.tiempo}")
print(f"{evento1} sucede al mismo tiempo que {evento3}: {evento1.tiempo == evento3.tiempo}")

#-------------------------------------------------------------------------------

# Este código define una clase Evento que representa un evento en el sistema de lógica temporal. 
# Cada evento tiene un nombre y un tiempo asociado. Luego, se crean algunos eventos (evento1, evento2 y evento3) con diferentes tiempos. 
# Finalmente, se verifican algunas relaciones temporales entre los eventos, como "antes que", "después que" y "al mismo tiempo que".