#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# El modelo de Manto de Markov es una herramienta fundamental en la modelización de procesos estocásticos donde las probabilidades 
# de transición entre estados dependen únicamente del estado actual y no de los estados anteriores. Se utiliza en una amplia gama de aplicaciones, 
# desde el modelado del clima hasta la predicción del lenguaje natural. 

# Funcionamiento de un Modelo de Manto de Markov:
# Definición de Estados y Transiciones: En un modelo de Manto de Markov, se define un conjunto de estados y las probabilidades de transición entre ellos.
# Cada estado representa una situación o condición y las transiciones representan cómo se mueve el sistema de un estado a otro.
# Probabilidades de Transición: Las probabilidades de transición especifican la probabilidad de pasar de un estado a otro. Estas probabilidades se representan 
# mediante una matriz de transición, donde cada entrada indica la probabilidad de transición de un estado a otro.
# Proceso de Generación o Predicción: Para generar secuencias o hacer predicciones, el modelo de Manto de Markov utiliza las probabilidades de transición para
# calcular la siguiente etapa o estado en función del estado actual.
# Estacionariedad: Un aspecto importante de los modelos de Manto de Markov es que pueden exhibir una propiedad llamada estacionariedad, donde las probabilidades 
# de transición no cambian con el tiempo. Esto significa que el comportamiento del sistema se mantiene constante independientemente del tiempo transcurrido.
#--------------- PROGRAMA ------------------------------------
import random

class ModeloMantoMarkov:
    def __init__(self):
        self.transiciones = {}  # Diccionario para almacenar las transiciones de palabras
        
    def entrenar(self, secuencia):
        for i in range(len(secuencia) - 1):
            palabra_actual = secuencia[i]
            palabra_siguiente = secuencia[i + 1]
            if palabra_actual not in self.transiciones:
                self.transiciones[palabra_actual] = {}
            if palabra_siguiente not in self.transiciones[palabra_actual]:
                self.transiciones[palabra_actual][palabra_siguiente] = 0
            self.transiciones[palabra_actual][palabra_siguiente] += 1
    
    def predecir(self, palabra_actual):
        if palabra_actual not in self.transiciones:
            return None
        posibles_siguientes_palabras = self.transiciones[palabra_actual]
        total_ocurrencias = sum(posibles_siguientes_palabras.values())
        probabilidad_acumulada = 0
        aleatorio = random.uniform(0, 1)
        for palabra, frecuencia in posibles_siguientes_palabras.items():
            probabilidad = frecuencia / total_ocurrencias
            probabilidad_acumulada += probabilidad
            if aleatorio < probabilidad_acumulada:
                return palabra

# Ejemplo de uso
secuencia_palabras = ["el", "gato", "estaba", "sobre", "la", "mesa", "el", "perro", "estaba", "bajo", "la", "mesa"]
modelo = ModeloMantoMarkov()
modelo.entrenar(secuencia_palabras)

palabra_inicial = "la"
palabra_siguiente = modelo.predecir(palabra_inicial)
print("Siguiente palabra después de '{}': {}".format(palabra_inicial, palabra_siguiente))
#----------------------------------------------------------------------------------------------------------------
# 1.-Definimos una clase ModeloMantoMarkov para representar nuestro modelo de Manto de Markov.
# 2.- El método entrenar recorre la secuencia de palabras y cuenta las transiciones de palabras, es decir, cuántas veces una palabra sigue a otra en la secuencia.
# 3.- El método predecir toma una palabra actual y devuelve la siguiente palabra basada en las transiciones de palabras observadas durante el entrenamiento.
# 4.- Creamos una instancia del modelo, lo entrenamos con una secuencia de palabras y realizamos una predicción de la siguiente palabra dada una palabra inicial.
# 5.- Imprimimos la palabra predicha.