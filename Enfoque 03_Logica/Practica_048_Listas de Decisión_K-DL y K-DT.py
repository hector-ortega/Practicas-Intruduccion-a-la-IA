#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# Listas de Decisión (K-DL):

# Las listas de decisión (Decision Lists) son estructuras utilizadas en aprendizaje automático para la clasificación de datos. Son una
# secuencia de reglas de decisión simples, donde cada regla especifica una condición sobre los atributos de entrada y la acción a tomar
# si esa condición se cumple. La predicción se realiza evaluando secuencialmente cada regla hasta encontrar una que se cumpla para la instancia de entrada.
# En contraste con los árboles de decisión, las listas de decisión no tienen una estructura jerárquica y pueden contener reglas superpuestas.

# Árboles de Decisión (K-DT):

# Los árboles de decisión (Decision Trees) son estructuras de árbol utilizadas para la clasificación y regresión en aprendizaje automático.
# Cada nodo interno del árbol representa una pregunta sobre una característica de entrada, y cada hoja representa una predicción. Los árboles
# de decisión se construyen dividiendo el conjunto de datos en función de las características que maximizan la pureza de las clases en cada nodo.
# Cuando una nueva instancia llega al árbol, se sigue un camino desde la raíz hasta una hoja, donde se realiza la predicción.

# Funcionamiento:

# - En las listas de decisión, se evalúa secuencialmente cada regla para determinar la acción a tomar para una instancia dada. 
#   Si una regla se cumple, se toma la acción asociada y se completa la predicción.
# - En los árboles de decisión, se sigue un camino desde la raíz hasta una hoja, evaluando las preguntas en cada nodo interno en 
#   función de los valores de las características de la instancia. Cuando se llega a una hoja, se realiza la predicción asociada a esa hoja.
# - En resumen, las listas de decisión y los árboles de decisión son algoritmos fundamentales
# #--------------- PROGRAMA ------------------------------------

#-------------------------Listas de Decisión (K-DL):------------------
class DecisionList:
    def __init__(self, rules):
        self.rules = rules  # Almacena las reglas de la lista de decisión

    def predict(self, instance):
        for condition, action in self.rules:
            if condition(instance):  # Verifica si la condición se cumple para la instancia
                return action  # Retorna la acción asociada a la primera regla que se cumple
        return "No se pudo clasificar"  # Si ninguna regla se cumple, retorna un mensaje de error


# Ejemplo de uso para Decision List
def condition1(instance):
    return instance["edad"] < 30  # Condición: Si la edad es menor a 30

def condition2(instance):
    return instance["sexo"] == "Femenino"  # Condición: Si el sexo es femenino

rules = [
    (condition1, "Grupo A"),  # Si condition1 es verdadera, clasificar como Grupo A
    (condition2, "Grupo B")   # Si condition2 es verdadera, clasificar como Grupo B
]

decision_list = DecisionList(rules)

instance1 = {"edad": 25, "sexo": "Masculino"}
instance2 = {"edad": 35, "sexo": "Femenino"}

print(decision_list.predict(instance1))  # Salida: Grupo A
print(decision_list.predict(instance2))  # Salida: Grupo B
#-------------------------------------------------------------------------
# Este código define la clase DecisionList, que representa una lista de decisión. Luego, se crea una instancia de esta clase 
# con reglas específicas y se realizan predicciones para dos instancias de entrada diferentes.

# El método predict recorre las reglas en orden y, para cada una, verifica si la condición se cumple para la instancia de entrada. 
# Si encuentra una regla cuya condición se cumple, devuelve la acción asociada a esa regla. Si ninguna regla se cumple, devuelve un mensaje de error.

#-------------------Arboles de desicion (K-DT)----------------------------

class DecisionTree:
    def __init__(self, question, true_branch, false_branch):
        self.question = question  # La pregunta que se hace en este nodo
        self.true_branch = true_branch  # Subárbol para respuestas verdaderas
        self.false_branch = false_branch  # Subárbol para respuestas falsas

    def predict(self, instance):
        if self.question(instance):  # Evalúa la pregunta para la instancia
            return self.true_branch.predict(instance)  # Si es verdadera, sigue por el subárbol verdadero
        else:
            return self.false_branch.predict(instance)  # Si es falsa, sigue por el subárbol falso


# Ejemplo de uso para Decision Tree
def question1(instance):
    return instance["edad"] < 30  # Pregunta: ¿La edad es menor a 30?

def question2(instance):
    return instance["sexo"] == "Femenino"  # Pregunta: ¿El sexo es femenino?

true_branch = DecisionTree("Pregunta 1", "Grupo A", "Grupo B")  # Subárbol para respuestas verdaderas
false_branch = DecisionTree("Pregunta 2", "Grupo C", "Grupo D")  # Subárbol para respuestas falsas

decision_tree = DecisionTree(question1, true_branch, false_branch)  # Raíz del árbol de decisiones

print(decision_tree.predict(instance1))  # Salida: Grupo A
print(decision_tree.predict(instance2))  # Salida: Grupo B

#-------------------------------------------------------------------------------------------
# En este código, la clase DecisionTree representa un árbol de decisión. Se crean instancias de esta clase con una pregunta, y 
# subárboles para respuestas verdaderas y falsas. La pregunta se evalúa para la instancia de entrada, y dependiendo del resultado, 
# se sigue por el subárbol verdadero o el falso.