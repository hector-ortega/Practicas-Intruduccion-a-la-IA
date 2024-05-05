#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# La lógica difusa, también conocida como lógica borrosa, es un enfoque computacional que permite manejar la incertidumbre
# y la imprecisión en los sistemas que modelan variables que no son binarias o que no tienen límites claros entre las diferentes categorías.
# En lugar de asignar valores binarios como verdadero o falso, la lógica difusa asigna grados de pertenencia a cada categoría. Este enfoque
# es útil cuando se trata con conceptos humanos vagos o ambiguos, como "caliente" o "frío", "rápido" o "lento", "alto" o "bajo".

# 1.- Variables de entrada y salida: Un algoritmo de lógica difusa comienza con la definición de las variables de entrada y salida del sistema.
#     Por ejemplo, si estamos modelando la calidad del aire, las variables de entrada pueden ser la concentración de contaminantes y la humedad,
#     mientras que la variable de salida puede ser la calidad del aire, expresada en términos de "mala", "aceptable" o "buena".
# 2.- Funciones de membresía: Para cada variable (tanto de entrada como de salida), se definen funciones de membresía que asignan un grado de 
#     pertenencia a cada categoría. Estas funciones pueden ser de diferentes formas, como triangular, trapezoidal, gaussiana, etc. Por ejemplo, 
#         en el caso de la temperatura, podríamos tener funciones de membresía para "frío", "templado" y "caliente".
# 3.- Reglas difusas: Se definen reglas difusas que relacionan las variables de entrada con la variable de salida. Estas reglas establecen qué 
#     acción tomar en función de las condiciones de las variables de entrada. Por ejemplo, "si la temperatura es fría y la humedad es alta, 
#     entonces la calidad del aire es mala".
# 4.- Inferencia difusa: Se utiliza un proceso de inferencia difusa para calcular el grado de pertenencia de la variable de salida
#     para cada regla difusa, teniendo en cuenta las funciones de membresía de las variables de entrada y las reglas difusas definidas.
#     Este proceso puede ser realizado utilizando diferentes métodos, como la lógica de Mamdani o la lógica de Takagi-Sugeno.
# 5.- Defuzzificación: Finalmente, se aplica un proceso de defuzzificación para convertir los resultados difusos en un valor nítido o una
#     decisión concreta. Este proceso puede ser tan simple como tomar el valor máximo de pertenencia o utilizar métodos más sofisticados
#     como el centro de gravedad.

#--------------- PROGRAMA ------------------------------------
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Definimos las variables de entrada y salida del sistema difuso
temperatura = ctrl.Antecedent(np.arange(0, 101, 1), 'temperatura')
calidad = ctrl.Consequent(np.arange(0, 11, 1), 'calidad')

# Definimos las funciones de membresía para la temperatura
temperatura['frío'] = fuzz.trimf(temperatura.universe, [0, 0, 50])
temperatura['templado'] = fuzz.trimf(temperatura.universe, [20, 50, 80])
temperatura['caliente'] = fuzz.trimf(temperatura.universe, [50, 100, 100])

# Definimos las funciones de membresía para la calidad
calidad['mala'] = fuzz.trimf(calidad.universe, [0, 0, 5])
calidad['aceptable'] = fuzz.trimf(calidad.universe, [0, 5, 10])
calidad['buena'] = fuzz.trimf(calidad.universe, [5, 10, 10])

# Visualizamos las funciones de membresía
temperatura.view()
calidad.view()

# Definimos las reglas del sistema difuso
regla1 = ctrl.Rule(temperatura['frío'], calidad['mala'])
regla2 = ctrl.Rule(temperatura['templado'], calidad['aceptable'])
regla3 = ctrl.Rule(temperatura['caliente'], calidad['buena'])

# Creamos el sistema de control difuso
sistema_ctrl = ctrl.ControlSystem([regla1, regla2, regla3])
sistema = ctrl.ControlSystemSimulation(sistema_ctrl)

# Asignamos un valor de temperatura al sistema
sistema.input['temperatura'] = 78

# Evaluamos el sistema
sistema.compute()

# Imprimimos el resultado
print("Calidad:", sistema.output['calidad'])
calidad.view(sim=sistema)

#---------------------------------------------------------------------
# 1.- Importamos las bibliotecas necesarias: numpy para operaciones numéricas, scikit-fuzzy para lógica difusa y control de scikit-fuzzy para controlar el sistema difuso.
# 2.- Definimos las variables de entrada (temperatura) y salida (calidad) del sistema difuso.
# 3.- Definimos las funciones de membresía para la temperatura y la calidad utilizando funciones triangulares.
# 4.- Visualizamos las funciones de membresía para la temperatura y la calidad.
# 5.- Definimos las reglas del sistema difuso. En este caso, si la temperatura es fría, la calidad es mala; si la temperatura es templada, la calidad es aceptable; si la temperatura es caliente, la calidad es buena.
# 6.- Creamos el sistema de control difuso y lo simulamos con un valor de temperatura de 78.
# 7.- Evaluamos el sistema difuso.
# 8.- Imprimimos y visualizamos el resultado de la calidad.