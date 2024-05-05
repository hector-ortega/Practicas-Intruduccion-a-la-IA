#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
#Funcionamiento de los Sistemas Expertos:
# 1.- Adquisición de Conocimiento:
# - Los sistemas expertos adquieren conocimiento de expertos humanos mediante entrevistas, análisis de documentos, 
#   revisión de literatura y otras fuentes de información.

# 2.- Representación del Conocimiento:
# - El conocimiento adquirido se representa en una estructura de datos que el sistema experto puede entender 
#   y utilizar. Esto puede incluir reglas lógicas, bases de conocimiento, árboles de decisión, redes semánticas, entre otros.

# 3.- Inferencia:
# - Utilizan algoritmos de inferencia para procesar el conocimiento representado y llegar a conclusiones
#   o tomar decisiones. Esto implica aplicar reglas lógicas, realizar cálculos probabilísticos o utilizar técnicas de razonamiento específicas del dominio.

# 4.- Explicación del Razonamiento:
# - Los sistemas expertos pueden explicar cómo llegaron a una determinada conclusión o recomendación, 
#   proporcionando transparencia y justificación para sus decisiones.

# 5.- Actualización y Mantenimiento:
# - El conocimiento y las reglas de los sistemas expertos pueden actualizarse y modificarse a medida que se adquiere nueva 
#   información o se cambian las circunstancias del dominio.
#--------------- PROGRAMA ------------------------------------
# Definición de la base de conocimientos (reglas lógicas)
base_conocimientos = {
    "fiebre": {"gripe", "infección"},
    "tos": {"gripe", "resfriado"},
    "dolor_cabeza": {"gripe", "migraña"},
    "dolor_garganta": {"resfriado", "amigdalitis"},
    "fatiga": {"gripe", "infección"},
}

# Función para consultar al usuario y obtener síntomas
def obtener_sintomas():
    sintomas = []
    print("Por favor, responde sí o no a las siguientes preguntas:")
    for sintoma in base_conocimientos.keys():
        respuesta = input(f"Tienes {sintoma}? ").lower()
        if respuesta == "si":
            sintomas.append(sintoma)
    return sintomas

# Función para realizar el diagnóstico basado en los síntomas
def diagnosticar(sintomas):
    enfermedades = set()
    for sintoma in sintomas:
        if sintoma in base_conocimientos:
            enfermedades.update(base_conocimientos[sintoma])
    return enfermedades

# Función principal que ejecuta el sistema experto
def main():
    print("Bienvenido al sistema experto de diagnóstico de enfermedades.")
    print("Por favor, responde las siguientes preguntas:")
    
    # Obtener los síntomas del usuario
    sintomas = obtener_sintomas()
    
    # Realizar el diagnóstico basado en los síntomas
    enfermedades = diagnosticar(sintomas)
    
    # Mostrar los resultados del diagnóstico
    if enfermedades:
        print("El diagnóstico sugiere las siguientes enfermedades:")
        for enfermedad in enfermedades:
            print("-", enfermedad)
    else:
        print("No se encontraron enfermedades relacionadas con los síntomas proporcionados.")

if __name__ == "__main__":
    main()

#---------------------------------------------------
# 1.- base_conocimientos: Es un diccionario que contiene reglas lógicas que relacionan síntomas con posibles enfermedades.
# 2.- obtener_sintomas(): Esta función consulta al usuario sobre sus síntomas y devuelve una lista de síntomas ingresados.
# 3.- diagnosticar(sintomas): Esta función recibe una lista de síntomas y devuelve un conjunto de posibles enfermedades   
#     basadas en la base de conocimientos.
# 4.- main(): La función principal que ejecuta el sistema experto. Invoca a las funciones anteriores para obtener síntomas y 
#     realizar el diagnóstico, luego muestra los resultados al usuario.