#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# Fuzzy CLIPS es una extensión de CLIPS (C Language Integrated Production System), un lenguaje de programación utilizado para construir sistemas expertos.
# La lógica difusa, también conocida como lógica borrosa, es una técnica que permite modelar la incertidumbre y la imprecisión en los datos y en el razonamiento.
# Fuzzy CLIPS combina las capacidades de CLIPS con las funciones de la lógica difusa para permitir la creación de sistemas expertos que manejen
# información imprecisa de manera efectiva.

# 1.- Definición de Reglas Difusas:
# - En Fuzzy CLIPS, se definen reglas difusas que relacionan las variables de entrada con las variables de salida. Estas reglas se expresan en un 
#   lenguaje similar a las reglas en CLIPS, pero incluyen términos difusos y operadores lógicos difusos.

# 2.- Definición de Conjuntos Difusos:
# - Se definen conjuntos difusos que representan las categorías o rangos de valores para las variables de entrada y salida. 
#   Cada conjunto difuso está asociado con una función de pertenencia que describe la probabilidad de que un valor pertenezca a ese conjunto.

# 3.- Inferencia Difusa:
# - Durante la inferencia, se evalúan las reglas difusas utilizando los valores de las variables de entrada y las funciones de pertenencia de los conjuntos difusos.
# - Se combinan las reglas difusas para obtener un resultado difuso que representa la salida del sistema.

# 4.- Defuzzificación (Opcional):
# - En algunos casos, es necesario convertir el resultado difuso en un valor numérico concreto. Esto se hace a través de un proceso 
#   llamado defuzzificación, que convierte el resultado difuso en un valor numérico que puede ser utilizado para tomar decisiones concretas.
#--------------- PROGRAMA ------------------------------------

import clips

# Inicializamos el entorno CLIPS
environment = clips.Enviorment()

# Definimos las reglas difusas en Fuzzy CLIPS
environment.build("""
    (defrule temperatura-fria
        (temperatura ?x&:(<= 0 ?x 20))
        =>
        (assert (grado-frio (fuzzy-triangle ?x 0 10 20)))
    )
    (defrule temperatura-calida
        (temperatura ?x&:(<= 15 ?x 25))
        =>
        (assert (grado-calor (fuzzy-triangle ?x 15 20 25)))
    )
    (defrule temperatura-caliente
        (temperatura ?x&:(<= 20 ?x 40))
        =>
        (assert (grado-calor (fuzzy-triangle ?x 20 30 40)))
    )
""")

# Definimos la función para realizar inferencia difusa
def inferir_temperatura(temperatura):
    environment.reset()  # Reseteamos el entorno CLIPS
    environment.assert_string(f"(temperatura {temperatura})")  # Insertamos la temperatura como hecho
    environment.run()  # Ejecutamos el sistema experto
    grado_frio = environment.eval("(membership grado-frio)")  # Obtenemos el grado de frío
    grado_calor = environment.eval("(membership grado-calor)")  # Obtenemos el grado de calor
    return grado_frio, grado_calor

# Ejemplo de inferencia difusa
temperatura_entrada = 18
grado_frio, grado_calor = inferir_temperatura(temperatura_entrada)
print(f"Temperatura de entrada: {temperatura_entrada}")
print(f"Grado de frío: {grado_frio}")
print(f"Grado de calor: {grado_calor}")

#---------------------------------------------------------------

# 1.- Importamos la biblioteca PyCLIPS, que nos permite interactuar con el sistema experto Fuzzy CLIPS desde Python.
# 2.- Inicializamos un entorno CLIPS.
# 3.- Definimos las reglas difusas en Fuzzy CLIPS utilizando el método build() del entorno. En este ejemplo, definimos reglas para clasificar 
#     la temperatura en fría, cálida y caliente utilizando conjuntos difusos triangulares.
# 4.- Definimos una función inferir_temperatura() que toma la temperatura como entrada, la inserta como hecho en el entorno CLIPS, ejecuta
#     el sistema experto y devuelve los grados de pertenencia a los conjuntos difusos de frío y calor.
# 5.- Ejecutamos un ejemplo de inferencia difusa para una temperatura de entrada específica (temperatura_entrada) y mostramos los resultados en la consola.