#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# FOIL (Primero Orden Iterativo de Aprendizaje de Reglas) es un algoritmo de programación lógica inductiva que se utiliza para aprender 
# reglas de clasificación a partir de ejemplos de datos etiquetados. El algoritmo es especialmente útil en el contexto de aprendizaje supervisado,
# donde se tienen datos de entrada junto con las etiquetas de salida correspondientes.

# El algoritmo FOIL funciona de la siguiente manera:

# 1.- Inicialización: Comienza con una regla vacía y busca el literal (condición) más específico que mejore la precisión de la regla. 
#     La precisión se refiere a la proporción de instancias correctamente clasificadas por la regla.
# 2.- Expansión iterativa: Luego, el algoritmo itera sobre todas las posibles extensiones de la regla, agregando literales que
#     aumenten la precisión de la regla. Estas extensiones se realizan considerando todas las combinaciones posibles de condiciones que
#     podrían ser agregadas a la regla.
# 3.- Selección de la mejor regla: Se selecciona la mejor regla, es decir, aquella que maximiza la precisión en 
#     el conjunto de datos de entrenamiento. Si hay múltiples reglas que proporcionan la misma precisión máxima, 
#     se puede seleccionar una de ellas aleatoriamente o mediante algún criterio de selección específico.

#--------------- PROGRAMA ------------------------------------
import itertools

# Función para calcular la precisión de una regla
def precision(rule, data):
    correct = sum(1 for instance in data if all(instance[attr] == val for attr, val in rule.items()))
    total = len(data)
    return correct / total if total > 0 else 0

# Función para generar todas las posibles extensiones de una regla
def expand_rule(rule, attributes, target_values):
    new_rules = []
    for attr in attributes:
        if attr not in rule:
            for val in target_values:
                new_rule = rule.copy()
                new_rule[attr] = val
                new_rules.append(new_rule)
    return new_rules

# Algoritmo FOIL
def foil(data, target_attr):
    # Obtener la lista de atributos y valores del objetivo
    attributes = set(data[0].keys()) - {target_attr}
    target_values = set(instance[target_attr] for instance in data)
    
    # Inicializar la regla vacía
    current_rule = {}
    
    # Iterar hasta que no haya mejoras en la precisión
    while True:
        # Generar todas las posibles extensiones de la regla actual
        possible_rules = expand_rule(current_rule, attributes, target_values)
        
        # Calcular la precisión de cada regla
        rule_precisions = [(rule, precision(rule, data)) for rule in possible_rules]
        
        # Seleccionar la regla con la mayor precisión
        best_rule, best_precision = max(rule_precisions, key=lambda x: x[1])
        
        # Si no hay mejora, terminar la iteración
        if best_precision <= precision(current_rule, data):
            break
        
        # Actualizar la regla actual
        current_rule = best_rule
    
    return current_rule

# Ejemplo de uso
if __name__ == "__main__":
    # Datos de ejemplo: instancias de entrenamiento con atributos y etiquetas
    data = [
        {'A': 'Soleado', 'B': 'Caliente', 'C': 'Alta', 'Playa': 'No'},
        {'A': 'Lluvioso', 'B': 'Fresco', 'C': 'Normal', 'Playa': 'No'},
        {'A': 'Soleado', 'B': 'Caliente', 'C': 'Alta', 'Playa': 'Sí'},
        {'A': 'Nublado', 'B': 'Caliente', 'C': 'Alta', 'Playa': 'Sí'},
        {'A': 'Nublado', 'B': 'Frío', 'C': 'Normal', 'Playa': 'Sí'},
        {'A': 'Lluvioso', 'B': 'Fresco', 'C': 'Normal', 'Playa': 'No'},
        {'A': 'Soleado', 'B': 'Fresco', 'C': 'Normal', 'Playa': 'Sí'},
        {'A': 'Lluvioso', 'B': 'Caliente', 'C': 'Alta', 'Playa': 'No'}
    ]
    
    # Atributo objetivo
    target_attr = 'Playa'
    
    # Aplicar el algoritmo FOIL para generar una regla
    rule = foil(data, target_attr)
    print("Regla generada:", rule)

#------------------------------------------------------------------------
# En este código, primero definimos una función precision que calcula la precisión de una regla en el conjunto de datos de entrenamiento. 
# Luego, definimos una función expand_rule que genera todas las posibles extensiones de una regla dada. Finalmente, implementamos
# la función foil que ejecuta el algorit