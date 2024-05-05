#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# El algoritmo de resolución Skolem se utiliza en lógica de primer orden para probar la validez de una fórmula mediante la negación de la 
# conclusión y la aplicación de la resolución para encontrar una contradicción. Este algoritmo es especialmente útil cuando se trabaja con 
# fórmulas que contienen cuantificadores existenciales.

# Funcionamiento:

# 1.- Combinación de Fórmulas:
# - Para aplicar la resolución Skolem, se combinan las cláusulas de la fórmula original y la negación de la conclusión. 
#   Estas cláusulas se utilizan como entrada para el algoritmo de resolución.

# 2.- Aplicación de la Resolución:
# - Se aplica la resolución de manera iterativa entre las cláusulas combinadas. La resolución se realiza combinando pares de cláusulas y 
#   eliminando literales que tengan su complemento en la otra cláusula.
# - Si se encuentra una cláusula vacía durante el proceso de resolución, esto indica una contradicción, lo que implica que la fórmula original es válida.

# 3.- Búsqueda de Contradicción:
# - El algoritmo continúa aplicando la resolución hasta que se encuentre una contradicción o hasta que ya no se puedan generar más cláusulas.  
#   Si no se encuentra una contradicción después de este proceso, la fórmula no es válida.
#--------------- PROGRAMA ------------------------------------
def complemento(literal):
    """
    Devuelve el complemento de un literal.
    Por ejemplo, si el literal es 'p', devuelve '~p', y viceversa.
    """
    if literal.startswith("~"):
        return literal[1:]
    else:
        return "~" + literal

def resolver(clausula1, clausula2):
    """
    Realiza la resolución entre dos cláusulas.
    Devuelve una nueva cláusula que es el resultado de la resolución.
    """
    nueva_clausula = []
    for literal in clausula1:
        if complemento(literal) not in clausula2:
            nueva_clausula.append(literal)
    for literal in clausula2:
        if complemento(literal) not in clausula1:
            nueva_clausula.append(literal)
    return nueva_clausula

def skolem(f1, f2):
    """
    Realiza el algoritmo de resolución Skolem.
    Devuelve True si se encuentra una contradicción, False en caso contrario.
    """
    clausulas = f1 + f2  # Combinamos las cláusulas de las dos fórmulas
    while True:
        nuevas_clausulas = []
        for i in range(len(clausulas)):
            for j in range(i+1, len(clausulas)):
                res = resolver(clausulas[i], clausulas[j])
                if [] in res:
                    # Si se encuentra una cláusula vacía, hay una contradicción
                    return True
                for clausula in res:
                    if clausula not in nuevas_clausulas:
                        nuevas_clausulas.append(clausula)
        if nuevas_clausulas == clausulas:
            # No se encontraron nuevas cláusulas, no hay contradicción
            return False
        clausulas = nuevas_clausulas

# Ejemplo de uso
formula1 = [["p", "~q"], ["~p", "r", "s"], ["q", "~r"]]
formula2 = [["~p", "q"], ["p", "~q", "~r"]]
print("¿Hay contradicción?", skolem(formula1, formula2))

#---------------------------------------------------------------
# 1.- La función complemento toma un literal como entrada y devuelve su complemento (negación). Por ejemplo, 
#     si el literal es 'p', devuelve '~p', y viceversa.
# 2.- La función resolver realiza la resolución entre dos cláusulas. Elimina los literales que tienen su complemento en la otra cláusula
#     y devuelve una nueva cláusula que es el resultado de la resolución.
# 3.- La función skolem implementa el algoritmo de resolución Skolem. Combina las cláusulas de las dos fórmulas, y luego aplica la resolución
#     de manera iterativa hasta que se encuentre una contradicción (cláusula vacía) o no se puedan generar más cláusulas.
# 4.- En el ejemplo de uso, definimos dos fórmulas (representadas como listas de cláusulas) y llamamos a la función skolem para verificar 
#     si hay una contradicción entre ellas.