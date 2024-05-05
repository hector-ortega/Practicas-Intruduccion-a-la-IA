#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------

# El encadenamiento hacia adelante y hacia atrás son dos técnicas fundamentales en la resolución de problemas en la inteligencia artificial 
# y la lógica computacional. Estas técnicas se utilizan en sistemas de inferencia para deducir nuevas conclusiones o verificar si ciertos 
# objetivos pueden ser demostrados.

# Encadenamiento Hacia Adelante:
# El encadenamiento hacia adelante comienza con los hechos conocidos y aplica reglas para inferir nuevas conclusiones.
# Este proceso continúa iterativamente hasta que ya no se puedan inferir más conclusiones. Es útil para predecir el estado futuro de un 
# sistema o para derivar conclusiones a partir de un conjunto de datos inicial.

# Funcionamiento:

# 1.- Inicialización: Se comienza con un conjunto de hechos conocidos.
# 2.- Aplicación de reglas: Se aplican las reglas del sistema de inferencia a los hechos conocidos para inferir nuevas conclusiones. 
# Si todos los antecedentes de una regla están presentes en los hechos conocidos, se agrega el consecuente de la regla como nuevo hecho.
# 3.- Iteración: Se repite el proceso de aplicación de reglas hasta que ya no se puedan inferir más conclusiones.

# Encadenamiento Hacia Atrás:

# El encadenamiento hacia atrás comienza con un objetivo que se quiere demostrar y trata de encontrar hechos que lo apoyen. Este proceso retrocede 
# a través de las reglas del sistema de inferencia para verificar si los antecedentes de alguna regla implican el objetivo. Es útil para probar si 
# ciertos objetivos pueden ser alcanzados o demostrados a partir de un conjunto dado de reglas y hechos conocidos.

# Funcionamiento:

# 1.- Establecimiento del objetivo: Se define el objetivo que se quiere demostrar.
# 2.- Verificación de reglas: Se revisan las reglas del sistema de inferencia para encontrar aquellas cuyo consecuente coincida con el objetivo.
# 3.- Verificación de antecedentes: Para cada regla encontrada, se verifica si todos los antecedentes de la regla pueden ser demostrados 
#     recursivamente utilizando encadenamiento hacia atrás.
# 4.- Iteración: Se repite este proceso hasta que se encuentren hechos que apoyen el objetivo o hasta que se agoten todas las posibilidades.

#--------------- PROGRAMA ------------------------------------

class Regla:
    def __init__(self, antecedente, consecuente):
        self.antecedente = antecedente  # Lista de antecedentes de la regla
        self.consecuente = consecuente  # Consecuente de la regla

class SistemaInferencia:
    def __init__(self, reglas):
        self.reglas = reglas  # Lista de reglas del sistema
        self.hechos = set()   # Conjunto de hechos conocidos

    def encadenamiento_adelante(self):
        """
        Realiza un encadenamiento hacia adelante para inferir nuevas conclusiones.
        """
        nuevos_hechos = True  # Bandera para controlar si se agregaron nuevos hechos
        while nuevos_hechos:
            nuevos_hechos = False
            for regla in self.reglas:
                # Verificar si todos los antecedentes de la regla están en los hechos conocidos
                if all(antecedente in self.hechos for antecedente in regla.antecedente):
                    # Agregar el consecuente de la regla como nuevo hecho
                    if regla.consecuente not in self.hechos:
                        self.hechos.add(regla.consecuente)
                        print("Nuevo hecho inferido:", regla.consecuente)
                        nuevos_hechos = True

    def encadenamiento_atras(self, objetivo):
        """
        Realiza un encadenamiento hacia atrás para verificar si un objetivo puede ser demostrado.
        """
        if objetivo in self.hechos:
            print("El objetivo ya está demostrado.")
            return True
        for regla in self.reglas:
            if regla.consecuente == objetivo:
                print("Se utiliza la regla:", regla.antecedente, "->", regla.consecuente)
                # Verificar si todos los antecedentes de la regla se pueden demostrar
                if all(self.encadenamiento_atras(antecedente) for antecedente in regla.antecedente):
                    return True
        return False

# Definimos algunas reglas y hechos iniciales
reglas = [
    Regla(["p"], "q"),
    Regla(["q", "r"], "s"),
    Regla(["t"], "r")
]

hechos_conocidos = {"p", "t"}

# Creamos un sistema de inferencia y aplicamos encadenamiento hacia adelante
sistema = SistemaInferencia(reglas)
sistema.hechos = hechos_conocidos
print("Hechos conocidos inicialmente:", sistema.hechos)
sistema.encadenamiento_adelante()

# Probamos el encadenamiento hacia atrás para verificar si podemos demostrar el objetivo "s"
print("\nProbando encadenamiento hacia atrás para el objetivo 's':")
if sistema.encadenamiento_atras("s"):
    print("El objetivo 's' puede ser demostrado.")
else:
    print("El objetivo 's' no puede ser demostrado.")
    
#-----------------------------------------------------------------------------
# 1.- Creamos una clase Regla para representar una regla del sistema de inferencia. Cada regla tiene un antecedente 
#     (una lista de hechos que deben ser verdaderos) y un consecuente (el hecho que se deduce si se cumplen los antecedentes).
# 2.- Creamos una clase SistemaInferencia que representa el sistema de inferencia en sí. Tiene un conjunto de reglas y un conjunto de hechos conocidos.
# 3.- La función encadenamiento_adelante realiza un encadenamiento hacia adelante, iterando sobre las reglas y verificando si todos los antecedentes
#     de una regla están en los hechos conocidos. Si es así, agrega el consecuente de la regla como nuevo hecho.
# 4.- La función encadenamiento_atras realiza un encadenamiento hacia atrás para verificar si un objetivo dado puede ser demostrado. 
#     Comienza verificando si el objetivo ya está en los hechos conocidos. Si no es así, busca una regla cuyo consecuente coincida con el objetivo y 
#     verifica si todos los antecedentes de esa regla pueden ser demostrados recursivamente.
# 5.- En el ejemplo de uso, definimos algunas reglas y hechos conocidos, creamos un sistema de inferencia y aplicamos encadenamiento hacia adelante.
#     Luego, probamos el encadenamiento hacia atrás para verificar si podemos demostrar el objetivo "s".