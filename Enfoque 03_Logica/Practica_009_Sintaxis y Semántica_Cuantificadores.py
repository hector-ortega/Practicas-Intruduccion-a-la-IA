#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------

# Los cuantificadores son elementos fundamentales en la lógica de predicados, que es una extensión de la lógica proposicional 
# que permite cuantificar sobre variables. Estos cuantificadores permiten expresar proposiciones sobre todos los elementos
# de un conjunto (cuantificador universal) o sobre al menos un elemento de un conjunto (cuantificador existencial). 
# Los cuantificadores son esenciales para la expresión de proposiciones más complejas y para la formalización de la lógica 
# matemática y el razonamiento deductivo.

# Funcionamiento:

# 1.- Cuantificador universal (∀): Este cuantificador se utiliza para expresar proposiciones que son verdaderas para 
#     todos los elementos de un conjunto. Por ejemplo, la proposición "todos los números naturales son pares" se
#      puede expresar como ∀x (x es un número natural → x es par), donde x representa un número natural.
# 2.- Cuantificador existencial (∃): Este cuantificador se utiliza para expresar proposiciones que son verdaderas para al 
#     menos un elemento de un conjunto. Por ejemplo, la proposición "existe un número primo mayor que 10" se puede expresar 
#     como ∃x (x es un número primo y x > 10), donde x representa un número entero.
# 3.- Evaluación de proposiciones con cuantificadores: Para evaluar una proposición con cuantificadores, se deben considerar 
#     todos los elementos del conjunto en cuestión. En el caso del cuantificador universal, la proposición debe ser verdadera para
#     todos los elementos del conjunto. En el caso del cuantificador existencial, la proposición debe ser verdadera para al menos
#     un elemento del conjunto.
# 4.- Algoritmos de inferencia y razonamiento: Los cuantificadores son utilizados en algoritmos de inferencia y razonamiento para 
#     realizar deducciones lógicas sobre conjuntos de proposiciones cuantificadas. Estos algoritmos pueden determinar la verdad o 
#     falsedad de proposiciones cuantificadas, así como realizar inferencias válidas sobre ellas.
#--------------- PROGRAMA ------------------------------------
def cuantificador_universal(conjunto, proposicion):
    """Evalúa si la proposición es verdadera para todos los elementos del conjunto."""
    for elemento in conjunto:
        if not proposicion(elemento):
            return False
    return True

def cuantificador_existencial(conjunto, proposicion):
    """Evalúa si la proposición es verdadera para al menos un elemento del conjunto."""
    for elemento in conjunto:
        if proposicion(elemento):
            return True
    return False

# Ejemplo de uso
numeros = [1, 2, 3, 4, 5]

# Definimos una proposición que verifica si un número es par
es_par = lambda x: x % 2 == 0

# Verificamos si todos los números en la lista son pares
resultado_universal = cuantificador_universal(numeros, es_par)
print("¿Todos los números son pares?", resultado_universal)

# Verificamos si al menos un número en la lista es par
resultado_existencial = cuantificador_existencial(numeros, es_par)
print("¿Al menos un número es par?", resultado_existencial)

#-------------------------------------------------------------------------

# 1.- Definimos dos funciones, cuantificador_universal y cuantificador_existencial, que implementan los cuantificadores universal y
#     existencial respectivamente.
# 2.- En la función cuantificador_universal, iteramos sobre cada elemento del conjunto y evaluamos la proposición para cada uno. 
#     Si encontramos al menos un elemento para el cual la proposición es falsa, retornamos False, indicando que la proposición 
#     no se cumple para todos los elementos. Si recorremos todos los elementos y la proposición es verdadera para cada uno, retornamos True.
# 3.- En la función cuantificador_existencial, iteramos sobre cada elemento del conjunto y evaluamos la proposición para cada uno. 
#     Si encontramos al menos un elemento para el cual la proposición es verdadera, retornamos True, indicando que al menos
#     un elemento cumple con la proposición. Si recorremos todos los elementos y la proposición es falsa para cada uno, retornamos False.
# 4.- En el ejemplo de uso, definimos una lista de números y una proposición que verifica si un número es par. 
#     Luego, utilizamos las funciones cuantificador_universal y cuantificador_existencial para verificar si todos 
#     los números son pares y si al menos uno es par respectivamente.