#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# La independencia condicional es un concepto fundamental en la teoría de la probabilidad que se refiere a la situación en la que la ocurrencia
# de un evento no afecta la probabilidad de que ocurra otro evento. Formalmente, dos eventos A y B se consideran condicionalmente independientes 
# si la probabilidad de que ocurra el evento 𝐵 dado que el evento A ha ocurrido es igual a la probabilidad de que ocurra el evento B sin tener en cuenta si el evento 
# A ha ocurrido o no.
#--------------- PROGRAMA ------------------------------------
# Importamos la librería random para generar números aleatorios
import random

# Definimos una función para simular el lanzamiento de un dado
def lanzar_dado():
    return random.randint(1, 6)  # Generamos un número aleatorio entre 1 y 6 (inclusive)

# Definimos una función para simular el lanzamiento de una moneda
def lanzar_moneda():
    return random.choice(['Cara', 'Sello'])  # Elegimos aleatoriamente entre 'Cara' y 'Sello'

# Definimos una función para realizar múltiples simulaciones y calcular la probabilidad condicional
def calcular_probabilidad_condicional(iteraciones):
    contador_evento_1_y_2 = 0  # Contador para eventos donde se obtiene número par en el dado y cara en la moneda
    contador_evento_1 = 0  # Contador para eventos donde se obtiene número par en el dado
    
    # Realizamos las simulaciones
    for _ in range(iteraciones):
        # Simulamos el lanzamiento del dado
        resultado_dado = lanzar_dado()
        # Simulamos el lanzamiento de la moneda
        resultado_moneda = lanzar_moneda()
        
        # Verificamos si se obtuvo un número par en el dado
        if resultado_dado % 2 == 0:
            contador_evento_1 += 1  # Incrementamos el contador para eventos donde se obtiene número par en el dado
            
            # Verificamos si también se obtuvo cara en la moneda
            if resultado_moneda == 'Cara':
                contador_evento_1_y_2 += 1  # Incrementamos el contador para eventos donde se obtiene número par en el dado y cara en la moneda
    
    # Calculamos la probabilidad condicional
    probabilidad_condicional = contador_evento_1_y_2 / contador_evento_1
    
    return probabilidad_condicional

# Definimos el número de simulaciones a realizar
iteraciones = 10000

# Calculamos la probabilidad condicional
probabilidad_condicional = calcular_probabilidad_condicional(iteraciones)

# Imprimimos el resultado
print("La probabilidad condicional de obtener cara en la moneda dado que se obtiene un número par en el dado es:", probabilidad_condicional)

#------------------------------------------------------------------------------------------------------------------------------------
# 1.- Importamos la librería random para generar números aleatorios.
# 2.- Definimos la función lanzar_dado() que simula el lanzamiento de un dado y devuelve un número aleatorio entre 1 y 6.
# 3.- Definimos la función lanzar_moneda() que simula el lanzamiento de una moneda y devuelve aleatoriamente 'Cara' o 'Sello'.
# 4.- Definimos la función calcular_probabilidad_condicional(iteraciones) que realiza un número especificado de simulaciones para calcular 
# la probabilidad condicional de obtener cara en la moneda dado que se obtiene un número par en el dado.
# 5.- En la función calcular_probabilidad_condicional(iteraciones), inicializamos contadores para contar eventos donde se obtiene un número 
# par en el dado y cara en la moneda, y eventos donde se obtiene un número par en el dado.
# 6.- Luego, realizamos las simulaciones, lanzando el dado y la moneda en cada iteración y actualizando los contadores según los resultados.
# 7.- Después de todas las simulaciones, calculamos la probabilidad condicional dividiendo el número de eventos donde se obtiene un número par
# en el dado y cara en la moneda entre el número de eventos donde se obtiene un número par en el dado.
# 8.- Finalmente, definimos el número de iteraciones a realizar y calculamos la probabilidad condicional llamando a la función 
# calcular_probabilidad_condicional(iteraciones).
# 9.- Imprimimos el resultado que muestra la probabilidad condicional calculada.