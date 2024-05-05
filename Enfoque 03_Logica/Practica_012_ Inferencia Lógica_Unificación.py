#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# Funcionamiento:
# El algoritmo de unificación busca encontrar una sustitución que haga que dos expresiones lógicas sean iguales. Funciona mediante la aplicación 
# de una serie de reglas que permiten combinar las expresiones de manera que puedan coincidir. Aquí están las reglas básicas del algoritmo de unificación:

# 1.- Variables: Si una de las expresiones es una variable, se puede unificar con cualquier otra expresión asignándole el valor de esa expresión.
# 2.- Constantes y Funciones: Si ambas expresiones son constantes o funciones con el mismo símbolo y la misma aridad, deben coincidir exactamente.
# 3.- Funciones: Si ambas expresiones son funciones con el mismo símbolo pero diferente aridad, no se pueden unificar.
# 4.- Listas y Estructuras de Datos Compuestas: Si ambas expresiones son listas o estructuras de datos compuestas con el mismo número de elementos,
#     se unifican elemento por elemento.
# 5.- Predicados: Si ambas expresiones son predicados con el mismo símbolo y el mismo número de argumentos, se unifican argumento por argumento.
# 6.- Recursividad: El algoritmo de unificación puede ser recursivo, lo que significa que puede aplicarse de manera iterativa hasta que se encuentre 
#     una solución o se determine que no es posible unificar las expresiones.

#--------------- PROGRAMA ------------------------------------
def unificar(s1, s2, sustitucion=None):
    """
    Función para unificar dos expresiones lógicas.
    
    Args:
        s1: Primera expresión lógica.
        s2: Segunda expresión lógica.
        sustitucion: Sustitución parcial inicial (opcional).
        
    Returns:
        Sustitución que hace que las dos expresiones sean iguales, o None si no se puede unificar.
    """
    # Si no se proporciona una sustitución, creamos una nueva
    if sustitucion is None:
        sustitucion = {}
    
    # Si las expresiones son iguales, devolvemos la sustitución actual
    if s1 == s2:
        return sustitucion
    
    # Si una de las expresiones es una variable, la sustituimos por la otra expresión
    if isinstance(s1, str):
        return unificar_variable(s1, s2, sustitucion)
    elif isinstance(s2, str):
        return unificar_variable(s2, s1, sustitucion)
    
    # Si las expresiones son listas, las unificamos elemento por elemento
    if isinstance(s1, list) and isinstance(s2, list):
        if len(s1) != len(s2):
            return None
        for x, y in zip(s1, s2):
            sustitucion = unificar(x, y, sustitucion)
            if sustitucion is None:
                return None
        return sustitucion
    
    # Si las expresiones son diferentes y ninguna es una variable, no se pueden unificar
    return None

def unificar_variable(var, x, sustitucion):
    """
    Función para unificar una variable con una expresión.
    
    Args:
        var: Variable a sustituir.
        x: Expresión con la que se sustituirá la variable.
        sustitucion: Sustitución parcial actual.
        
    Returns:
        Sustitución que hace que la variable sea igual a la expresión.
    """
    if var in sustitucion:
        return unificar(sustitucion[var], x, sustitucion)
    elif x in sustitucion:
        return unificar(var, sustitucion[x], sustitucion)
    else:
        sustitucion[var] = x
        return sustitucion

# Ejemplo de uso
expresion1 = ["f", "X", "a"]
expresion2 = ["f", "b", "Y"]
sustitucion = unificar(expresion1, expresion2)
print("Sustitución:", sustitucion)

#------------------------------------------------------------------
# 1.- La función unificar es la función principal que realiza la unificación entre dos expresiones lógicas.
#     Recibe dos expresiones s1 y s2, y una sustitución parcial opcional sustitucion. Comienza verificando si las
#     expresiones son iguales. Si lo son, devuelve la sustitución actual. Luego, verifica si una de las expresiones es una variable,
#     y si es así, llama a la función unificar_variable para tratar ese caso. Finalmente, si las expresiones son listas, las unifica elemento por elemento.
# 2.- La función unificar_variable maneja el caso en el que una de las expresiones es una variable. Si la variable ya está en la sustitución,
#     la unifica con la otra expresión en la sustitución. Si la otra expresión ya está en la sustitución, unifica la variable con esa expresión. 
#     Si ninguna de las expresiones está en la sustitución, agrega la variable y la expresión a la sustitución.
# 3.- En el ejemplo de uso, definimos dos expresiones y llamamos a la función unificar para encontrar una sustitución que haga que 
#     las expresiones sean iguales. Luego, imprimimos la sustitución encontrada.