#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# Los algoritmos de reglas de diagnóstico y causales se utilizan para determinar la causa probable de un problema o 
# condición basándose en un conjunto de reglas lógicas que describen la relación entre los síntomas observados y las 
# posibles causas. Estos algoritmos son utilizados en una variedad de campos, incluida la medicina, la ingeniería, la 
# informática y más, donde es necesario diagnosticar problemas basados en observaciones específicas.

# Funcionamiento:

# 1.- Definición de reglas: El primer paso en el uso de un algoritmo de reglas de diagnóstico es definir un conjunto 
#     de reglas que describan la relación entre los síntomas observados y las posibles causas. Estas reglas pueden
#     ser proporcionadas por expertos en el dominio o pueden ser derivadas de datos históricos.
# 2.- Evaluación de síntomas: Una vez que se han definido las reglas, el algoritmo evalúa los síntomas observados en 
#     función de estas reglas para determinar las posibles causas del problema. Esto puede implicar comparar los 
#     síntomas observados con los síntomas asociados a cada posible causa y determinar la probabilidad de que cada causa sea la responsable.
# 3.- Selección de la causa más probable: Una vez que se han evaluado los síntomas, el algoritmo selecciona la causa más 
#     probable del problema basándose en la información proporcionada por las reglas de diagnóstico y la probabilidad de 
#     que cada causa sea responsable.
# 4.- Presentación de resultados: Finalmente, el algoritmo presenta los resultados del diagnóstico al usuario,
#     proporcionando información sobre la causa probable del problema y, en algunos casos, recomendaciones para el 
#     tratamiento o la solución del problema.
#--------------- PROGRAMA ------------------------------------

# Definimos un diccionario que contiene las reglas de diagnóstico
reglas_diagnostico = {
    "Resfriado": ["Congestión nasal", "Estornudos", "Tos"],
    "Gripe": ["Fiebre", "Dolor de cabeza", "Dolor de cuerpo"],
    "Alergia": ["Estornudos", "Picazón en los ojos", "Secreción nasal"]
}

def diagnosticar(sintomas, reglas):
    """
    Función para diagnosticar la enfermedad basada en los síntomas observados.
    
    Args:
        sintomas: Lista de síntomas observados.
        reglas: Diccionario de reglas de diagnóstico.
        
    Returns:
        Lista de posibles enfermedades basadas en los síntomas observados.
    """
    enfermedades_posibles = []  # Lista para almacenar las enfermedades posibles
    
    # Iteramos sobre cada regla en el diccionario de reglas
    for enfermedad, sintomas_enfermedad in reglas.items():
        # Verificamos si todos los síntomas de la enfermedad están presentes en los síntomas observados
        if all(sintoma in sintomas for sintoma in sintomas_enfermedad):
            enfermedades_posibles.append(enfermedad)
    
    return enfermedades_posibles

# Ejemplo de uso
sintomas_observados = ["Estornudos", "Picazón en los ojos", "Secreción nasal"]
enfermedades_diagnosticadas = diagnosticar(sintomas_observados, reglas_diagnostico)
print("Enfermedades diagnosticadas:", enfermedades_diagnosticadas)

#----------------------------------------------------------------------------------
# 1.- Definimos un diccionario llamado reglas_diagnostico que contiene las reglas de diagnóstico. Cada clave del diccionario
#     representa una posible enfermedad, y el valor asociado es una lista de síntomas que están relacionados con esa enfermedad.
# 2.- Creamos una función llamada diagnosticar que toma como entrada una lista de síntomas observados y el 
#     diccionario de reglas de diagnóstico. La función recorre cada regla en el diccionario y compara los síntomas
#     observados con los síntomas asociados a cada enfermedad. Si todos los síntomas de una enfermedad están presentes 
#     en los síntomas observados, esa enfermedad se agrega a la lista de enfermedades posibles.
# 3.- En el ejemplo de uso, definimos una lista de síntomas observados y llamamos a la función diagnosticar para obtener
#     una lista de posibles enfermedades basadas en esos síntomas. Luego, imprimimos la lista de enfermedades diagnosticadas.