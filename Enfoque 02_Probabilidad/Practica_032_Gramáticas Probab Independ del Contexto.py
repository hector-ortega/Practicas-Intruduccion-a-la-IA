#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.
#-----------------TEORIA----------------------------------------
# Un Modelo Probabilístico del Lenguaje (PML) se utiliza en el procesamiento del lenguaje natural (PLN) para asignar probabilidades a 
# secuencias de palabras o caracteres. Estos modelos se utilizan en una variedad de aplicaciones, como reconocimiento de voz, traducción automática, 
# corrección ortográfica, generación de texto, entre otros.

# El objetivo principal de un PML es calcular la probabilidad de ocurrencia de una secuencia de palabras dada, lo que permite evaluar la fluidez y coherencia
# de dicha secuencia en el contexto del lenguaje. Esto es crucial en aplicaciones como la generación de texto, donde se busca producir oraciones gramaticalmente 
# correctas y con significado.

# Existen diferentes enfoques para construir un PML, y uno de ellos es mediante el uso de un corpus de texto. Un corpus es una colección grande de textos que se 
# utiliza como conjunto de entrenamiento para el modelo. La idea básica detrás de un PML basado en corpus es calcular la probabilidad de una secuencia de palabras 
# basándose en la frecuencia con la que ocurren esas palabras y secuencias similares en el corpus de entrenamiento.

# El modelo utiliza estadísticas recopiladas del corpus para estimar las probabilidades. Por ejemplo, puede calcular la probabilidad de una palabra dado un contexto 
# específico (modelo de bigramas) o incluso dado un contexto más amplio (modelo de trigramas o n-gramas en general). Esto se hace mediante el conteo de ocurrencias 
# de palabras y secuencias en el corpus y dividiendo por el número total de palabras o secuencias en el corpus.
#--------------- PROGRAMA --------------------------------------
import random

class PCFG:
    def __init__(self):
        self.rules = {}  # Diccionario para almacenar las reglas de producción y sus probabilidades

    def add_rule(self, non_terminal, production, probability):
        """
        Agrega una regla de producción con su respectiva probabilidad al diccionario de reglas.
        """
        if non_terminal in self.rules:
            self.rules[non_terminal].append((production, probability))
        else:
            self.rules[non_terminal] = [(production, probability)]

    def generate_sequence(self, symbol):
        """
        Genera una secuencia de acuerdo con la gramática probabilística.
        """
        if symbol not in self.rules:
            return symbol  # Si el símbolo no tiene reglas de producción, se devuelve tal cual

        productions, probabilities = zip(*self.rules[symbol])  # Separa las producciones y las probabilidades

        # Se elige una producción de acuerdo con sus probabilidades
        chosen_production = random.choices(productions, weights=probabilities)[0]

        # Se genera la secuencia recursivamente para cada símbolo en la producción
        sequence = ''
        for sym in chosen_production:
            sequence += self.generate_sequence(sym)

        return sequence

# Ejemplo de uso
if __name__ == "__main__":
    # Creamos una instancia de la PCFG
    pcfg = PCFG()

    # Definimos algunas reglas de producción con sus probabilidades
    pcfg.add_rule('S', ('NP', 'VP'), 0.7)
    pcfg.add_rule('S', ('Aux', 'NP', 'VP'), 0.3)
    pcfg.add_rule('NP', ('Det', 'N'), 0.5)
    pcfg.add_rule('NP', ('N',), 0.5)
    pcfg.add_rule('VP', ('V',), 1.0)
    pcfg.add_rule('Det', ('the',), 1.0)
    pcfg.add_rule('N', ('cat',), 0.5)
    pcfg.add_rule('N', ('dog',), 0.5)
    pcfg.add_rule('V', ('chased',), 1.0)
    pcfg.add_rule('Aux', ('did',), 1.0)

    # Generamos varias secuencias de acuerdo con la gramática
    for i in range(5):
        sequence = pcfg.generate_sequence('S')
        print(f"Secuencia {i + 1}: {sequence}")