#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# La lógica difusa es una extensión de la lógica clásica que permite manejar la incertidumbre y la imprecisión en el razonamiento.
# La inferencia difusa es el proceso de derivar conclusiones a partir de premisas difusas utilizando reglas difusas. Este tipo de inferencia 
# se utiliza en situaciones en las que la información disponible es incompleta o imprecisa, lo que hace que las decisiones basadas en la lógica
# clásica sean difíciles de aplicar.

# Funcionamiento:

# 1.- Definición de Conjuntos Difusos:
# - Se definen conjuntos difusos que representan variables de entrada y salida del sistema. Cada conjunto difuso tiene asociada una
#   función de pertenencia que indica en qué medida un elemento pertenece al conjunto.

# 2.- Definición de Reglas Difusas:
# - Se definen reglas difusas que establecen relaciones entre los conjuntos difusos de entrada y salida. Cada regla difusa tiene un 
#   antecedente y un consecuente, y se evalúa utilizando la lógica difusa.

# 3.- Inferencia Difusa:
# - Durante la inferencia difusa, se evalúa el grado de activación de cada regla difusa utilizando los valores de las variables de entrada y 
#   la función de pertenencia de los conjuntos difusos.
# - Se combinan los grados de activación de las reglas difusas para obtener el grado de pertenencia de los conjuntos difusos de salida.

# 4.- Defuzzificación (Opcional):
# - En algunos casos, es necesario convertir el resultado difuso en un valor concreto. Esto se hace a través de un proceso llamado defuzzificación,
#   que convierte el resultado difuso en un valor numérico que puede ser utilizado para tomar decisiones concretas.
#--------------- PROGRAMA ------------------------------------
class ConjuntoDifuso:
    """
    Clase que representa un conjunto difuso.
    """
    def __init__(self, nombre, funcion_pertenencia):
        self.nombre = nombre  # Nombre del conjunto
        self.funcion_pertenencia = funcion_pertenencia  # Función de pertenencia del conjunto

    def pertenencia(self, x):
        """
        Calcula el grado de pertenencia de un elemento x al conjunto difuso.
        """
        return self.funcion_pertenencia(x)


class ReglaDifusa:
    """
    Clase que representa una regla difusa.
    """
    def __init__(self, antecedente, consecuente):
        self.antecedente = antecedente  # Antecedente de la regla (conjunto difuso)
        self.consecuente = consecuente  # Consecuente de la regla (conjunto difuso)


class MotorInferenciaDifusa:
    """
    Clase que representa un motor de inferencia difusa.
    """
    def __init__(self, reglas):
        self.reglas = reglas  # Lista de reglas difusas

    def inferir(self, entrada):
        """
        Realiza la inferencia difusa para una entrada dada.
        """
        # Lista para almacenar los grados de pertenencia de los consecuentes
        grados_consecuentes = []

        # Itera sobre cada regla difusa
        for regla in self.reglas:
            # Calcula el grado de activación de la regla
            grado_activacion = min(regla.antecedente.pertenencia(entrada), regla.consecuente.pertenencia(entrada))
            # Agrega el grado de activación del consecuente de la regla a la lista
            grados_consecuentes.append(grado_activacion)

        # Calcula el grado de pertenencia final del conjunto difuso resultante
        grado_pertenencia_final = max(grados_consecuentes)

        return grado_pertenencia_final


# Definimos los conjuntos difusos de entrada y salida
entrada_frio = ConjuntoDifuso("Frio", lambda x: max(0, min(1, (20 - x) / 10)))
salida_apagar = ConjuntoDifuso("Apagar", lambda x: max(0, min(1, x / 50)))

# Definimos una regla difusa que relaciona los conjuntos difusos de entrada y salida
regla1 = ReglaDifusa(entrada_frio, salida_apagar)

# Creamos el motor de inferencia difusa con la lista de reglas
motor = MotorInferenciaDifusa([regla1])

# Realizamos una inferencia difusa para una temperatura de entrada específica
temperatura = 15
grado_pertenencia_final = motor.inferir(temperatura)

# Imprimimos el resultado de la inferencia difusa
print(f"Grado de pertenencia a 'Apagar' para una temperatura de {temperatura} grados: {grado_pertenencia_final}")

#------------------------------------------------------------------

# 1.- Definimos la clase ConjuntoDifuso que representa un conjunto difuso con un nombre y una función de pertenencia.
# 2.- Definimos la clase ReglaDifusa que representa una regla difusa con un antecedente y un consecuente, ambos conjuntos difusos.
# 3.- Definimos la clase MotorInferenciaDifusa que representa un motor de inferencia difusa, que toma una lista de reglas difusas como entrada.
# 4.- Creamos instancias de conjuntos difusos de entrada (entrada_frio) y salida (salida_apagar), y una regla difusa (regla1) que relaciona ambos conjuntos.
# 5.- Creamos una instancia del motor de inferencia difusa (motor) con la lista de reglas difusas.
# 6.- Realizamos una inferencia difusa para una temperatura de entrada específica (temperatura) y almacenamos el resultado en grado_pertenencia_final.
# 7.- Imprimimos el resultado de la inferencia difusa.