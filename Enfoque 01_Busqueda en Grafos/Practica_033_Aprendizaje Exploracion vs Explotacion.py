#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# El concepto de exploración vs. explotación es fundamental en el campo del aprendizaje por refuerzo y se utiliza para abordar 
# el dilema de decidir entre acciones que se conocen y que han dado buenos resultados en el pasado (explotación) y acciones que
# podrían llevar a descubrir nuevas oportunidades o mejorar el rendimiento a largo plazo (exploración).

# ¿Cómo funciona?
# Cuando un agente interactúa con un entorno, tiene que decidir entre dos estrategias:

# .- Explotación: Esta estrategia consiste en seleccionar acciones que se sabe que son efectivas con base en la información 
# disponible hasta el momento. El agente elige la opción con el mayor valor conocido, lo que optimiza el rendimiento a corto plazo.
# .- Exploración: Por otro lado, la exploración implica probar nuevas acciones o opciones para recolectar más información sobre el entorno 
# y posiblemente descubrir estrategias más efectivas a largo plazo. Esto puede implicar elegir una opción que no se ha probado mucho o 
# seleccionar aleatoriamente entre todas las opciones posibles.
# El desafío radica en encontrar un equilibrio entre estas dos estrategias para maximizar la recompensa total acumulada a lo largo del tiempo.
#--------------- PROGRAMA ------------------------------------
import numpy as np

class ExplorationExploitation:
    def __init__(self, num_options, exploration_rate):
        """
        Constructor de la clase ExplorationExploitation.
        
        Args:
            num_options (int): Número de opciones disponibles.
            exploration_rate (float): Tasa de exploración ε.
        """
        self.num_options = num_options
        self.exploration_rate = exploration_rate

    def select_option(self):
        """
        Método para seleccionar una opción basada en la política de exploración vs. explotación.
        
        Returns:
            int: Opción seleccionada por el agente.
        """
        if np.random.uniform(0, 1) < self.exploration_rate:
            # Exploración: seleccionamos una opción aleatoria
            return np.random.randint(0, self.num_options)
        else:
            # Explotación: seleccionamos la opción con el mayor valor
            return np.argmax(self.option_values)

# Crear instancia del agente de exploración vs. explotación
num_options = 5  # Número de opciones disponibles
exploration_rate = 0.2  # Tasa de exploración ε

agent = ExplorationExploitation(num_options, exploration_rate)

# Simular múltiples selecciones de opciones por parte del agente
num_selections = 1000
option_counts = np.zeros(num_options)

for _ in range(num_selections):
    option = agent.select_option()
    option_counts[option] += 1

# Imprimir la frecuencia de selección de cada opción
print("Frecuencia de selección de opciones:")
for i in range(num_options):
    print("Opción", i, ":", option_counts[i])

# Calcular la tasa de exploración vs. explotación
exploration_count = sum(option_counts) * exploration_rate
exploitation_count = sum(option_counts) - exploration_count

print("\nTotal de selecciones:")
print("Exploración:", exploration_count)
print("Explotación:", exploitation_count)

#-------------------------------------------------------------------------------------
# 1.- Importamos la biblioteca numpy para realizar cálculos numéricos eficientes.
# 2.- Definimos la clase ExplorationExploitation, que representa el agente que debe tomar decisiones entre explorar nuevas opciones o explotar las opciones conocidas.
# 3.- En el constructor __init__, inicializamos el número de opciones disponibles y la tasa de exploración ε.
# 4.- Implementamos el método select_option, que selecciona una opción basada en la política de exploración vs. explotación.
#     Si un número aleatorio generado está por debajo de la tasa de exploración ε, el agente realiza una exploración y elige una opción aleatoria.
#     De lo contrario, el agente realiza una explotación y selecciona la opción con el mayor valor conocido.
# 5.- Creamos una instancia del agente ExplorationExploitation con el número de opciones y la tasa de exploración especificados.
# 6.- Simulamos múltiples selecciones de opciones por parte del agente y registramos la frecuencia de selección de cada opción.
# 7.- Imprimimos la frecuencia de selección de cada opción, así como el total de selecciones realizadas para exploración y explotación.