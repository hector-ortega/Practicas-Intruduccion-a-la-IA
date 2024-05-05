#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# La teoría detrás de los algoritmos de Equivalencia, Validez y Satisfacibilidad está enraizada en la lógica proposicional,
# que es una rama de la lógica que se centra en el estudio de proposiciones o afirmaciones que pueden ser verdaderas o falsas.

# ¿Cómo funcionan los algoritmos?

# 1.- Equivalencia: Para verificar la equivalencia entre dos expresiones lógicas, se pueden comparar todas las posibles combinaciones
#     de valores de verdad de las variables involucradas en ambas expresiones. Si los resultados son los mismos para todas las 
#     combinaciones, entonces las expresiones son equivalentes.
# 2.- Validez: Para verificar la validez de una expresión lógica, se puede usar el método de tabla de verdad. Si todas las filas de la
#     tabla de verdad de la expresión tienen un valor de verdad verdadero en la columna final, entonces la expresión es válida.
# 3.- Satisfacibilidad: Para verificar la satisfacibilidad de una expresión lógica, se pueden generar todas las posibles combinaciones 
#     de valores de verdad de las variables proposicionales y evaluar la expresión en cada una de estas combinaciones. 
#     Si al menos una de estas evaluaciones resulta en un valor de verdad verdadero, entonces la expresión es satisfacible.
#--------------- PROGRAMA ------------------------------------
import sympy as sp

class LogicaProposicional:
    def __init__(self):
        pass

    def verificar_equivalencia(self, expresion1, expresion2):
        """Verifica si dos expresiones lógicas son equivalentes."""
        expr1 = sp.sympify(expresion1)  # Convertir expresión a objeto sympy
        expr2 = sp.sympify(expresion2)  # Convertir expresión a objeto sympy
        return sp.Equivalent(expr1, expr2)

    def verificar_validez(self, expresion):
        """Verifica si una expresión lógica es válida (verdadera en todas las interpretaciones)."""
        expr = sp.sympify(expresion)  # Convertir expresión a objeto sympy
        return sp.satisfiable(expr)

    def verificar_satisfacibilidad(self, expresion):
        """Verifica si una expresión lógica es satisfacible (al menos una interpretación la hace verdadera)."""
        expr = sp.sympify(expresion)  # Convertir expresión a objeto sympy
        return sp.satisfiable(expr)

# Crear una instancia de la clase LogicaProposicional
lp = LogicaProposicional()

# Verificar equivalencia entre dos expresiones
expresion1 = "P and Q"
expresion2 = "Q and P"
print("¿Las expresiones", expresion1, "y", expresion2, "son equivalentes?")
print(lp.verificar_equivalencia(expresion1, expresion2))

# Verificar validez de una expresión
expresion = "P or not P"
print("¿La expresión", expresion, "es válida?")
print(lp.verificar_validez(expresion))

# Verificar satisfacibilidad de una expresión
expresion = "P and Q"
print("¿La expresión", expresion, "es satisfacible?")
print(lp.verificar_satisfacibilidad(expresion))

#-----------------------------------------------------------------
# 1.- importamos la biblioteca sympy para trabajar con expresiones simbólicas y lógicas.
# 2.- Definimos una clase LogicaProposicional que contendrá los métodos para verificar la equivalencia, validez y 
#     satisfacibilidad de expresiones lógicas.
# 3.- En el método verificar_equivalencia, convertimos las expresiones lógicas dadas en objetos sympy, y luego usamos 
#     la función Equivalent de sympy para verificar si son equivalentes.
# 4.- En el método verificar_validez, convertimos la expresión lógica dada en un objeto sympy, y luego usamos la función 
#     satisfiable de sympy para verificar si es válida (es decir, si es verdadera en todas las interpretaciones).
# 5.- En el método verificar_satisfacibilidad, convertimos la expresión lógica dada en un objeto sympy, y luego usamos la 
#     función satisfiable de sympy para verificar si es satisfacible (es decir, si al menos una interpretación la hace verdadera).
# 6.- Creamos una instancia de la clase LogicaProposicional.
# 7.- Probamos los métodos de la clase con algunas expresiones lógicas y mostramos los resultados.