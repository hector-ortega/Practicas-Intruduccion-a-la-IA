#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------

# La lógica por defecto es una forma de lógica no monótona que permite definir reglas por defecto que se aplican a menos que se presente 
# evidencia en contra de ellas. Esta lógica se utiliza para razonar en situaciones donde la información es incompleta o incierta, y donde las 
# conclusiones pueden cambiar a medida que se presenta nueva información.

# Funcionamiento:

# 1.- Reglas por Defecto:
# - En la lógica por defecto, se definen reglas por defecto que se aplican a menos que se presente evidencia en contra de ellas.
# - Estas reglas establecen relaciones entre eventos y estados y proporcionan una base para la inferencia en ausencia de información completa.

# 2.- Inferencia con Reglas por Defecto:
# - Para realizar inferencias, se evalúan las reglas por defecto en función de la información disponible.
# - Si se encuentra evidencia que contradice una regla por defecto, esta regla puede ser anulada y se pueden hacer nuevas inferencias basadas en la nueva información.

# 3.- Flexibilidad en las Conclusiones:
# - La lógica por defecto permite una flexibilidad en las conclusiones, ya que estas pueden cambiar a medida que se presenta nueva información.
# - Las conclusiones no son necesariamente definitivas y pueden estar sujetas a revisión en función de la evidencia disponible.

# 4.- Adaptabilidad a la Información:
# La lógica por defecto es adaptable a medida que se presenta nueva información, lo que permite tomar decisiones informadas incluso en situaciones de incertidumbre

#--------------- PROGRAMA ------------------------------------
class Regla:
    """
    Clase que representa una regla en el sistema de lógica por defecto.
    """
    def __init__(self, antecedente, consecuente):
        self.antecedente = antecedente  # Parte izquierda de la regla
        self.consecuente = consecuente  # Parte derecha de la regla

    def __str__(self):
        return f"{self.antecedente} => {self.consecuente}"


class SistemaLogicaPorDefecto:
    """
    Clase que representa un sistema de lógica por defecto.
    """
    def __init__(self):
        self.reglas_por_defecto = []  # Lista de reglas por defecto en el sistema

    def agregar_regla(self, regla):
        """
        Agrega una regla por defecto al sistema.
        """
        self.reglas_por_defecto.append(regla)

    def inferir_conclusion(self, hecho):
        """
        Infieren una conclusión basada en las reglas por defecto.
        """
        conclusion = None  # Conclusion inicialmente no se ha inferido
        
        # Itera sobre cada regla por defecto en el sistema
        for regla in self.reglas_por_defecto:
            # Verifica si el antecedente de la regla está presente en los hechos
            if regla.antecedente in hecho:
                conclusion = regla.consecuente  # Asigna la conclusión como el consecuente de la regla
        
        # Si ninguna regla se aplica, se devuelve None
        return conclusion


# Creamos un sistema de lógica por defecto
sistema = SistemaLogicaPorDefecto()

# Definimos algunas reglas por defecto
regla1 = Regla("p", "q")  # Si p es verdadero, entonces q es verdadero por defecto
regla2 = Regla("q", "r")  # Si q es verdadero, entonces r es verdadero por defecto

# Agregamos las reglas al sistema
sistema.agregar_regla(regla1)
sistema.agregar_regla(regla2)

# Definimos algunos hechos iniciales
hechos = ["p"]  # Se asume inicialmente que p es verdadero

# Inferimos una conclusión basada en los hechos
conclusion = sistema.inferir_conclusion(hechos)

# Imprimimos la conclusión inferida
print("Conclusión inferida:", conclusion)

#------------------------------------------------------------------
# Este código implementa un sistema de lógica por defecto simple utilizando clases en Python. La clase Regla representa una regla con un 
# antecedente y un consecuente, mientras que la clase SistemaLogicaPorDefecto representa el sistema de lógica por defecto en sí.

# El programa crea un sistema de lógica por defecto, define algunas reglas por defecto, agrega las reglas al sistema, y luego define 
# algunos hechos iniciales. Luego, infiere una conclusión basada en los hechos iniciales y las reglas por defecto.