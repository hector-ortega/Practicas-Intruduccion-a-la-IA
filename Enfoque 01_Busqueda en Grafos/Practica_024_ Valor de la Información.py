#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# El algoritmo del "Valor de la Información" es una técnica utilizada en el análisis de decisiones bajo incertidumbre para evaluar el
# impacto de adquirir nueva información antes de tomar una decisión. La idea principal detrás de este algoritmo es determinar cuánto 
# puede aumentar la utilidad esperada de una decisión si se adquiere cierta información adicional.

# En el contexto de las redes de decisiones, el "Valor de la Información" se utiliza para calcular el valor que tiene obtener 
# cierta información antes de tomar una decisión. Esto implica evaluar cómo la nueva información puede afectar las probabilidades
# de los eventos futuros y, por lo tanto, influir en la utilidad esperada de la decisión.
# #--------------- PROGRAMA ------------------------------------   
 
class NodoDecision:
   class NodoDecision:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre del nodo de decisión

    def calcular_utilidad_esperada(self, red_decision, secuencia_decisiones):
        # Calcular la utilidad esperada tomando en cuenta la secuencia de decisiones
        return red_decision.calcular_utilidad_esperada(secuencia_decisiones)


class NodoEvento:
    def __init__(self, nombre, utilidades):
        self.nombre = nombre  # Nombre del nodo de evento
        self.utilidades = utilidades  # Utilidades asociadas a los posibles resultados del evento

    def calcular_utilidad_esperada(self, red_decision, secuencia_decisiones):
        # Calcular la utilidad esperada del evento
        return sum(probabilidad * red_decision.calcular_utilidad_esperada(secuencia_decisiones + [self.nombre]) 
                   for probabilidad, utilidad in self.utilidades.items())


class RedDecision:
    def __init__(self):
        self.nodos = {}  # Diccionario para almacenar los nodos de la red

    def agregar_nodo_decision(self, nombre):
        self.nodos[nombre] = NodoDecision(nombre)  # Agregar un nuevo nodo de decisión a la red

    def agregar_nodo_evento(self, nombre, utilidades):
        self.nodos[nombre] = NodoEvento(nombre, utilidades)  # Agregar un nuevo nodo de evento a la red

    def calcular_utilidad_esperada(self, secuencia_decisiones):
        utilidad_total = 0  # Inicializar la utilidad total

        for decision in secuencia_decisiones:
            if decision in self.nodos:  # Verificar si la decisión es un nodo de la red
                utilidad_total += self.nodos[decision].calcular_utilidad_esperada(self, secuencia_decisiones)  
                # Calcular la utilidad esperada de la decisión

        return utilidad_total

# Ejemplo de uso
red_decision = RedDecision()

# Agregar nodos de decisión
red_decision.agregar_nodo_decision("D1")
red_decision.agregar_nodo_decision("D2")

# Agregar nodos de evento con sus utilidades asociadas
red_decision.agregar_nodo_evento("E1", {0.3: 100, 0.7: 50})
red_decision.agregar_nodo_evento("E2", {0.2: 200, 0.5: 150, 0.3: 100})

# Calcular la utilidad esperada de una secuencia de decisiones
secuencia_decisiones = ["D1", "E1", "D2", "E2"]
utilidad_esperada = red_decision.calcular_utilidad_esperada(secuencia_decisiones)
print("Utilidad esperada de la secuencia de decisiones:", utilidad_esperada)