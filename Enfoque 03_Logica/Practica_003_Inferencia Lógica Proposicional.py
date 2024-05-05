#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# La inferencia lógica proposicional es un proceso fundamental en el campo de la lógica y la inteligencia artificial. 
# Consiste en deducir nuevas proposiciones a partir de proposiciones existentes utilizando reglas de inferencia.
# Este proceso es esencial para el razonamiento automatizado y la toma de decisiones en sistemas basados en conocimiento.

# ¿Cómo funciona un algoritmo de inferencia lógica proposicional?

# 1.- Representación del conocimiento: El primer paso es representar el conocimiento relevante en términos de proposiciones lógicas.
#      Esto implica identificar hechos y definir reglas que describan relaciones entre ellos.
# 2.- Definición de reglas de inferencia: Se definen reglas de inferencia que especifican cómo deducir nuevas proposiciones a 
#     partir de proposiciones existentes. Por ejemplo, el Modus Ponens es una regla de inferencia común que establece que si tenemos 
#     una implicación "si P entonces Q", y sabemos que P es verdadero, entonces podemos inferir que Q es verdadero.
# 3.- Aplicación de reglas de inferencia: Se aplican las reglas de inferencia para deducir nuevas proposiciones a partir de proposiciones
#     existentes. Esto se hace utilizando técnicas como la búsqueda de coincidencias, la unificación y la resolución.
# 4.- Validación de conclusiones: Se validan las conclusiones deducidas para asegurar que sean lógicamente consistentes y coherentes con el 
#     conocimiento previo. Esto puede implicar verificar la validez de las reglas de inferencia utilizadas y comprobar si las conclusiones 
#     son consistentes con los hechos conocidos.
# 5.- Actualización del conocimiento: A medida que se deducen nuevas proposiciones, se actualiza el conjunto de conocimientos disponibles. 
#     Esto puede incluir agregar nuevas proposiciones inferidas a la base de conocimiento y modificar reglas existentes en función de 
#     nuevas observaciones.
#--------------- PROGRAMA ------------------------------------
class InferenciaLogicaProposicional:
    def __init__(self):
        self.reglas = []

    def agregar_regla(self, antecedente, consecuente):
        """Agrega una regla a la base de reglas."""
        self.reglas.append((antecedente, consecuente))

    def inferir(self, hecho):
        """Infere nuevos hechos a partir de las reglas y el hecho dado."""
        nuevos_hechos = []
        for antecedente, consecuente in self.reglas:
            if antecedente == hecho:
                nuevos_hechos.append(consecuente)
        return nuevos_hechos

# Crear una instancia de la inferencia lógica proposicional
ilp = InferenciaLogicaProposicional()

# Agregar reglas al sistema
ilp.agregar_regla("P", "Q")
ilp.agregar_regla("Q", "R")

# Consultar nuevos hechos a inferir
hecho = "P"
print("Hecho:", hecho)
nuevos_hechos = ilp.inferir(hecho)
print("Nuevos hechos inferidos:", nuevos_hechos)
#-------------------------------------------------------------------------------
# 1.- class InferenciaLogicaProposicional:: Definimos una clase llamada InferenciaLogicaProposicional para representar nuestro sistema 
#     de inferencia lógica proposicional.
# 2.- def __init__(self):: El método __init__ se llama cuando se crea una nueva instancia de la clase. Aquí inicializamos la lista de reglas.
# 3.- self.reglas = []: Creamos una lista vacía para almacenar las reglas. Cada regla será una tupla de la forma (antecedente, consecuente).
# 4.- def agregar_regla(self, antecedente, consecuente):: Definimos un método llamado agregar_regla para agregar una regla al sistema.
# 5.- self.reglas.append((antecedente, consecuente)): Agregamos la regla dada a la lista de reglas.
# 6.- def inferir(self, hecho):: Definimos un método llamado inferir para inferir nuevos hechos a partir de las reglas y un hecho dado.
# 7.- nuevos_hechos = []: Creamos una lista vacía para almacenar los nuevos hechos inferidos.
# 8.- for antecedente, consecuente in self.reglas:: Iteramos sobre cada regla en la lista de reglas.
# 9.- if antecedente == hecho:: Comprobamos si el antecedente de la regla coincide con el hecho dado.
# 10.- nuevos_hechos.append(consecuente): Si coincide, agregamos el consecuente de la regla a la lista de nuevos hechos inferidos.
# 11.- return nuevos_hechos: Devolvemos la lista de nuevos hechos inferidos.
# 12.- ilp = InferenciaLogicaProposicional(): Creamos una instancia de la clase InferenciaLogicaProposicional.
# 13.- ilp.agregar_regla("P", "Q"): Agregamos algunas reglas al sistema. En este caso, estamos utilizando el Modus Ponens: 
#      si P implica Q, y tenemos P, entonces podemos inferir Q.
# 14.- ilp.agregar_regla("Q", "R"): Agregamos otra regla al sistema.
# 15.- hecho = "P": Definimos un hecho inicial.
# 16.- nuevos_hechos = ilp.inferir(hecho): Utilizamos el método inferir para inferir nuevos hechos a partir del hecho dado.
# 17.- print("Hecho:", hecho): Imprimimos el hecho inicial.
# 18.- print("Nuevos hechos inferidos:", nuevos_hechos): Imprimimos los nuevos hechos inferidos.