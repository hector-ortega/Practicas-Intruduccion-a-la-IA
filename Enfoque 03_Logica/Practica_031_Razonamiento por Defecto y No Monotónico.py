#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# El razonamiento por defecto y no monotónico es un enfoque en inteligencia artificial y lógica que permite tomar decisiones y sacar 
# conclusiones incluso en situaciones donde la información disponible es incompleta o sujeta a cambios. Este tipo de razonamiento se utiliza
# para modelar el pensamiento humano, que a menudo opera con suposiciones incompletas y está sujeto a revisiones en función de nuevas evidencias.

# Funcionamiento del Razonamiento por Defecto y No Monotónico:

# 1.- Suposiciones Iniciales:
# - Se parte de un conjunto de suposiciones iniciales o creencias sobre el mundo, que pueden estar incompletas o ser parciales.

# 2.- Inferencia Tentativa:
# - Se realiza una inferencia inicial basada en las suposiciones disponibles, lo que puede llevar a conclusiones provisionales o tentativas.

# 3.- Revisión de Conclusiones:
# - A medida que se adquiere nueva información, se revisan las conclusiones provisionales en función de esta información adicional. 
#   Si la nueva información contradice las conclusiones existentes, estas pueden ser revisadas o modificadas.

# 4.- Actualización Continua:
# - El proceso de razonamiento es continuo y adaptativo, ya que las conclusiones pueden ser revisadas y actualizadas a medida que se adquiere
#   nueva información o se detectan cambios en el entorno.
#--------------- PROGRAMA ------------------------------------

class BaseConocimiento:
    def __init__(self):
        self.hechos = set()  # Conjunto de hechos conocidos
        self.reglas = []      # Lista de reglas conocidas

    def agregar_hecho(self, hecho):
        self.hechos.add(hecho)

    def agregar_regla(self, regla):
        self.reglas.append(regla)

    def razonar(self, hecho_nuevo):
        # Verificar si el nuevo hecho contradice un hecho conocido
        if hecho_nuevo in self.hechos:
            print("El hecho ya es conocido:", hecho_nuevo)
            return

        # Verificar si el nuevo hecho contradice una regla
        for regla in self.reglas:
            if hecho_nuevo in regla.consecuente and not regla.evaluar(self.hechos):
                print("El hecho contradice la regla:", regla)
                return

        # Agregar el nuevo hecho a la base de conocimiento
        self.hechos.add(hecho_nuevo)
        print("Nuevo hecho agregado a la base de conocimiento:", hecho_nuevo)

class Regla:
    def __init__(self, antecedente, consecuente):
        self.antecedente = antecedente  # Condiciones que deben cumplirse para aplicar la regla
        self.consecuente = consecuente  # Hecho que se concluye si se cumplen las condiciones

    def evaluar(self, hechos):
        # Verificar si se cumplen las condiciones del antecedente
        for condicion in self.antecedente:
            if condicion not in hechos:
                return False  # La regla no se aplica si alguna condición no se cumple
        return True  # Todas las condiciones se cumplen, por lo que la regla se puede aplicar

# Crear una base de conocimiento
bc = BaseConocimiento()

# Definir algunas reglas y hechos iniciales
regla1 = Regla(["puede_volar"], "es_un_ave")
bc.agregar_regla(regla1)

regla2 = Regla(["es_un_ave"], "tiene_plumas")
bc.agregar_regla(regla2)

# Agregar algunos hechos iniciales a la base de conocimiento
bc.agregar_hecho("puede_volar")
bc.agregar_hecho("tiene_plumas")

# Intentar agregar un nuevo hecho que contradice una regla
bc.razonar("no_es_un_ave")

# Intentar agregar un nuevo hecho que ya es conocido
bc.razonar("puede_volar")
#.-------------------------------------------------------------
# 1.- La clase BaseConocimiento representa la base de conocimiento del sistema, que contiene hechos y reglas.
# 2.- La clase Regla define una regla con un antecedente y un consecuente.
# 3.- El método razonar en la clase BaseConocimiento intenta agregar un nuevo hecho a la base de conocimiento, 
#     pero primero verifica si contradice algún hecho conocido o alguna regla.
# 4.- Se definen algunas reglas y hechos iniciales, y luego se intenta agregar un nuevo hecho que contradice una regla y otro que ya es conocido.