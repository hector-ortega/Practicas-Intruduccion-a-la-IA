#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# Funcionamiento de un Algoritmo de Acciones, Situaciones y Eventos: Marcos:

# 1.- Definición de Marcos:
# - Se definen los marcos principales para cada tipo de entidad (acción, situación, evento), especificando las propiedades 
#   y relaciones relevantes que deben contener.

# 2.- Creación de Instancias de Marcos:
# - Se crean instancias específicas de marcos para representar acciones, situaciones y eventos concretos, proporcionando valores para 
#   las propiedades definidas en los marcos principales.

# 3.- Organización Jerárquica:
# - Los marcos se organizan en una estructura jerárquica, con marcos principales en la parte superior y submarcos que representan instancias
#   específicas en niveles inferiores.

# 4.- Manipulación y Razonamiento:
# - Los sistemas de IA pueden acceder, modificar y razonar sobre los marcos para realizar diversas tareas, como inferir información, tomar decisiones 
#   y entender situaciones y eventos en un contexto más amplio.
#--------------- PROGRAMA ------------------------------------
class Accion:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre  # Nombre de la acción
        self.descripcion = descripcion  # Descripción de la acción

class Situacion:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre  # Nombre de la situación
        self.descripcion = descripcion  # Descripción de la situación
        self.acciones = []  # Lista de acciones asociadas a esta situación

    def agregar_accion(self, accion):
        self.acciones.append(accion)  # Agregar una acción a la lista de acciones de la situación

class Evento:
    def __init__(self, nombre, descripcion, situacion):
        self.nombre = nombre  # Nombre del evento
        self.descripcion = descripcion  # Descripción del evento
        self.situacion = situacion  # Situación asociada al evento

# Crear algunas acciones
accion1 = Accion("Correr", "Moverse rápidamente usando las piernas")
accion2 = Accion("Saltar", "Elevarse en el aire usando las piernas")

# Crear algunas situaciones y asociarles acciones
situacion1 = Situacion("Parque", "Espacio abierto con áreas verdes")
situacion1.agregar_accion(accion1)
situacion1.agregar_accion(accion2)

# Crear algunos eventos asociados a situaciones
evento1 = Evento("Carrera en el parque", "Competencia de correr en el parque", situacion1)

# Imprimir información sobre el evento
print("Evento:", evento1.nombre)
print("Descripción:", evento1.descripcion)
print("Situación:", evento1.situacion.nombre)
print("Descripción de la situación:", evento1.situacion.descripcion)
print("Acciones asociadas a la situación:")
for accion in evento1.situacion.acciones:
    print("-", accion.nombre, ":", accion.descripcion)

#--------------------------------------------------------------------------
# 1.- Definimos una clase Accion para representar una acción con un nombre y una descripción.
# 2.- Definimos una clase Situacion para representar una situación con un nombre, una descripción y una lista de acciones asociadas.
# 3.- Definimos una clase Evento para representar un evento con un nombre, una descripción y una situación asociada.
# 4.- Creamos instancias de acciones, situaciones y eventos.
# 5.- Asociamos acciones a situaciones utilizando el método agregar_accion de la clase Situacion.
# 6.- Imprimimos información sobre el evento, incluyendo el nombre, la descripción, la situación asociada y las acciones asociadas a esa situación.