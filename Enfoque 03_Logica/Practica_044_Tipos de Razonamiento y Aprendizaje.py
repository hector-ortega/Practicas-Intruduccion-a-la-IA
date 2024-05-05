#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# Los algoritmos de "Tipos de Razonamiento y Aprendizaje" se utilizan en el campo de la inteligencia artificial para abordar diferentes tipos 
# de problemas de manera automatizada. Estos algoritmos se basan en principios de lógica, inferencia, aprendizaje y representación del 
# conocimiento para realizar tareas como clasificación, predicción, toma de decisiones y resolución de problemas.
#--------------- PROGRAMA ------------------------------------
# Paso 1: Importar las bibliotecas necesarias
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Paso 2: Cargar el conjunto de datos Iris
iris = load_iris()
X = iris.data  # Características de las flores
y = iris.target  # Etiquetas de las flores

# Paso 3: Dividir el conjunto de datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Paso 4: Crear un clasificador SVM
svm_classifier = SVC(kernel='linear', random_state=42)

# Paso 5: Entrenar el clasificador SVM
svm_classifier.fit(X_train, y_train)

# Paso 6: Realizar predicciones en el conjunto de prueba
y_pred = svm_classifier.predict(X_test)

# Paso 7: Calcular la precisión del clasificador
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del clasificador SVM: {:.2f}".format(accuracy))

#----------------------------------------------------------------------
# Paso 1: Importamos las bibliotecas necesarias. Utilizamos NumPy para el manejo de matrices y vectores, scikit-learn para cargar el conjunto de datos Iris, dividir los datos en conjuntos de entrenamiento y prueba, crear el clasificador SVM y evaluar su precisión.
# Paso 2: Cargamos el conjunto de datos Iris, que contiene características de las flores y las etiquetas correspondientes.
# Paso 3: Dividimos el conjunto de datos en conjuntos de entrenamiento (80%) y prueba (20%).
# Paso 4: Creamos un clasificador SVM utilizando el kernel lineal y fijamos una semilla aleatoria para la reproducibilidad de los resultados.
# Paso 5: Entrenamos el clasificador SVM utilizando los datos de entrenamiento.
# Paso 6: Realizamos predicciones en el conjunto de prueba utilizando el clasificador entrenado.
# Paso 7: Calculamos la precisión del clasificador comparando las etiquetas verdaderas del conjunto de prueba con las etiquetas predichas por el clasificador.