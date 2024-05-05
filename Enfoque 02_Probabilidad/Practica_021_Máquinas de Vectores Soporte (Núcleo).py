#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.
#-----------------TEORIA----------------------------------------

# Las Máquinas de Vectores de Soporte (SVM) son un poderoso algoritmo de aprendizaje supervisado utilizado tanto para clasificación 
# como para regresión. La idea principal detrás de SVM es encontrar un hiperplano en un espacio de características que mejor separe las
# clases de datos.

# Funcionamiento de las Máquinas de Vectores de Soporte (SVM):

# 1.- Definición del Hiperplano de Separación:
# En un problema de clasificación binaria, SVM busca encontrar un hiperplano en un espacio de características que 
# mejor separe las dos clases. Este hiperplano se define como la frontera de decisión que maximiza el margen entre las clases.
# 2.- Selección del Hiperplano Óptimo:
# SVM busca encontrar el hiperplano óptimo que maximice el margen entre las clases. El margen es la distancia perpendicular desde 
# el hiperplano a los puntos de datos más cercanos de cada clase, conocidos como vectores de soporte. Maximizar el margen ayuda a SVM a 
# generalizar mejor con datos nuevos.
# 3.- Uso de Núcleos:
# En muchos casos, los datos no son linealmente separables en el espacio de características original. En tales casos, SVM utiliza una 
# técnica llamada "kernel trick" para proyectar los datos en un espacio dimensional superior donde sí puedan ser separados linealmente.
# Algunos tipos comunes de núcleos son el núcleo lineal, polinomial y gaussiano (RBF).
# 4.- Entrenamiento del Modelo:
# Una vez que se ha seleccionado el núcleo y se ha definido el problema, SVM resuelve un problema de optimización para encontrar el 
# iperplano óptimo que mejor separa las clases de datos.
# 5.- Predicción:
# Una vez que el modelo SVM ha sido entrenado, puede utilizarse para hacer predicciones sobre nuevos datos. El modelo clasifica los nuevos datos
# según el lado del hiperplano en el que caigan.

#--------------- PROGRAMA --------------------------------------
# Paso 1: Importar las bibliotecas necesarias
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Paso 2: Generar datos de ejemplo
X, y = make_classification(n_samples=100, n_features=2, n_classes=2, 
                           n_clusters_per_class=1, n_redundant=0, random_state=42)

# Paso 3: Dividir los datos en conjunto de entrenamiento y conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Paso 4: Crear y entrenar el modelo SVM con un kernel
svm_model = SVC(kernel='rbf', random_state=42)
svm_model.fit(X_train, y_train)

# Paso 5: Realizar predicciones sobre el conjunto de prueba
y_pred = svm_model.predict(X_test)

# Paso 6: Calcular la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del modelo SVM con kernel RBF:", accuracy)
#--------------------------------------------------------------------------------------------------------------
# 1.- Importar las bibliotecas necesarias: Importamos las bibliotecas que necesitaremos, incluyendo funciones para generar datos de ejemplo, 
#     dividir los datos en conjuntos de entrenamiento y prueba, crear el modelo SVM y calcular la precisión del modelo.
# 2.- Generar datos de ejemplo: Utilizamos la función make_classification de scikit-learn para generar datos de ejemplo con dos características 
#     y dos clases.
# 3.- Dividir los datos: Dividimos los datos generados en conjuntos de entrenamiento y prueba utilizando la función train_test_split de scikit-learn.
# 4.- Crear y entrenar el modelo SVM: Creamos un modelo SVM utilizando la clase SVC de scikit-learn y especificamos el tipo de kernel
#     que queremos utilizar (en este caso, 'rbf' para un kernel gaussiano). Luego, entrenamos el modelo utilizando el conjunto de entrenamiento.
# 5.- Realizar predicciones: Utilizamos el modelo entrenado para realizar predicciones sobre el conjunto de prueba.
# 6.- Calcular la precisión del modelo: Calculamos la precisión del modelo utilizando la función accuracy_score de scikit-learn, 
#     que compara las etiquetas verdaderas con las etiquetas predichas y devuelve la fracción de clasificaciones correctas.
