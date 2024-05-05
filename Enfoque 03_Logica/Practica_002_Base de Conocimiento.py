#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# un algoritmo de Base de Conocimiento es una herramienta poderosa para representar, almacenar y razonar sobre el conocimiento 
# en un dominio específico. Permite a las máquinas capturar y utilizar el conocimiento humano de manera automatizada, lo que
# tiene numerosas aplicaciones en inteligencia artificial, sistemas expertos, y otros campos relacionados.

# ¿Cómo funciona un algoritmo de Base de Conocimiento?

# 1.- Representación del conocimiento: El primer paso es definir cómo se va a representar el conocimiento en la base de conocimiento. 
#     Esto puede incluir la especificación de hechos simples, reglas lógicas o cualquier otra información relevante para el dominio.
# 2.- Almacenamiento de datos: Una vez que se ha definido la representación del conocimiento, se procede a almacenar los datos en la 
#     base de conocimiento. Esto puede implicar la creación de estructuras de datos adecuadas para contener los hechos y reglas.
# 3.- Razonamiento: El corazón de un algoritmo de BC es el proceso de razonamiento. Esto implica la aplicación de reglas de inferencia 
#     para derivar nuevas conclusiones a partir de los hechos existentes en la base de conocimiento. Dependiendo del tipo de algoritmo 
#     y la representación del conocimiento, el razonamiento puede ser deductivo, inductivo o probabilístico.
# 4.- Consultas: Los usuarios pueden realizar consultas a la base de conocimiento para obtener información específica o hacer preguntas
#     sobre el dominio. Esto implica buscar hechos que coincidan con ciertos criterios o aplicar reglas para responder a las consultas 
#     de manera automatizada.
# 5.- Actualización del conocimiento: Las bases de conocimiento suelen ser dinámicas y pueden ser actualizadas con nuevos hechos o 
#     reglas a medida que se adquiere más información sobre el dominio. Los algoritmos de BC deben ser capaces de manejar estas 
#     actualizaciones de manera eficiente.
#--------------- PROGRAMA ------------------------------------
class BaseConocimiento:
    def __init__(self):
        self.hechos = []

    def agregar_hecho(self, hecho):
        """Agrega un hecho a la base de conocimiento."""
        self.hechos.append(hecho)

    def consultar(self, hecho):
        """Consulta si un hecho está en la base de conocimiento."""
        return hecho in self.hechos

# Crear una instancia de la base de conocimiento
bc = BaseConocimiento()

# Agregar algunos hechos
bc.agregar_hecho("El cielo es azul")
bc.agregar_hecho("El sol es caliente")
bc.agregar_hecho("El agua es líquida")

# Consultar algunos hechos
print("¿El cielo es azul?", bc.consultar("El cielo es azul"))
print("¿La tierra es plana?", bc.consultar("La tierra es plana"))

#--------------------------------------------------------------------
# 1.- class BaseConocimiento:: Definimos una clase llamada BaseConocimiento para representar nuestra base de conocimiento.
# 2.- def __init__(self):: El método __init__ se llama cuando se crea una nueva instancia de la clase. Aquí inicializamos la lista de hechos.
# 3.- self.hechos = []: Creamos una lista vacía para almacenar los hechos.
# 4.- def agregar_hecho(self, hecho):: Definimos un método llamado agregar_hecho para agregar un hecho a la base de conocimiento.
# 5.- self.hechos.append(hecho): Agregamos el hecho dado a la lista de hechos.
# 6.- def consultar(self, hecho):: Definimos un método llamado consultar para consultar si un hecho está en la base de conocimiento.
# 7.- eturn hecho in self.hechos: Devolvemos True si el hecho está en la lista de hechos, False en caso contrario.
# 8.- bc = BaseConocimiento(): Creamos una instancia de la clase BaseConocimiento.
# 9.- bc.agregar_hecho("El cielo es azul"): Agregamos algunos hechos a la base de conocimiento.
# 10.- bc.agregar_hecho("El sol es caliente"): Agregamos más hechos.
# 11.- bc.agregar_hecho("El agua es líquida"): Agregamos otro hecho.
# 12.- print("¿El cielo es azul?", bc.consultar("El cielo es azul")): Consultamos si el cielo es azul e imprimimos el resultado.
# 13.- print("¿La tierra es plana?", bc.consultar("La tierra es plana")): Consultamos si la tierra es plana e imprimimos el resultado.