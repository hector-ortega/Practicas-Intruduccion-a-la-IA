#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------

# La Ingeniería del Conocimiento es una disciplina que se centra en el diseño y desarrollo de sistemas inteligentes que 
# pueden resolver problemas mediante la captura, representación y aplicación del conocimiento experto. Este enfoque se basa 
# en la idea de que el conocimiento experto, que normalmente reside en la mente de individuos con experiencia en un dominio 
# específico, puede ser formalizado y utilizado para resolver problemas de manera efectiva.

# Funcionamiento:
# 1.- Captura del conocimiento: El primer paso en el desarrollo de un sistema basado en conocimiento es capturar
#     el conocimiento experto relevante en el dominio específico. Esto puede implicar entrevistar a expertos humanos, 
#     analizar datos históricos, revisar literatura especializada y más.
# 2.- Representación del conocimiento: Una vez que se ha capturado el conocimiento, este debe ser representado en una
#     forma que pueda ser utilizada por un sistema informático. Esto puede implicar la creación de bases de conocimiento,
#     ontologías, reglas lógicas, modelos de redes semánticas u otras estructuras de datos.
# 3.- Desarrollo del sistema: Con el conocimiento representado, se procede al desarrollo del sistema basado en conocimiento 
#     utilizando técnicas de programación, diseño de bases de datos, desarrollo de interfaces de usuario y otras herramientas
#     y tecnologías de software.
# 4.- Evaluación y refinamiento: Una vez que el sistema está en funcionamiento, se evalúa su rendimiento en situaciones reales
#     y se realizan ajustes y mejoras según sea necesario. Esto puede implicar la incorporación de nuevos datos,
#     la actualización de reglas o modelos, y la mejora de la interfaz de usuario.

#--------------- PROGRAMA ------------------------------------
# Definimos un diccionario que contiene las reglas de recomendación de actividad
reglas_actividades = {
    'soleado': 'Ir a la playa',
    'lluvioso': 'Ver una película en casa',
    'nublado': 'Salir a dar un paseo',
    'nevado': 'Hacer muñecos de nieve'
}

def recomendar_actividad(clima):
    """
    Función para recomendar una actividad basada en el clima.
    
    Args:
        clima: String que describe el clima actual.
        
    Returns:
        String con la actividad recomendada.
    """
    if clima in reglas_actividades:  # Verificamos si hay una regla para el clima actual
        return reglas_actividades[clima]  # Devolvemos la actividad recomendada para ese clima
    else:
        return 'No se ha definido una actividad para este clima'  # Mensaje de error si no hay regla definida

# Ejemplo de uso
clima_actual = 'soleado'
actividad_recomendada = recomendar_actividad(clima_actual)
print(f"Para el clima '{clima_actual}', se recomienda: {actividad_recomendada}")

#----------------------------------------------------------------------

# 1.- Definimos un diccionario llamado reglas_actividades que contiene las reglas de recomendación de actividad.
#     Cada clave del diccionario representa una condición climática (soleado, lluvioso, nublado, nevado) y el valor
#     asociado es la actividad recomendada para ese clima.
# 2.- Creamos una función llamada recomendar_actividad que toma como entrada el clima actual y devuelve la actividad recomendada.
#     La función verifica si hay una regla definida para el clima actual en el diccionario de reglas. Si hay una regla definida,
#     devuelve la actividad recomendada; de lo contrario, devuelve un mensaje de error.
# 3.- En el ejemplo de uso, definimos el clima actual como 'soleado' y llamamos a la función recomendar_actividad
#     para obtener la actividad recomendada. Luego, imprimimos la actividad recomendada en la consola.