#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------

# El algoritmo de Iteración de Políticas es una técnica utilizada en la resolución de problemas de toma de decisiones de Markov (MDP) 
# para encontrar la política óptima. Un MDP es un modelo matemático para la toma de decisiones en situaciones donde los resultados son parcialmente 
# aleatorios y parcialmente controlados por las decisiones tomadas por un agente. El objetivo del agente es encontrar la secuencia de acciones que maximice 
# su recompensa esperada a largo plazo.

# La política en un MDP es una estrategia que determina qué acción debe tomar el agente en cada estado del entorno.
# La política óptima es aquella que maximiza la recompensa esperada para el agente. El algoritmo de Iteración de Políticas busca encontrar
# esta política óptima directamente, iterando sobre todas las posibles políticas hasta converger a la mejor opción.
#--------------- PROGRAMA ------------------------------------   
import numpy as np

class IteracionPoliticas:
    def __init__(self, estados, acciones, recompensas, probabilidades_transicion, factor_descuento=0.9, epsilon=1e-6):
        self.estados = estados  # Lista de estados
        self.acciones = acciones  # Lista de acciones
        self.recompensas = recompensas  # Matriz de recompensas
        self.probabilidades_transicion = probabilidades_transicion  # Matriz de probabilidades de transición
        self.factor_descuento = factor_descuento  # Factor de descuento para futuras recompensas
        self.epsilon = epsilon  # Umbral de convergencia

        # Inicializar la política aleatoria
        self.politica = {estado: np.random.choice(acciones) for estado in estados}

    def iteracion_politicas(self):
        # Iterar hasta que la política converja
        while True:
            delta = 0  # Inicializar el cambio máximo en la política en esta iteración

            # Iterar sobre todos los estados
            for estado in self.estados:
                accion_anterior = self.politica[estado]  # Acción anterior para el estado
                mejor_accion = None  # Mejor acción encontrada para el estado
                mejor_valor = float('-inf')  # Mejor valor encontrado para el estado

                # Iterar sobre todas las acciones posibles
                for accion in self.acciones:
                    valor = 0  # Valor acumulado para la acción
                    
                    # Calcular el valor esperado para la acción
                    for proximo_estado in self.estados:
                        valor += self.probabilidades_transicion[estado, accion, proximo_estado] * (
                            self.recompensas[estado, accion, proximo_estado] + 
                            self.factor_descuento * self.obtener_valor_estado(proximo_estado)
                        )

                    # Actualizar la mejor acción y valor encontrado
                    if valor > mejor_valor:
                        mejor_accion = accion
                        mejor_valor = valor

                # Actualizar la política del estado
                self.politica[estado] = mejor_accion
                
                # Calcular el cambio en la política
                delta = max(delta, abs(accion_anterior - mejor_accion))

            # Verificar si la convergencia alcanzada
            if delta < self.epsilon:
                break

        return self.politica

    def obtener_valor_estado(self, estado):
        # Obtener el valor esperado para un estado dado su política actual
        return self.recompensas[estado, self.politica[estado], :].mean()

# Ejemplo de uso
estados = [0, 1, 2]  # Lista de estados
acciones = [0, 1]  # Lista de acciones
recompensas = np.array([[[0, 0, 1], [0, 1, 0]], [[0, 0, 1], [0, 1, 0]], [[1, 0, 0], [0, 0, 0]]])  # Matriz de recompensas
probabilidades_transicion = np.array([[[0.8, 0.2, 0], [0.4, 0.6, 0]], [[0.8, 0.2, 0], [0, 0.4, 0.6]], [[0, 1, 0], [0, 1, 0]]])  # Matriz de probabilidades de transición

# Crear una instancia del algoritmo Iteración de Políticas
ip = IteracionPoliticas(estados, acciones, recompensas, probabilidades_transicion)

# Ejecutar el algoritmo Iteración de Políticas
politica_final = ip.iteracion_politicas()
print("Política Final:")
print(politica_final)