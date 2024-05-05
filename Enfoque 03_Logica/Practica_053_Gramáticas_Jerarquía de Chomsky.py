#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------

# La jerarquía de Chomsky es una clasificación de las gramáticas formales propuesta por el lingüista Noam Chomsky en la década de 1950.
# Esta jerarquía organiza las gramáticas según su poder expresivo y la estructura de las reglas de producción que las componen.
# Está compuesta por cuatro tipos de gramáticas, cada una de las cuales es capaz de generar un conjunto específico de lenguajes formales.

# Aquí está una descripción de cada tipo de gramática en la jerarquía de Chomsky, de menor a mayor poder expresivo:

# 1.- Tipo 3 (Regular):
# - También conocidas como gramáticas regulares o gramáticas de tipo 3, son las menos potentes en la jerarquía de Chomsky.
# - Sus reglas de producción tienen la forma A → αB o A → α, donde A y B son símbolos no terminales, α es una cadena de símbolos terminales o no terminales,
#   y la longitud de α no excede uno.
# - Los lenguajes regulares son aquellos que pueden ser generados por una gramática de tipo 3.
# - Se utilizan para modelar lenguajes regulares, como expresiones regulares y autómatas finitos.

# 2.- Tipo 2 (Libre de Contexto):
# - También conocidas como gramáticas libres de contexto o gramáticas de tipo 2, son más expresivas que las gramáticas regulares.
# - Sus reglas de producción tienen la forma A → α, donde A es un símbolo no terminal y α es una cadena de símbolos terminales y no terminales.
# - Los lenguajes libres de contexto son aquellos que pueden ser generados por una gramática de tipo 2.
# - Se utilizan para modelar estructuras sintácticas simples, como la gramática de un lenguaje de programación o la estructura de un documento XML.

# 3.- Tipo 1 (Sensible al Contexto):
# - También conocidas como gramáticas sensibles al contexto o gramáticas de tipo 1, son más expresivas que las gramáticas libres de contexto.
# - Sus reglas de producción tienen la forma αAβ → αγβ, donde α, β y γ son cadenas de símbolos terminales y no terminales, y al menos uno de ellos
#   no puede ser una cadena vacía.
# - Los lenguajes sensibles al contexto son aquellos que pueden ser generados por una gramática de tipo 1.
# - Se utilizan en aplicaciones donde la estructura del lenguaje depende del contexto, como en algunos lenguajes naturales y en la síntesis de lenguaje natural.

# 4.- Tipo 0 (Irrestringida):
# - También conocidas como gramáticas irrestrictas o gramáticas de tipo 0, son las más expresivas en la jerarquía de Chomsky.
# - No imponen restricciones en las reglas de producción.
# - Pueden generar cualquier lenguaje formal.
# - Se utilizan en la descripción de lenguajes naturales complejos y en la teoría de la computación.

#--------------- PROGRAMA ------------------------------------
import random

class Tipo0Gramatica:
    def __init__(self, reglas):
        self.reglas = reglas

    def generar_cadena(self):
        regla = random.choice(self.reglas)  # Selecciona una regla aleatoria
        cadena = regla[1]  # La cadena inicial es la parte derecha de la regla seleccionada
        while True:
            nueva_cadena = ""
            for simbolo in cadena:
                if simbolo in self.reglas:
                    nueva_cadena += random.choice(self.reglas[simbolo])  # Sustituye símbolos no terminales según las reglas
                else:
                    nueva_cadena += simbolo  # Mantén los símbolos terminales sin cambios
            if nueva_cadena == cadena:
                break  # Detener si la cadena no cambia después de una iteración
            cadena = nueva_cadena  # Actualizar la cadena para la próxima iteración
        return cadena

class Tipo1Gramatica:
    def __init__(self, reglas):
        self.reglas = reglas

    def generar_cadena(self):
        cadena = "$"  # Símbolo inicial
        while True:
            nueva_cadena = ""
            for i in range(len(cadena)):
                if cadena[i] in self.reglas:
                    regla = random.choice(self.reglas[cadena[i]])  # Selecciona una regla para el símbolo no terminal
                    if len(regla[1]) <= len(cadena) - i:
                        nueva_cadena += regla[1]  # Agrega la parte derecha de la regla si cabe en la cadena
                    else:
                        nueva_cadena += cadena[i]  # Mantén el símbolo no terminal si no hay espacio suficiente
                else:
                    nueva_cadena += cadena[i]  # Mantén los símbolos terminales sin cambios
            if nueva_cadena == cadena:
                break  # Detener si la cadena no cambia después de una iteración
            cadena = nueva_cadena  # Actualizar la cadena para la próxima iteración
        return cadena[1:]  # Eliminar el símbolo inicial "$" al final

class Tipo2Gramatica:
    def __init__(self, reglas):
        self.reglas = reglas

    def generar_cadena(self):
        cadena = "$"  # Símbolo inicial
        while True:
            nueva_cadena = ""
            for simbolo in cadena:
                if simbolo in self.reglas:
                    nueva_cadena += random.choice(self.reglas[simbolo])  # Sustituye símbolos no terminales según las reglas
                else:
                    nueva_cadena += simbolo  # Mantén los símbolos terminales sin cambios
            if nueva_cadena == cadena:
                break  # Detener si la cadena no cambia después de una iteración
            cadena = nueva_cadena  # Actualizar la cadena para la próxima iteración
        return cadena[1:]  # Eliminar el símbolo inicial "$" al final

class Tipo3Gramatica:
    def __init__(self, reglas):
        self.reglas = reglas

    def generar_cadena(self):
        cadena = "$"  # Símbolo inicial
        while True:
            nueva_cadena = ""
            for simbolo in cadena:
                if simbolo in self.reglas:
                    nueva_cadena += random.choice(self.reglas[simbolo])  # Sustituye símbolos no terminales según las reglas
                else:
                    nueva_cadena += simbolo  # Mantén los símbolos terminales sin cambios
            if nueva_cadena == cadena:
                break  # Detener si la cadena no cambia después de una iteración
            cadena = nueva_cadena  # Actualizar la cadena para la próxima iteración
        return cadena[1:]  # Eliminar el símbolo inicial "$" al final

# Ejemplo de uso
def main():
    # Definir reglas para cada tipo de gramática
    tipo0_reglas = {'S': ['aS', 'b']}
    tipo1_reglas = {'S': [('aA', 'Aa'), ('bB', 'Bb')], 'A': [('aA', 'Aa'), ('bB', 'Bb'), ('a', 'a')], 'B': [('bB', 'Bb'), ('a', 'a')]}
    tipo2_reglas = {'S': ['aSb', 'bSa', 'a', 'b']}
    tipo3_reglas = {'S': ['aS', 'b']}

    # Crear gramáticas
    tipo0_gramatica = Tipo0Gramatica(tipo0_reglas)
    tipo1_gramatica = Tipo1Gramatica(tipo1_reglas)
    tipo2_gramatica = Tipo2Gramatica(tipo2_reglas)
    tipo3_gramatica = Tipo3Gramatica(tipo3_reglas)

    # Generar y mostrar cadenas para cada tipo de gramática
    print("Tipo 0:", tipo0_gramatica.generar_cadena())
    print("Tipo 1:", tipo1_gramatica.generar_cadena())
    print("Tipo 2:", tipo2_gramatica.generar_cadena())
    print("Tipo 3:", tipo3_gramatica.generar_cadena())

if __name__ == "__main__":
    main()

#---------------------------------------------------------------------------
# Este código consta de cuatro clases, una para cada tipo de gramática de la jerarquía de Chomsky: Tipo 0, Tipo 1, Tipo 2 y Tipo 3. 
# Cada clase tiene un método generar_cadena() que genera una cadena válida según las reglas de la gramática correspondiente.

# - En el caso de la clase Tipo0Gramatica, se selecciona una regla aleatoria y se aplica a la cadena hasta que no se realicen más sustituciones.
# - Para las clases Tipo1Gramatica, Tipo2Gramatica y Tipo3Gramatica, se va construyendo la cadena aplicando reglas de sustitución de acuerdo
#   con las reglas definidas para cada tipo de gramática.
# - La función main() muestra ejemplos de cadenas generadas para cada tipo de gramática.
