#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.
#-----------------TEORIA----------------------------------------
#Funcionamiento:
# El algoritmo de verificación de separabilidad lineal busca una línea, plano o hiperplano en un espacio de características que pueda separar 
# perfectamente las muestras de las diferentes clases. Esto significa que todas las muestras de una clase están en un lado de la línea 
# (o plano o hiperplano) y todas las muestras de la otra clase están en el lado opuesto.

# Para verificar la separabilidad lineal, el algoritmo puede trazar una línea entre los puntos extremos de las dos clases en un 
# espacio de características bidimensional. Si es posible trazar una línea que separe completamente las clases, entonces los datos
# son linealmente separables. Si no es posible, los datos no son linealmente separables.
#--------------- PROGRAMA --------------------------------------
import numpy as np
import matplotlib.pyplot as plt

def check_linear_separability(X, y):
    """
    Verifica la separabilidad lineal de un conjunto de datos.

    Parameters:
    X : numpy array
        Matriz de características de entrada.
    y : numpy array
        Vector de etiquetas de clase.

    Returns:
    bool
        True si los datos son linealmente separables, False de lo contrario.
    """
    # Verifica si al menos hay dos clases
    if len(np.unique(y)) < 2:
        print("No se pueden verificar la separabilidad lineal con menos de dos clases.")
        return False

    # Verifica la dimensión de las características
    if X.shape[1] != 2:
        print("Este algoritmo solo admite conjuntos de datos bidimensionales.")
        return False

    # Divide el conjunto de datos en dos clases
    class_1 = X[y == 1]
    class_2 = X[y == -1]

    # Grafica las clases
    plt.scatter(class_1[:, 0], class_1[:, 1], color='blue', marker='o', label='Clase 1')
    plt.scatter(class_2[:, 0], class_2[:, 1], color='red', marker='s', label='Clase 2')

    # Añade etiquetas y leyenda
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.title('Linear Separability Check')
    plt.legend(loc='upper left')

    # Verifica la separabilidad lineal trazando una línea entre los puntos más extremos de cada clase
    min_x1, max_x1 = np.min(X[:, 0]), np.max(X[:, 0])
    min_x2, max_x2 = np.min(X[:, 1]), np.max(X[:, 1])
    plt.plot([min_x1, max_x1], [min_x2, max_x2], color='black', linestyle='--')

    # Muestra la gráfica
    plt.show()

    # Comprueba si la línea separa completamente las clases
    if np.all(np.sign(np.dot(class_1, [max_x1 - min_x1, max_x2 - min_x2])) == 1) \
            and np.all(np.sign(np.dot(class_2, [max_x1 - min_x1, max_x2 - min_x2])) == -1):
        print("Los datos son linealmente separables.")
        return True
    else:
        print("Los datos no son linealmente separables.")
        return False

# Ejemplo de uso
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]])
y = np.array([1, 1, 1, -1, -1, -1])

check_linear_separability(X, y)
#-----------------------------------------------------------------------------------------------
# 1.- La función check_linear_separability toma un conjunto de datos X y las etiquetas de clase y y verifica si son linealmente separables.
# 2.- Primero, verifica si hay al menos dos clases y si el conjunto de datos es bidimensional.
# 3.- Luego, divide los datos en dos clases y los grafica utilizando diferentes colores para cada clase.
# 4.- Traza una línea entre los puntos más extremos de cada clase para verificar la separabilidad lineal. Si una línea puede separar 
#     completamente las clases, entonces los datos son linealmente separables.
# 5.-  Finalmente, muestra el gráfico y devuelve True si los datos son linealmente separables, False de lo contrario.