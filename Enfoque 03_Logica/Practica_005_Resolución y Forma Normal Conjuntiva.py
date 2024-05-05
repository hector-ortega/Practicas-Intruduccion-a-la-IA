#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# Resolución

# La resolución es un método de inferencia utilizado en lógica proposicional para deducir nuevas cláusulas lógicas a partir 
# de cláusulas existentes. Es una técnica completa y refutacional, lo que significa que si hay una refutación para una 
# expresión lógica, la resolución eventualmente la encontrará. Se basa en el principio de la resolución refutacional de la
# lógica de predicados, que afirma que para probar una fórmula, es suficiente probar su negación.

# El algoritmo de resolución procede eliminando variables en las cláusulas hasta que se derive una contradicción.
# Se realiza utilizando el siguiente proceso:

# 1.- Forma de Cláusulas: Primero, las expresiones lógicas se convierten a una forma normal conjuntiva (FNC) y luego a cláusulas disyuntivas.
# 2.- Unificación: Se aplica la unificación para encontrar instancias de literales que puedan ser resueltos juntos.
# 3.- Resolución: Se aplican reglas de resolución para deducir nuevas cláusulas. La resolución se realiza entre dos cláusulas que
#     contienen literales complementarios.
# 4.- Iteración: Se repite el proceso hasta que se obtenga una cláusula vacía, lo que indica una contradicción, o hasta que ya no se 
#     puedan derivar nuevas cláusulas.

# Forma Normal Conjuntiva (FNC)

# La forma normal conjuntiva (FNC) es una forma normal en la que una expresión lógica se representa como una conjunción de 
# disyunciones de literales. En FNC, una expresión lógica se representa como una conjunción de cláusulas, donde cada cláusula 
# es una disyunción de literales. La conversión a FNC es importante porque simplifica la expresión y facilita su manipulación y análisis.

# El proceso de conversión a FNC implica los siguientes pasos:

# 1.- Eliminación de implicaciones: Se reescribe la expresión lógica utilizando equivalencias lógicas para eliminar las implicaciones.
# 2.- Forma Normal Negativa (FNN): Se convierte la expresión en FNN, lo que implica mover las negaciones hacia el interior de la fórmula 
#     utilizando las leyes de De Morgan.
# 3.- Distribución: Se distribuyen las conjunciones sobre las disyunciones para obtener la FNC, aplicando la propiedad distributiva.
#--------------- PROGRAMA ------------------------------------
import sympy as sp

class ResolucionFNC:
    def __init__(self):
        pass

    def resolver(self, clausulas):
        """Resuelve cláusulas utilizando el método de resolución."""
        clausulas = [sp.Or(*c) for c in clausulas]  # Convertir a expresiones disyuntivas
        return sp.satisfiable(sp.And(*clausulas))

    def convertir_a_fnc(self, expresion):
        """Convierte una expresión lógica a Forma Normal Conjuntiva (FNC)."""
        expr = sp.to_cnf(expresion, True)  # Convertir a FNC
        return expr

# Crear una instancia de la clase ResolucionFNC
rfnc = ResolucionFNC()

# Ejemplo de resolución
clausulas = [["P", "Q"], ["~P", "R"], ["Q", "~R"]]
print("Resolución:", rfnc.resolver(clausulas))

# Ejemplo de conversión a FNC
expresion = "((P | Q) & (~P | R) & (Q | ~R))"
print("Expresión original:", expresion)
print("Forma Normal Conjuntiva:", rfnc.convertir_a_fnc(expresion))

#-------------------------------------------------------------------------
# 1.- Importamos la biblioteca sympy para trabajar con expresiones lógicas simbólicas.
# 2.- Definimos una clase ResolucionFNC que contendrá métodos para resolver cláusulas utilizando el método de resolución 
#     y para convertir expresiones a Forma Normal Conjuntiva.
# 3.- En el método resolver, convertimos las cláusulas a expresiones disyuntivas y luego usamos la función satisfiable de 
#     sympy para verificar si la conjunción de estas cláusulas es satisfacible.
# 4.- En el método convertir_a_fnc, utilizamos la función to_cnf de sympy para convertir una expresión lógica a Forma Normal Conjuntiva.
# 5.- Creamos una instancia de la clase ResolucionFNC.
# 6.- Probamos los métodos de la clase con ejemplos de resolución y conversión a FNC y mostramos los resultados.