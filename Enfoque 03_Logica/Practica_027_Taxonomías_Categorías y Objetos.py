#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# Una taxonomía es una estructura jerárquica que organiza conceptos en categorías y subcategorías basadas en sus similitudes y relaciones. 
# Se utiliza para clasificar y organizar la información de manera que sea más fácil de entender y buscar. En el contexto de la inteligencia
# artificial y la ingeniería del conocimiento, las taxonomías son fundamentales para organizar y representar el conocimiento de un dominio específico.

# Funcionamiento de un Algoritmo de Taxonomías:

# Definición de Categorías y Subcategorías:
# Se definen las categorías principales y, opcionalmente, las subcategorías que formarán la taxonomía. Cada categoría puede tener atributos como nombre,
# descripción, relaciones con otras categorías, etc.

# Asignación de Objetos a Categorías:
# Se asignan objetos individuales a las categorías correspondientes según sus características y relaciones con las categorías en la taxonomía.

# Navegación y Consulta:
# Los usuarios pueden navegar por la taxonomía, explorando las categorías y subcategorías para encontrar la información que necesitan.
# También pueden realizar consultas para buscar objetos específicos dentro de la taxonomía.

# Actualización y Mantenimiento:
# La taxonomía puede actualizarse y modificarse según sea necesario para reflejar cambios en el conocimiento o en el dominio que representa. 
# Esto puede implicar agregar nuevas categorías, eliminar categorías obsoletas o actualizar relaciones entre categorías.
#--------------- PROGRAMA ------------------------------------
class Categoria:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre  # Nombre de la categoría
        self.descripcion = descripcion  # Descripción de la categoría
        self.objetos = []  # Lista de objetos pertenecientes a esta categoría

    def agregar_objeto(self, objeto):
        self.objetos.append(objeto)  # Agregar un objeto a la lista de objetos de la categoría

class Objeto:
    def __init__(self, nombre, descripcion, categoria):
        self.nombre = nombre  # Nombre del objeto
        self.descripcion = descripcion  # Descripción del objeto
        self.categoria = categoria  # Categoría a la que pertenece el objeto

# Crear algunas categorías
categoria1 = Categoria("Electrónica", "Productos electrónicos")
categoria2 = Categoria("Muebles", "Muebles para el hogar")

# Crear algunos objetos y asignarlos a las categorías
objeto1 = Objeto("Smartphone", "Teléfono inteligente", categoria1)
objeto2 = Objeto("Silla", "Silla de comedor", categoria2)
objeto3 = Objeto("Laptop", "Computadora portátil", categoria1)

# Agregar objetos a las categorías
categoria1.agregar_objeto(objeto1)
categoria2.agregar_objeto(objeto2)
categoria1.agregar_objeto(objeto3)

# Mostrar información sobre las categorías y los objetos
print("Categoría:", categoria1.nombre)
print("Descripción:", categoria1.descripcion)
print("Objetos:")
for objeto in categoria1.objetos:
    print("-", objeto.nombre)

print("\nCategoría:", categoria2.nombre)
print("Descripción:", categoria2.descripcion)
print("Objetos:")
for objeto in categoria2.objetos:
    print("-", objeto.nombre)

#-----------------------------------------------------------------------

# 1.- Definimos una clase Categoria que tiene un constructor __init__ para inicializar el nombre, la descripción y la lista de objetos de la categoría. 
#     También tiene un método agregar_objeto para agregar objetos a la lista de la categoría.
# 2.- Definimos una clase Objeto que tiene un constructor __init__ para inicializar el nombre, la descripción y la categoría del objeto.
# 3.- Creamos algunas instancias de Categoria y Objeto para representar las categorías y los objetos.
# 4.- Asignamos los objetos a las categorías correspondientes.
# 5.- Imprimimos la información sobre las categorías y los objetos.