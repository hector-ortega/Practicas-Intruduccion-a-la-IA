#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# Los algoritmos de "Explicaciones e Información Relevante" son herramientas utilizadas en inteligencia artificial para comprender y explicar cómo los 
# modelos toman decisiones basadas en datos. Estos algoritmos son especialmente importantes en aplicaciones donde la transparencia y la interpretabilidad
# del modelo son críticas, como en la medicina, la justicia penal y el crédito bancario, entre otros.

# El propósito principal de estos algoritmos es proporcionar explicaciones comprensibles y relevantes sobre las decisiones del modelo,
# lo que permite a los usuarios humanos entender cómo se llegó a una determinada predicción o decisión. Esto puede ayudar a validar la
# confiabilidad del modelo, detectar sesgos o errores, y mejorar la confianza en su uso.

# Los algoritmos de explicación pueden tomar diferentes formas dependiendo del tipo de modelo y del contexto de aplicación. Algunos enfoques comunes incluyen:

# 1.- Métodos basados en reglas: Estos métodos generan reglas lógicas simples que explican cómo se toman las decisiones del modelo. 
#     Por ejemplo, un árbol de decisión puede ser fácilmente interpretable y proporcionar reglas claras para la clasificación de datos.
# 3.- Métodos basados en importancia de características: Estos métodos identifican las características más importantes para la toma de decisiones del modelo. 
#     Por ejemplo, los algoritmos de bosques aleatorios y de gradient boosting pueden proporcionar información sobre la importancia relativa de cada
#     característica en la predicción.
# 4.- Métodos de visualización: Estos métodos representan visualmente las decisiones del modelo para facilitar su comprensión. 
#     Por ejemplo, los mapas de calor y los gráficos de dispersión pueden ser útiles para visualizar patrones en los datos y explicar cómo 
#     el modelo los utiliza para tomar decisiones.

#--------------- PROGRAMA ------------------------------------
# Importamos las librerías necesarias
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Cargamos el conjunto de datos Iris
iris = load_iris()
X = iris.data
y = iris.target

# Dividimos el conjunto de datos en datos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creamos el clasificador de árbol de decisión
clf = DecisionTreeClassifier(random_state=42)

# Entrenamos el modelo
clf.fit(X_train, y_train)

# Evaluamos la precisión del modelo en los datos de prueba
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Explicación de la predicción para un ejemplo de prueba
sample_index = 0
sample = X_test[sample_index].reshape(1, -1)
prediction = clf.predict(sample)[0]

# Mostramos la predicción
print("Predicted class:", prediction)

# Obtenemos las características (features) utilizadas por el modelo
features = iris.feature_names

# Mostramos las características utilizadas por el modelo
print("Features:", features)

# Mostramos el valor de cada característica para el ejemplo de prueba
print("Sample values:", sample)

# Mostramos la ruta de decisión seguida por el modelo para esta predicción
path = clf.decision_path(sample)
print("Decision path:", path)

# Mostramos las características más importantes para la predicción
importance = clf.feature_importances_
print("Feature importance:", importance)

#------------------------------------------------------------------------
# 1.- Importamos las bibliotecas necesarias, incluyendo los conjuntos de datos de Iris, el clasificador de árbol de decisión, 
#     las funciones para dividir el conjunto de datos y evaluar el modelo, y las métricas de precisión.
# 2.- Cargamos el conjunto de datos Iris.
# 3.- Dividimos los datos en conjuntos de entrenamiento y prueba.
# 4.- Creamos un clasificador de árbol de decisión.
# 5.- Entrenamos el modelo utilizando los datos de entrenamiento.
# 6.- Evaluamos la precisión del modelo utilizando los datos de prueba.
# 7.- Seleccionamos un ejemplo de prueba y realizamos una predicción con el modelo.
# 8.- Mostramos la predicción y las características utilizadas por el modelo.
# 9.- Mostramos los valores de las características para el ejemplo de prueba.
# 10.- Mostramos la ruta de decisión seguida por el modelo para esta predicción.
# 11.- Mostramos la importancia de cada característica para la predicción.