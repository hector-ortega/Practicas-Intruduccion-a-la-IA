#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------

# La Gramática Causal Definida (DGC) es un marco teórico utilizado en inteligencia artificial y ciencias cognitivas
# para modelar y comprender relaciones causales entre eventos. Se utiliza para representar cómo ciertos eventos
# pueden influir en otros dentro de un sistema o dominio específico.

# La idea principal detrás de la DGC es representar las relaciones causales entre eventos de una manera formal 
# y estructurada, de modo que se puedan realizar inferencias y razonamientos sobre cómo los cambios en un evento 
# pueden afectar a otros eventos en el sistema.

# La DGC se basa en la noción de que los eventos pueden tener causas y efectos, y que estas relaciones causales
# pueden ser modeladas y analizadas utilizando estructuras gramaticales. En esencia, la DGC proporciona un marco 
# para describir cómo los eventos están interconectados causalmente en un sistema dado.

# Los algoritmos asociados con la DGC se utilizan para construir y manipular estas estructuras gramaticales,
# lo que permite realizar tareas como el razonamiento causal, la predicción de efectos de acciones, la planificación
# basada en causas, entre otras

#--------------- PROGRAMA ------------------------------------

class Event:
    def __init__(self, name):
        self.name = name
        self.causes = []
        self.effects = []

    def add_cause(self, cause_event):
        self.causes.append(cause_event)

    def add_effect(self, effect_event):
        self.effects.append(effect_event)


class CausalGrammar:
    def __init__(self):
        self.events = {}

    def add_event(self, event_name):
        event = Event(event_name)
        self.events[event_name] = event
        return event

    def add_causal_relation(self, cause_event_name, effect_event_name):
        cause_event = self.events.get(cause_event_name)
        effect_event = self.events.get(effect_event_name)
        if cause_event and effect_event:
            effect_event.add_cause(cause_event)
            cause_event.add_effect(effect_event)

    def print_causal_relations(self):
        for event_name, event in self.events.items():
            print(f"Event: {event_name}")
            print("Causes:")
            for cause in event.causes:
                print(f"\t- {cause.name}")
            print("Effects:")
            for effect in event.effects:
                print(f"\t- {effect.name}")


# Crear una instancia de la Gramática Causal Definida
causal_grammar = CausalGrammar()

# Definir eventos
event_a = causal_grammar.add_event("A")
event_b = causal_grammar.add_event("B")
event_c = causal_grammar.add_event("C")

# Definir relaciones causales
causal_grammar.add_causal_relation("A", "B")
causal_grammar.add_causal_relation("B", "C")

# Imprimir relaciones causales
causal_grammar.print_causal_relations()
#--------------------------------------------------------------
# La clase Event tiene un nombre y listas de eventos que causa y eventos que son causados por él.
# La clase CausalGrammar mantiene un diccionario de eventos y proporciona métodos para agregar eventos y relaciones causales entre ellos.
# Creamos una instancia de CausalGrammar, agregamos algunos eventos y definimos relaciones causales entre ellos.
# Finalmente, imprimimos las relaciones causales para demostrar que funciona correctamente.