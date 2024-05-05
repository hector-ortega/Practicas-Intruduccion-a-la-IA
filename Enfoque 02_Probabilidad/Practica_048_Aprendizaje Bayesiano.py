#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.
#-----------------TEORIA----------------------------------------

# El Aprendizaje Bayesiano es un enfoque estadístico para la inferencia y la toma de decisiones que se basa en el teorema de Bayes. 
# Este teorema proporciona un marco para actualizar nuestras creencias sobre la probabilidad de un evento en función de la evidencia observada. 
# En el contexto del aprendizaje automático, el Aprendizaje Bayesiano se utiliza para modelar la incertidumbre y tomar decisiones basadas en esta incertidumbre.

# En el aprendizaje bayesiano, representamos nuestras creencias sobre los parámetros de un modelo mediante distribuciones de probabilidad. Luego, 
# actualizamos estas creencias a medida que observamos datos mediante el teorema de Bayes. Esto nos permite obtener una distribución posterior sobre 
# los parámetros del modelo, que combina nuestras creencias iniciales con la evidencia observada.

# El Aprendizaje Bayesiano se utiliza en una variedad de aplicaciones, incluyendo la clasificación, la regresión, el agrupamiento y la toma de decisiones.
# Algunos de los principales beneficios del Aprendizaje Bayesiano incluyen su capacidad para manejar la incertidumbre de manera natural, su capacidad para 
# manejar conjuntos de datos pequeños y su flexibilidad para modelar relaciones complejas entre las variables.
#--------------- PROGRAMA --------------------------------------
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Cargar el conjunto de datos Iris
iris = load_iris()
X = iris.data
y = iris.target

# Dividir el conjunto de datos en datos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el clasificador Naive Bayes
clf = GaussianNB()

# Entrenar el clasificador con los datos de entrenamiento
clf.fit(X_train, y_train)

# Predecir las etiquetas de clase para los datos de prueba
y_pred = clf.predict(X_test)

# Calcular la precisión del clasificador
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del clasificador Naive Bayes:", accuracy)

#------------------------------------------------------------------
# 1.- import numpy as np: Importamos la biblioteca numpy y la renombramos como np. Numpy es una biblioteca popular en Python para operaciones numéricas eficientes.
# 2.- from sklearn.datasets import load_iris: Importamos la función load_iris desde el módulo datasets de scikit-learn. Esta función nos permite
#     cargar el conjunto de datos Iris.
# 3.- from sklearn.model_selection import train_test_split: Importamos la función train_test_split desde el módulo model_selection de scikit-learn.
#     Esta función nos permite dividir el conjunto de datos en datos de entrenamiento y prueba.
# 4.- from sklearn.naive_bayes import GaussianNB: Importamos la clase GaussianNB desde el módulo naive_bayes de scikit-learn. Esta clase implementa 
#     el clasificador bayesiano ingenuo.
# 5.- from sklearn.metrics import accuracy_score: Importamos la función accuracy_score desde el módulo metrics de scikit-learn. Esta función nos 
#     permite calcular la precisión del clasificador.
# 6.- iris = load_iris(): Cargamos el conjunto de datos Iris en la variable iris.
# 7.- X = iris.data y y = iris.target: Extraemos las características y las etiquetas de clase del conjunto de datos Iris y las almacenamos en 
#     las variables X e y respectivamente.
# 8.- X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42): Dividimos el conjunto de datos en datos de
#     entrenamiento y prueba utilizando la función train_test_split. El parámetro test_size=0.2 indica que el 20% de los datos se utilizarán 
#     como datos de prueba, mientras que el 80% se utilizarán como datos de entrenamiento. El parámetro random_state=42 se utiliza para garantizar 
#     la reproducibilidad de la división.
# 9.- clf = GaussianNB(): Creamos una instancia del clasificador Naive Bayes.
# 10.- clf.fit(X_train, y_train): Entrenamos el clasificador con los datos de entrenamiento utilizando el método fit.
# 11.- y_pred = clf.predict(X_test): Predecimos las etiquetas de clase para los datos de prueba utilizando el método predict.
# 12.- accuracy = accuracy_score(y_test, y_pred): Calculamos la precisión del clasificador comparando las etiquetas de clase reales (y_test) 
#     con las etiquetas de clase predichas (y_pred) utilizando la función accuracy_score.
# 13.- print("Precisión del clasificador Naive Bayes:", accuracy): Imprimimos la precisión del clasificador Naive Bayes en la consola.