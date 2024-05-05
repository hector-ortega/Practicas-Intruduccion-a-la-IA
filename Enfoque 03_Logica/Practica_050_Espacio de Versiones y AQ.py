#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------

# El Espacio de Versiones y el Algoritmo AQ (Algoritmo de Quinlan) son algoritmos de aprendizaje supervisado utilizados en el ámbito de la inteligencia
# artificial para la clasificación de datos.

# Espacio de Versiones:
# El Espacio de Versiones es un algoritmo que busca encontrar la hipótesis más específica que sea consistente con todos los ejemplos positivos y negativos 
# en un conjunto de entrenamiento. El algoritmo trabaja con un conjunto de hipótesis que son versiones candidatas de la solución final. Inicialmente, el 
# Espacio de Versiones establece una hipótesis inicial vacía y, a medida que recorre los ejemplos de entrenamiento, la modifica para que sea más específica 
# sin dejar de ser consistente con los ejemplos observados.

# El algoritmo generalmente sigue los siguientes pasos:

# 1.- Inicializa la hipótesis como la versión más específica posible.
# 2.- Recorre cada ejemplo de entrenamiento.
# 3.- Actualiza la hipótesis para que sea más específica sin dejar de ser consistente con el ejemplo actual.
# 4.- Repite el paso 3 para cada ejemplo de entrenamiento.

# El Espacio de Versiones es efectivo para problemas de clasificación donde la hipótesis final puede representarse como una conjunción de restricciones sobre los atributos.

# Algoritmo AQ:
# El Algoritmo AQ, desarrollado por Ross Quinlan, es una extensión del Espacio de Versiones que puede manejar atributos nominales 
# y numéricos, así como valores desconocidos en los datos de entrenamiento. AQ utiliza un enfoque de dividir y conquistar para construir
# un árbol de decisión que clasifique los ejemplos de manera efectiva.

# Las características principales del algoritmo AQ son:

# 1.- Trata con atributos nominales y numéricos.
# 2.- Maneja valores desconocidos (missing values).
# 3.- Construye un árbol de decisión utilizando un enfoque de dividir y conquistar.
# #--------------- PROGRAMA ------------------------------------
class EspacioVersiones:
    def __init__(self, num_atributos):
        self.hipotesis = [None] * num_atributos  # Inicializa la hipótesis como una lista de None
    
    def entrena(self, ejemplos_positivos, ejemplos_negativos):
        for ejemplo in ejemplos_positivos:  # Actualiza la hipótesis para ejemplos positivos
            for i, valor in enumerate(ejemplo):
                if self.hipotesis[i] is None:  # Si el valor no se ha definido, actualízalo
                    self.hipotesis[i] = valor
                elif self.hipotesis[i] != valor:  # Si el valor ya se ha definido y es diferente, cambia a '?'
                    self.hipotesis[i] = '?'
        
        for ejemplo in ejemplos_negativos:  # Actualiza la hipótesis para ejemplos negativos
            for i, valor in enumerate(ejemplo):
                if self.hipotesis[i] is not None and self.hipotesis[i] != valor:
                    self.hipotesis[i] = '?'  # Si el valor ya se ha definido y es diferente, cambia a '?'
    
    def clasifica(self, ejemplo):
        for i, valor in enumerate(ejemplo):
            if self.hipotesis[i] is not None and self.hipotesis[i] != valor:
                return False  # Si algún valor no coincide con la hipótesis, clasifica como negativo
        return True  # Si todos los valores coinciden, clasifica como positivo


# Ejemplo de uso del algoritmo Espacio de Versiones
ejemplos_positivos = [
    ['sol', 'calor', 'alta', 'normal'],
    ['sol', 'calor', 'alta', 'alta'],
]
ejemplos_negativos = [
    ['lluvia', 'frio', 'alta', 'normal'],
    ['lluvia', 'calor', 'normal', 'alta'],
]

# Crear una instancia del Espacio de Versiones
espacio_versiones = EspacioVersiones(num_atributos=4)

# Entrenar el Espacio de Versiones con los ejemplos
espacio_versiones.entrena(ejemplos_positivos, ejemplos_negativos)

# Clasificar nuevos ejemplos
nuevo_ejemplo1 = ['sol', 'calor', 'alta', 'normal']
print("Clasificación para el nuevo ejemplo 1:", espacio_versiones.clasifica(nuevo_ejemplo1))

nuevo_ejemplo2 = ['lluvia', 'frio', 'normal', 'alta']
print("Clasificación para el nuevo ejemplo 2:", espacio_versiones.clasifica(nuevo_ejemplo2))

#-------------------------------------------------------------------------------------------
# 1.- En el método __init__, se inicializa la hipótesis como una lista de None, con la longitud igual al número de atributos.
# 2.- En el método entrena, se actualiza la hipótesis recorriendo los ejemplos positivos y negativos. Para cada atributo en cada ejemplo, 
#     si el valor ya está definido en la hipótesis y es diferente al valor actual, se cambia a ?.
# 3.- En el método clasifica, se clasifica un nuevo ejemplo comparándolo con la hipótesis. Si algún valor no coincide, se clasifica como negativo;
#     de lo contrario, se clasifica como positivo.
# 4.- Finalmente, se muestra un ejemplo de uso del algoritmo con dos ejemplos de clasificación. El primer ejemplo debería clasificarse como 
#     positivo y el segundo como negativo.