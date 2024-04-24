#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# El algoritmo de Iteración de Valores es una técnica utilizada en teoría de la decisión y en la resolución de problemas de inteligencia 
# artificial para encontrar la política óptima en un proceso de toma de decisiones de Markov (MDP). Su propósito principal es calcular la 
# función de valor de cada estado en un entorno determinista o estocástico.
#--------------- PROGRAMA ------------------------------------   
import numpy as np

class IteracionValores:
    def __init__(self, estados, acciones, recompensas, probabilidades_transicion, factor_descuento=0.9, epsilon=1e-6):
        self.estados = estados  # Lista de estados
        self.acciones = acciones  # Lista de acciones
        self.recompensas = recompensas  # Matriz de recompensas
        self.probabilidades_transicion = probabilidades_transicion  # Matriz de probabilidades de transición
        self.factor_descuento = factor_descuento  # Factor de descuento para futuras recompensas
        self.epsilon = epsilon  # Umbral de convergencia

        # Inicializar la función de valor
        self.funcion_valor = {estado: 0 for estado in estados}

    def iteracion_valores(self):
        # Iterar hasta que la función de valor converja
        while True:
            delta = 0  # Inicializar el cambio máximo en la función de valor en esta iteración

            # Iterar sobre todos los estados
            for estado in self.estados:
                valor_anterior = self.funcion_valor[estado]  # Valor anterior del estado
                mejor_valor = float('-inf')  # Mejor valor encontrado para el estado

                # Iterar sobre todas las acciones posibles
                for accion in self.acciones:
                    valor = 0  # Valor acumulado para la acción
                    
                    # Calcular el valor esperado para la acción
                    for proximo_estado in self.estados:
                        valor += self.probabilidades_transicion[estado, accion, proximo_estado] * (
                            self.recompensas[estado, accion, proximo_estado] + 
                            self.factor_descuento * self.funcion_valor[proximo_estado]
                        )

                    # Actualizar el mejor valor encontrado para el estado
                    mejor_valor = max(mejor_valor, valor)

                # Actualizar la función de valor del estado
                self.funcion_valor[estado] = mejor_valor
                
                # Calcular el cambio en la función de valor
                delta = max(delta, abs(valor_anterior - mejor_valor))

            # Verificar si la convergencia alcanzada
            if delta < self.epsilon:
                break

        return self.funcion_valor

# Ejemplo de uso
estados = [0, 1, 2]  # Lista de estados
acciones = [0, 1]  # Lista de acciones
recompensas = np.array([[[0, 0, 1], [0, 1, 0]], [[0, 0, 1], [0, 1, 0]], [[1, 0, 0], [0, 0, 0]]])  # Matriz de recompensas
probabilidades_transicion = np.array([[[0.8, 0.2, 0], [0.4, 0.6, 0]], [[0.8, 0.2, 0], [0, 0.4, 0.6]], [[0, 1, 0], [0, 1, 0]]])  # Matriz de probabilidades de transición

# Crear una instancia del algoritmo Iteración de Valores
iv = IteracionValores(estados, acciones, recompensas, probabilidades_transicion)

# Ejecutar el algoritmo Iteración de Valores
funcion_valor_final = iv.iteracion_valores()
print("Función de Valor Final:")
print(funcion_valor_final)