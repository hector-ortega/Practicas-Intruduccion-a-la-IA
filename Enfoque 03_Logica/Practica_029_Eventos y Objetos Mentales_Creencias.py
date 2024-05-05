#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------

# La teoría de "Eventos y Objetos Mentales: Creencias" es una parte importante en la inteligencia artificial y la modelación cognitiva. 
# Se utiliza para representar y manejar el conocimiento sobre el mundo interno y externo de un agente inteligente. 

# Funcionamiento de un Algoritmo de Eventos y Objetos Mentales: Creencias

# 1.- Creación de Creencias:
# - Se definen creencias iniciales que representan el conocimiento inicial del agente sobre el mundo. Cada creencia tiene un nombre,
#   una descripción y un valor inicial (verdadero o falso).

# 2.-Modelado de Eventos:
# - Se definen eventos que representan cambios en el mundo que pueden afectar las creencias del agente. Cada evento tiene un nombre y 
#   puede estar asociado con uno o más efectos sobre las creencias.

# 3.- Actualización de Creencias por Eventos:
# - Cuando ocurre un evento, se actualizan las creencias relevantes afectadas por ese evento. La actualización puede implicar cambiar el 
#   valor de una creencia, agregar nuevas creencias o eliminar creencias existentes.

# 4.- Razonamiento y Toma de Decisiones:
# - Basándose en las creencias actuales y los eventos observados, el agente puede realizar razonamientos para inferir nuevas creencias o 
#   tomar decisiones sobre cómo actuar en su entorno.
#--------------- PROGRAMA ------------------------------------
class Creencia:
    def __init__(self, nombre, descripcion, valor):
        self.nombre = nombre  # Nombre de la creencia
        self.descripcion = descripcion  # Descripción de la creencia
        self.valor = valor  # Valor de la creencia (verdadero o falso)

    def actualizar_valor(self, nuevo_valor):
        self.valor = nuevo_valor  # Actualizar el valor de la creencia

class Evento:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre  # Nombre del evento
        self.descripcion = descripcion  # Descripción del evento

    def afectar_creencia(self, creencia, nuevo_valor):
        creencia.actualizar_valor(nuevo_valor)  # Actualizar la creencia afectada por el evento

# Crear algunas creencias iniciales
creencia1 = Creencia("Llueve", "Indica si está lloviendo", False)
creencia2 = Creencia("Tiene hambre", "Indica si tiene hambre", True)

# Crear un evento que cambie el valor de una creencia
evento1 = Evento("Comienza a llover", "Evento que indica que comienza a llover")
evento1.afectar_creencia(creencia1, True)  # El evento afecta la creencia "Llueve" y la establece en Verdadero

# Imprimir el estado actual de las creencias
print("Estado de las creencias después del evento:")
print(creencia1.nombre + ":", creencia1.valor)
print(creencia2.nombre + ":", creencia2.valor)

#-------------------------------------------------------------------
# 1.- Definimos una clase Creencia para representar una creencia con un nombre, una descripción y un valor (verdadero o falso).
# 2.- Definimos una clase Evento para representar un evento con un nombre y una descripción.
# 3.- Creamos instancias de creencias iniciales con valores predeterminados.
# 4.- Creamos un evento que puede afectar una creencia cambiando su valor.
# 5.- Utilizamos el evento para afectar una creencia específica y actualizar su valor.
# 6.- Imprimimos el estado actual de las creencias después de que se ha producido el evento.