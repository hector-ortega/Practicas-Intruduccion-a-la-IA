#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.
#-----------------TEORIA----------------------------------------
# El reconocimiento de escritura es una tarea importante en el campo del procesamiento de imágenes y la inteligencia artificial.
# Se utiliza para convertir imágenes de texto manuscrito en texto legible por máquina, lo que permite a las computadoras comprender 
# y procesar la información contenida en documentos escritos a mano.

# Los algoritmos de reconocimiento de escritura funcionan analizando las características de las imágenes de texto manuscrito y extrayendo 
# patrones que pueden utilizarse para identificar las letras, palabras o frases presentes en la imagen. Estos algoritmos pueden utilizar diferentes 
# enfoques y técnicas, pero en general, el proceso de reconocimiento de escritura implica las siguientes etapas:

# 1.- Preprocesamiento de la imagen: Antes de realizar el reconocimiento, es común realizar operaciones de preprocesamiento en la imagen para mejorar 
#     la calidad y facilitar la extracción de características. Esto puede incluir la eliminación de ruido, la binarización de la imagen para convertirla 
#     en blanco y negro, la normalización del tamaño y la orientación del texto, entre otros.
# 2.- Extracción de características: En esta etapa, se extraen características relevantes de la imagen que pueden utilizarse para identificar las letras 
#     o palabras presentes en ella. Esto puede incluir características como la forma de las letras, la distribución de los píxeles, la orientación de los trazos,
#     entre otros.
# 3.- Entrenamiento del modelo: En muchos casos, se utiliza un enfoque de aprendizaje automático para entrenar un modelo que pueda reconocer el texto manuscrito. 
#     Se proporciona al modelo un conjunto de datos de entrenamiento que consiste en imágenes de texto manuscrito junto con las etiquetas correspondientes
#     (es decir, el texto escrito en las imágenes). El modelo aprende a asociar las características de las imágenes con las etiquetas durante el entrenamiento.
# 4.- Clasificación o reconocimiento: Una vez que el modelo está entrenado, se utiliza para clasificar nuevas imágenes de texto manuscrito. 
#     El modelo analiza las características de la imagen y predice la etiqueta correspondiente, es decir, el texto representado en la imagen.
# 5.- Postprocesamiento: Finalmente, es posible realizar operaciones de postprocesamiento en la salida del modelo para mejorar la precisión del reconocimiento.
#     Esto puede incluir la corrección de errores ortográficos, la eliminación de caracteres incorrectos o la combinación de caracteres reconocidos en palabras
#     o frases coherentes.
#--------------- PROGRAMA --------------------------------------
# Importar las bibliotecas necesarias
import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Descargar el conjunto de datos MNIST
mnist = fetch_openml('mnist_784')

# Dividir los datos en características (X) y etiquetas (y)
X, y = mnist.data, mnist.target

# Dividir los datos en conjunto de entrenamiento y conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializar el clasificador k-NN con un valor de k=5
knn_classifier = KNeighborsClassifier(n_neighbors=5)

# Entrenar el clasificador utilizando el conjunto de entrenamiento
knn_classifier.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = knn_classifier.predict(X_test)

# Calcular la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del modelo:", accuracy)

#-------------------------------------------------------------------
# 1.- Importamos las bibliotecas necesarias, incluyendo NumPy para operaciones numéricas, fetch_openml de scikit-learn para obtener el conjunto de datos MNIST, 
#     y KNeighborsClassifier para implementar el clasificador de vecinos más cercanos.
# 2.- Descargamos el conjunto de datos MNIST, que contiene imágenes de dígitos escritos a mano junto con sus etiquetas correspondientes.
# 3.- Dividimos los datos en características (las imágenes de los dígitos) y etiquetas (los dígitos representados en las imágenes).
# 4.- Dividimos los datos en un conjunto de entrenamiento y un conjunto de prueba utilizando la función train_test_split.
# 5.- Inicializamos el clasificador k-NN con un valor de k igual a 5.
# 6.- Entrenamos el clasificador utilizando el conjunto de entrenamiento utilizando el método fit.
# 7.- Realizamos predicciones en el conjunto de prueba utilizando el método predict.
# 8.- Calculamos la precisión del modelo comparando las etiquetas verdaderas del conjunto de prueba con las predicciones realizadas por el
#     modelo utilizando la función accuracy_score.
# 9.- Imprimimos la precisión del modelo.