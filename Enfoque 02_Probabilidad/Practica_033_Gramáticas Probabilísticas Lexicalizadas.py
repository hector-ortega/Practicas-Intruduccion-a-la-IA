#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.
#-----------------TEORIA----------------------------------------
# Las Gramáticas Probabilísticas Lexicalizadas (GPL) son un tipo de gramática probabilística utilizada en el procesamiento del lenguaje natural (PLN). 
# Estas gramáticas extienden las Gramáticas Probabilísticas Contextuales (GPC) al asociar probabilidades con cada regla de producción y permitir que los 
# símbolos no terminales tengan múltiples opciones de expansión con probabilidades asociadas.

# Las GPL son especialmente útiles en tareas como la generación de lenguaje natural, el análisis sintáctico y la traducción automática. Permiten modelar 
# la estructura gramatical de un idioma de una manera más realista al considerar la variabilidad y la ambigüedad que se encuentran en el lenguaje natural.

# En una GPL, cada regla de producción está asociada con una probabilidad que indica la verosimilitud de esa regla en un contexto particular. Por ejemplo, 
# en una regla como NP -> Det N [0.6] | N [0.4], la primera expansión tiene una probabilidad del 60% de ocurrir, mientras que la segunda tiene una probabilidad del 40%.
#--------------- PROGRAMA --------------------------------------
import random

class ProbabilisticGrammar:
    def __init__(self):
        self.productions = {}

    def add_production(self, non_terminal, expansions):
        if non_terminal not in self.productions:
            self.productions[non_terminal] = []
        self.productions[non_terminal].extend(expansions)

    def expand(self, symbol):
        if symbol in self.productions:
            expansions = self.productions[symbol]
            return random.choices(expansions)
        else:
            return [symbol]

# Creación de una instancia de la gramática
grammar = ProbabilisticGrammar()

# Definición de las reglas de producción
grammar.add_production('S', ['NP VP'])
grammar.add_production('NP', ['Det N [0.6]', 'N [0.4]'])
grammar.add_production('VP', ['V NP'])
grammar.add_production('Det', ['the', 'a'])
grammar.add_production('N', ['dog', 'cat'])
grammar.add_production('V', ['chased', 'ate'])

# Función para generar una oración aleatoria
def generate_sentence(grammar):
    sentence = []
    sentence.extend(grammar.expand('S'))
    return ' '.join(sentence)

# Generación de una oración aleatoria
random_sentence = generate_sentence(grammar)
print("Random Sentence:", random_sentence)

#--------------------------------------------------------------------
# 1.- Importamos el módulo random para generar números aleatorios.
# 2.- Creamos una clase ProbabilisticGrammar que representa una Gramática Probabilística.
# 3.- En el método __init__, inicializamos el diccionario productions para almacenar las reglas de producción.
# 4.- El método add_production agrega una regla de producción al diccionario productions.
# 5.- El método expand toma un símbolo no terminal y devuelve una de sus expansiones con base en las probabilidades asociadas.
# 6.- Creamos una instancia de la gramática llamada grammar.
# 7.- Definimos las reglas de producción de la gramática.
# 8.- Definimos una función generate_sentence que genera una oración aleatoria utilizando la gramática.
# 9.- Finalmente, generamos una oración aleatoria y la imprimimos.