#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------

# La teoría de "Reglas, Redes Semánticas y Lógica Descriptiva" es una parte importante en el campo de la inteligencia artificial y la 
# representación del conocimiento. Estas herramientas se utilizan para modelar y razonar sobre el conocimiento de un sistema inteligente.

# Funcionamiento de un Algoritmo de Reglas, Redes Semánticas y Lógica Descriptiva

# 1.- Representación del Conocimiento:
# - Se define un conjunto de reglas que establecen condiciones y acciones, una red semántica que describe las relaciones entre los objetos,
#   y lógica descriptiva que describe propiedades y restricciones sobre el dominio.

# 2.- Inferencia y Razonamiento:
# - El sistema aplica las reglas de inferencia para derivar nuevas conclusiones a partir de las reglas existentes y los hechos conocidos. 
#   También utiliza la red semántica para navegar entre los objetos y relaciones, y la lógica descriptiva para realizar consultas sobre el conocimiento.

# 3.- Toma de Decisiones:
# - Basado en las conclusiones derivadas y el conocimiento representado, el sistema toma decisiones sobre cómo actuar en una situación dada. 
#   Esto puede implicar seleccionar la mejor acción posible o generar recomendaciones para el usuario.

# 4.- Actualización del Conocimiento:
# - A medida que el sistema interactúa con su entorno y recibe nueva información, actualiza su conocimiento mediante la aplicación
#   de reglas de actualización y modificando la red semántica según sea necesario.
#--------------- PROGRAMA ------------------------------------
class Regla:
    def __init__(self, antecedente, consecuente):
        self.antecedente = antecedente  # Condiciones que deben cumplirse para aplicar la regla
        self.consecuente = consecuente  # Acción que se ejecuta si se cumplen las condiciones

    def evaluar(self, hechos):
        # Verificar si se cumplen las condiciones del antecedente
        for condicion in self.antecedente:
            if condicion not in hechos:
                return False  # La regla no se aplica si alguna condición no se cumple
        return True  # Todas las condiciones se cumplen, por lo que la regla se puede aplicar

class RedSemantica:
    def __init__(self):
        self.relaciones = {}

    def agregar_relacion(self, objeto1, relacion, objeto2):
        if objeto1 not in self.relaciones:
            self.relaciones[objeto1] = {}
        self.relaciones[objeto1][relacion] = objeto2

    def obtener_relacion(self, objeto1, relacion):
        if objeto1 in self.relaciones and relacion in self.relaciones[objeto1]:
            return self.relaciones[objeto1][relacion]
        return None

# Definir algunas reglas y relaciones en una red semántica
regla1 = Regla(["llueve"], "llevar_paraguas")
red_semantica = RedSemantica()
red_semantica.agregar_relacion("llueve", "implica", "llevar_paraguas")

# Definir los hechos iniciales
hechos = {"llueve": True}

# Evaluar las reglas para tomar decisiones
for regla in [regla1]:
    if regla.evaluar(hechos):
        print("Se cumple la regla:", regla.consecuente)

# Obtener información de la red semántica
relacion = red_semantica.obtener_relacion("llueve", "implica")
if relacion:
    print("La lluvia implica:", relacion)
else:
    print("No se encontró una relación para la lluvia")

#------------------------------------------------------------
# 1.- Definimos una clase Regla que representa una regla con un antecedente (condiciones que deben cumplirse) 
#     y un consecuente (acción que se ejecuta si se cumplen las condiciones).
# 2.- Creamos un método evaluar en la clase Regla para verificar si se cumplen las condiciones del antecedente.
# 3.- Definimos una clase RedSemantica que representa una red semántica con relaciones entre objetos.
# 4.- Creamos métodos para agregar relaciones y obtener relaciones en la clase RedSemantica.
# 5.- Definimos algunas reglas y relaciones en una instancia de RedSemantica.
# 6.- Definimos hechos iniciales que representan el estado inicial del sistema.
# 7.- Evaluamos las reglas para tomar decisiones basadas en los hechos.
# 8.- Obtenemos información de la red semántica para realizar razonamiento.