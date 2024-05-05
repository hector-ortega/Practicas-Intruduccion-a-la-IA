#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.
#-----------------TEORIA----------------------------------------
# Un Modelo Probabilístico del Lenguaje (MPL) es una herramienta utilizada en el procesamiento del lenguaje natural (PLN) para modelar la probabilidad 
# de ocurrencia de secuencias de palabras en un texto. El objetivo principal de un MPL es capturar y estimar la estructura subyacente del lenguaje natural, 
# lo que permite predecir la probabilidad de palabras o secuencias de palabras dentro de un contexto dado.

# La idea central detrás de un MPL es que las palabras en un texto no ocurren de manera aleatoria, sino que están influenciadas por las palabras que las rodean,
# es decir, su contexto. Por lo tanto, un MPL utiliza estadísticas de ocurrencia de palabras y secuencias de palabras en un corpus de entrenamiento para estimar 
# la probabilidad de que una palabra específica aparezca en un contexto dado.

# El corpus, en este contexto, se refiere a un conjunto de textos que se utilizan para entrenar el modelo de lenguaje. Puede ser cualquier conjunto de documentos,
# libros, artículos, conversaciones, etc., que representen el dominio del lenguaje que se está modelando.

# El proceso general para construir un MPL utilizando un corpus de texto implica los siguientes pasos:

# 1.- Tokenización: Se divide el texto en unidades más pequeñas, como palabras o caracteres. Esto permite al modelo entender la estructura del texto.
# 2.- Generación de N-gramas: Se crean secuencias de n palabras consecutivas a partir del texto tokenizado. Estas secuencias se conocen como n-gramas.
# 3.- Conteo de N-gramas y Contextos: Se cuentan las ocurrencias de cada n-grama y se almacenan en una estructura de datos adecuada. Además, se cuentan 
# los contextos de cada n-grama, que son todas las palabras en el n-grama excepto la última.
# 4.- Estimación de Probabilidades: Utilizando los recuentos de n-gramas y contextos, se calculan las probabilidades condicionales de ocurrencia de palabras
# dadas las palabras anteriores.
# 5.- Uso del Modelo: Una vez entrenado el modelo, se puede utilizar para predecir la probabilidad de una palabra o secuencia de palabras dadas las palabras anteriores.
#--------------- PROGRAMA --------------------------------------
import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from collections import defaultdict

class LanguageModel:
    def __init__(self, n):
        """
        Inicializa el modelo de lenguaje con el tamaño del n-grama.

        Args:
        n (int): El tamaño del n-grama.
        """
        self.n = n
        self.ngram_counts = defaultdict(int)  # Diccionario para almacenar los recuentos de n-gramas
        self.context_counts = defaultdict(int)  # Diccionario para almacenar los recuentos de contextos

    def train(self, corpus):
        """
        Entrena el modelo de lenguaje con un corpus de texto.

        Args:
        corpus (str): El texto del corpus.
        """
        # Tokenización del texto en palabras
        tokens = word_tokenize(corpus.lower())  # Convertimos todo a minúsculas para evitar la distinción entre mayúsculas y minúsculas

        # Generación de n-gramas
        ngrams_list = list(ngrams(tokens, self.n, pad_left=True, pad_right=True))

        # Conteo de n-gramas y contextos
        for ngram in ngrams_list:
            context = tuple(ngram[:-1])  # El contexto es todo el n-grama excepto la última palabra
            self.context_counts[context] += 1
            self.ngram_counts[ngram] += 1

    def probability(self, word, context):
        """
        Calcula la probabilidad de una palabra dado un contexto utilizando el modelo de lenguaje.

        Args:
        word (str): La palabra de interés.
        context (tuple): El contexto de la palabra como una tupla de palabras.

        Returns:
        float: La probabilidad de la palabra dado el contexto.
        """
        context = tuple(context)
        context_count = self.context_counts[context]
        if context_count == 0:
            return 0  # Si el contexto no está en el corpus, la probabilidad es cero
        else:
            ngram = context + (word,)
            ngram_count = self.ngram_counts[ngram]
            return ngram_count / context_count

# Ejemplo de uso
corpus = "El gato está en el tejado. El tejado es alto. El gato es negro."
lm = LanguageModel(n=2)
lm.train(corpus)

# Calculamos la probabilidad de una palabra dada un contexto
word = "gato"
context = ("el",)
print(f"La probabilidad de la palabra '{word}' dado el contexto '{' '.join(context)}' es:")
print(lm.probability(word, context))

#--------------------------------------------------------------------------
# Este código define una clase LanguageModel que representa un modelo de lenguaje basado en n-gramas. Aquí hay una 
# explicación detallada de cada parte del código:

# Inicialización: En el método __init__, se inicializa el modelo de lenguaje con el tamaño del n-grama especificado.
# Entrenamiento: El método train se encarga de entrenar el modelo de lenguaje con un corpus de texto. Primero, 
# se tokeniza el texto en palabras utilizando la biblioteca NLTK. Luego, se generan los n-gramas utilizando la función ngrams de NLTK. 
# Finalmente, se cuentan los n-gramas y los contextos (todo el n-grama excepto la última palabra) y se almacenan en diccionarios.
# Cálculo de Probabilidad: El método probability calcula la probabilidad de una palabra dada un contexto utilizando el modelo de lenguaje
# entrenado. La probabilidad se calcula dividiendo el recuento del n-grama por el recuento del contexto.
# Ejemplo de Uso: Se muestra un ejemplo de uso del modelo de lenguaje entrenado. Calculamos la probabilidad de la palabra "gato"
#  dado el contexto "el".