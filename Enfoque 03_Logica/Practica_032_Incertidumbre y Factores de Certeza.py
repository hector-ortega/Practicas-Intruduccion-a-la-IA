#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# El algoritmo de incertidumbre y factores de certeza se utiliza en inteligencia artificial para representar y manejar 
# situaciones donde la información disponible es incierta o sujeta a diferentes grados de confiabilidad. Este tipo de algoritmo es
# esencial cuando el conocimiento disponible no es absoluto y se requiere un manejo de la incertidumbre para la toma de decisiones.

# Funcionamiento del Algoritmo de Incertidumbre y Factores de Certeza:

# 1.- Asignación de Valores de Certeza:
# - Cada hecho o premisa se asocia con un valor de certeza que indica la confiabilidad de esa información.

# 2.- Inferencia con Valores de Certeza:
# - Se aplican reglas lógicas teniendo en cuenta los valores de certeza asociados con los hechos. Esto permite que las conclusiones 
#   reflejen la incertidumbre del conocimiento disponible.

# 3.- Actualización de Creencias:
# - A medida que se adquiere nueva información, los valores de certeza se actualizan en función de esta información adicional.
#   Esto permite que el sistema adapte sus creencias a medida que se acumula más evidencia.

# 4-.- Manejo de la Incertidumbre en la Toma de Decisiones:
# - Cuando se toman decisiones, se consideran los valores de certeza asociados con las diferentes opciones. 
#   Esto permite que el sistema tome decisiones informadas incluso en entornos inciertos.

#--------------- PROGRAMA ------------------------------------

class Regla:
    def __init__(self, antecedente, consecuente, peso):
        self.antecedente = antecedente  # Condiciones que deben cumplirse para aplicar la regla
        self.consecuente = consecuente  # Hecho que se concluye si se cumplen las condiciones
        self.peso = peso                # Peso o grado de certeza de la regla

class BaseConocimiento:
    def __init__(self):
        self.hechos = {}      # Diccionario para almacenar los hechos y sus valores de verdad
        self.reglas = []      # Lista de reglas conocidas

    def agregar_hecho(self, hecho, valor):
        self.hechos[hecho] = valor

    def agregar_regla(self, regla):
        self.reglas.append(regla)

    def inferir(self):
        resultados = {}  # Diccionario para almacenar los resultados de la inferencia
        for regla in self.reglas:
            valor = self.evaluar_regla(regla)
            if regla.consecuente not in resultados or valor > resultados[regla.consecuente]:
                resultados[regla.consecuente] = valor
        return resultados

    def evaluar_regla(self, regla):
        min_valor = 1  # Valor inicial para el mínimo valor de verdad de las premisas
        for premisa, valor in regla.antecedente.items():
            if premisa not in self.hechos:
                return 0  # Si alguna premisa no está en la base de conocimiento, no se puede evaluar la regla
            min_valor = min(min_valor, self.hechos[premisa] * valor)  # Calcula el mínimo valor de verdad
        return min_valor * regla.peso  # Retorna el mínimo valor de verdad multiplicado por el peso de la regla

# Crear una base de conocimiento
bc = BaseConocimiento()

# Definir algunas reglas y hechos iniciales
regla1 = Regla({"llueve": 1}, "humedo", 0.8)
regla2 = Regla({"nublado": 0.7, "no_llueve": 0.9}, "seco", 0.6)

# Agregar reglas y hechos a la base de conocimiento
bc.agregar_regla(regla1)
bc.agregar_regla(regla2)
bc.agregar_hecho("llueve", 0.6)
bc.agregar_hecho("nublado", 0.8)

# Inferir nuevos hechos y sus valores de verdad
resultados = bc.inferir()

# Imprimir los resultados de la inferencia
for hecho, valor in resultados.items():
    print(f"{hecho}: {valor}")

#---------------------------------------------------------------
# 1.- La clase Regla representa una regla con un antecedente, un consecuente y un peso que indica el grado de certeza de la regla.
# 2.- La clase BaseConocimiento contiene los hechos conocidos y las reglas que se utilizan para inferir nuevos hechos.
# 3.- El método inferir recorre todas las reglas conocidas, evalúa cada una y devuelve los resultados con los valores de verdad más altos para cada consecuente.
# 4.- El método evaluar_regla evalúa el valor de verdad de una regla en función de los hechos conocidos y sus valores de verdad.