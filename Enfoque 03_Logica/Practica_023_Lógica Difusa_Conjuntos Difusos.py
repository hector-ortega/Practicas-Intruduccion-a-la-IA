#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# La lógica difusa y los conjuntos difusos son herramientas utilizadas para modelar y manejar la incertidumbre y la imprecisión en el razonamiento.
# La lógica difusa extiende la lógica clásica, que solo permite valores de verdad binarios (verdadero o falso), para permitir valores de verdad
# en un continuo entre 0 y 1. Esto permite representar grados de verdad y tomar decisiones basadas en la incertidumbre y la imprecisión en los datos.

# Los conjuntos difusos son una aplicación directa de la lógica difusa y se utilizan para representar conjuntos en los que la pertenencia de un 
# elemento a ese conjunto no es definida de forma precisa, sino que se describe utilizando una función de pertenencia. La función de pertenencia
# asigna un valor entre 0 y 1 a cada elemento del universo, indicando en qué medida ese elemento pertenece al conjunto difuso.

# Funcionamiento:

# 1.- Funciones de Pertenencia:
# - Cada conjunto difuso está definido por una función de pertenencia que asigna un valor entre 0 y 1 a cada elemento del universo.
# - Esta función describe cómo se distribuye la pertenencia de los elementos en el conjunto difuso.

# 2.- Operaciones sobre Conjuntos Difusos:
# - Se pueden realizar operaciones como unión, intersección y complemento sobre conjuntos difusos utilizando operadores definidos en la lógica difusa.
# - Estas operaciones permiten combinar conjuntos difusos y realizar operaciones de lógica difusa.

# 3.- Inferencia Difusa:
# - La inferencia difusa es el proceso de derivar conclusiones a partir de premisas difusas utilizando reglas de inferencia difusa.
# - Se utilizan reglas difusas que especifican cómo combinar grados de pertenencia y lógica difusa para realizar inferencias basadas en información imprecisa.

#--------------- PROGRAMA ------------------------------------
class ConjuntoDifuso:
    """
    Clase que representa un conjunto difuso.
    """
    def __init__(self, nombre, a, b, c):
        self.nombre = nombre  # Nombre del conjunto
        self.a = a  # Punto de inicio de la función de pertenencia
        self.b = b  # Punto medio de la función de pertenencia
        self.c = c  # Punto final de la función de pertenencia

    def pertenencia(self, x):
        """
        Calcula el grado de pertenencia de un elemento x al conjunto difuso.
        """
        if x <= self.a or x >= self.c:
            return 0  # Si x está fuera del rango del conjunto difuso, su pertenencia es 0
        elif self.a < x <= self.b:
            return (x - self.a) / (self.b - self.a)  # Función de pertenencia creciente
        else:
            return (self.c - x) / (self.c - self.b)  # Función de pertenencia decreciente


# Creamos un conjunto difuso triangular llamado "Bajo" con una función de pertenencia triangular
bajo = ConjuntoDifuso("Bajo", 0, 25, 50)

# Calculamos el grado de pertenencia de un valor x al conjunto difuso "Bajo"
x = 20
grado_pertenencia = bajo.pertenencia(x)

# Imprimimos el resultado
print(f"El grado de pertenencia de {x} al conjunto difuso {bajo.nombre} es: {grado_pertenencia}")

#---------------------------------------------------------------------
# 1.- Definimos una clase ConjuntoDifuso que representa un conjunto difuso. Tiene un nombre y tres parámetros que definen la función de pertenencia triangular: a, b y c.
# 2.- La función pertenencia(x) calcula el grado de pertenencia de un valor x al conjunto difuso utilizando una función de pertenencia triangular. 
#     Esta función es 0 fuera del intervalo [a, c] y crece linealmente de a a b y decrece linealmente de b a c.
# 3.- Creamos un conjunto difuso triangular llamado "Bajo" con parámetros a = 0, b = 25 y c = 50.
# 4.- Calculamos el grado de pertenencia de un valor x = 20 al conjunto difuso "Bajo" utilizando el método pertenencia(x).
# 5.- Imprimimos el resultado que muestra el grado de pertenencia de x al conjunto difuso "Bajo".