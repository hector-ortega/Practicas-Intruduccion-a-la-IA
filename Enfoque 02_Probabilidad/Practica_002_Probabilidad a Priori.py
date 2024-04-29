#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# La probabilidad a priori es una medida de incertidumbre que representa nuestras creencias o conocimientos previos sobre un evento 
# antes de observar cualquier evidencia. Los algoritmos de probabilidad a priori se utilizan en una variedad de aplicaciones donde 
# es importante tener en cuenta la información inicial disponible antes de procesar nuevos datos o evidencia.

# A continuación, te explicaré con más detalle la teoría detrás de la probabilidad a priori y cómo se utiliza:

# Teoría:
# 1.- Probabilidad a priori: La probabilidad a priori se denota como 
# P(A) y representa la probabilidad de que ocurra un evento A antes de tener en cuenta cualquier evidencia adicional. 
# Es una medida subjetiva que refleja nuestras creencias o conocimientos previos sobre el evento. La probabilidad a
# priori puede basarse en experiencias pasadas, conocimientos expertos o simplemente en intuiciones.

# 2.- Teorema de Bayes: El teorema de Bayes es una herramienta fundamental en la teoría de probabilidad que nos permite actualizar 
# nuestras creencias a priori en función de nueva evidencia observada. Matemáticamente, el teorema de Bayes se expresa como:

# P(A|B) = (P(B|A) X P(A))/P(B)
# Donde:
# P(A|B) es la probabilad posterior de que ocurra el evento A dada la evidencia B
# P(B|A) es la probabilidad de que ocurra la evidencia B dado que el evento A ha ocurrido
# P(A) es la probabilidad a priori del evento A
# P(B) es la probabilidad de que ocurra la evidencia B independientemente de si el evento A ocurre o no

# 3.- Actualización de probabilidades a priori: Utilizando el teorema de Bayes, podemos actualizar nuestras probabilidades a priori 
# en función de la nueva evidencia observada. Esto nos permite obtener probabilidades a posteriori más precisas y actualizadas sobre los eventos de interés.
#--------------- PROGRAMA ------------------------------------
import random

# Definimos la clase Moneda para representar una moneda
class Moneda:
    def __init__(self, probabilidad_cara):
        self.probabilidad_cara = probabilidad_cara

    # Método para lanzar la moneda
    def lanzar_moneda(self):
        if random.random() < self.probabilidad_cara:
            return 'Cara'  # Si el número aleatorio generado es menor que la probabilidad de cara, retorna 'Cara'
        else:
            return 'Sello' # Si no, retorna 'Sello'

# Función para actualizar la probabilidad a priori
def actualizar_probabilidad_a_priori(probabilidad_previa, resultado_lanzamiento, probabilidad_cara):
    if resultado_lanzamiento == 'Cara':
        # Si el resultado del lanzamiento es 'Cara', actualizamos la probabilidad multiplicándola por la probabilidad de cara
        return (probabilidad_previa * probabilidad_cara)
    else:
        # Si el resultado del lanzamiento es 'Sello', no hay evidencia de que la moneda esté cargada,
        # así que simplemente retornamos la probabilidad previa sin cambios
        return probabilidad_previa

# Probabilidad a priori de que la moneda esté cargada
probabilidad_a_priori = 0.5
# Probabilidad de que salga cara en una moneda justa
probabilidad_cara = 0.5

# Creamos una instancia de la clase Moneda
moneda = Moneda(probabilidad_cara)

# Realizamos algunos lanzamientos de la moneda y actualizamos la probabilidad a priori en cada iteración
for _ in range(10):
    # Lanzamos la moneda
    resultado_lanzamiento = moneda.lanzar_moneda()
    # Actualizamos la probabilidad a priori basada en el resultado del lanzamiento
    probabilidad_a_priori = actualizar_probabilidad_a_priori(probabilidad_a_priori, resultado_lanzamiento, probabilidad_cara)
    # Imprimimos la probabilidad a priori actualizada
    print("Probabilidad a priori de que la moneda esté cargada:", probabilidad_a_priori)

#--------------------------------------------------------------------------------------------------------
# 1.-import random: Importamos el módulo random de Python para generar números aleatorios.
# 2.-Definimos la clase Moneda para representar una moneda. La clase tiene un atributo probabilidad_cara que representa 
# la probabilidad de que la moneda salga cara.
# 3.-En el método lanzar_moneda(), simulamos el lanzamiento de la moneda generando un número aleatorio entre 0 y 1.
# Si este número es menor que la probabilidad de cara, retornamos 'Cara'; de lo contrario, retornamos 'Sello'.
# 4.-Definimos la función actualizar_probabilidad_a_priori() para actualizar la probabilidad a priori basada en el 
# resultado del lanzamiento de la moneda. Si el resultado es 'Cara', multiplicamos la probabilidad previa por la probabilidad de cara; 
# si es 'Sello', dejamos la probabilidad previa sin cambios.
# 5.-Inicializamos la probabilidad a priori probabilidad_a_priori en 0.5, ya que no tenemos información previa sobre si la moneda está cargada o no.
# 6.-Inicializamos la probabilidad de que la moneda salga cara en probabilidad_cara en 0.5, ya que estamos considerando una moneda justa.
# 7.-Creamos una instancia de la clase Moneda con la probabilidad de cara especificada.
# 8.-Realizamos 10 lanzamientos de la moneda en un bucle for.
# 9.-En cada iteración del bucle, lanzamos la moneda, actualizamos la probabilidad a priori y luego imprimimos la probabilidad a priori actualizada.
# 10.-Este algoritmo simula lanzamientos de una moneda y actualiza la probabilidad a priori sobre si la moneda está cargada o no en función
# de los resultados observados, lo que demuestra cómo se puede utilizar la probabilidad a priori en un contexto de inteligencia artificial.
# Puedes ejecutar este código en Python y observar cómo cambia la probabilidad a priori a medida que se realizan más lanzamientos de la moneda.