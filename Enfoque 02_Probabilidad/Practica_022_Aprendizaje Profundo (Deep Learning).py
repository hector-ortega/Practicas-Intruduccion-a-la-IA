#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.
#-----------------TEORIA----------------------------------------
# El aprendizaje profundo, también conocido como deep learning, es una rama del aprendizaje automático que se enfoca en el entrenamiento de 
# modelos de inteligencia artificial (IA) basados en redes neuronales artificiales con múltiples capas intermedias. Estos modelos son capaces 
# de aprender representaciones de datos cada vez más abstractas y complejas a medida que se profundiza en las capas de la red. El aprendizaje 
# profundo ha demostrado ser extremadamente efectivo en una amplia gama de tareas de inteligencia artificial, incluyendo reconocimiento de imágenes,
# procesamiento del lenguaje natural, reconocimiento de voz y más

# Características del Aprendizaje Profundo:
# 1.- Capas Intermedias: Una característica fundamental del aprendizaje profundo es la presencia de múltiples capas intermedias 
#   (también conocidas como capas ocultas) entre la capa de entrada y la capa de salida de una red neuronal. Estas capas intermedias 
#   permiten que el modelo aprenda representaciones jerárquicas de los datos, lo que facilita la extracción de características complejas 
#   y la realización de tareas de aprendizaje más sofisticadas.
# 2.- Aprendizaje Jerárquico: A medida que se profundiza en las capas de la red neuronal, las características aprendidas se vuelven cada
#   vez más abstractas y de alto nivel. Esto permite que el modelo aprenda y capture patrones y estructuras de los datos en diferentes niveles
#   de abstracción, lo que lo hace extremadamente efectivo para tareas de procesamiento de datos complejas.
# 3.- Modelos No Lineales y Flexibles: Las redes neuronales profundas son inherentemente modelos no lineales y altamente flexibles.
#   Esto les permite aprender y modelar relaciones complejas y no lineales entre las entradas y las salidas, lo que los hace adecuados
#   para una amplia gama de aplicaciones de aprendizaje automático.
#--------------- PROGRAMA --------------------------------------
# Paso 1: Importar las bibliotecas necesarias
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist

# Paso 2: Cargar y preparar los datos
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
train_images, test_images = train_images / 255.0, test_images / 255.0

# Paso 3: Definir la arquitectura del modelo
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),          # Capa de entrada: aplanar la imagen 28x28 a un vector de 784 elementos
    layers.Dense(128, activation='relu'),         # Capa oculta: 128 neuronas con función de activación ReLU
    layers.Dropout(0.2),                          # Dropout para regularización
    layers.Dense(10, activation='softmax')        # Capa de salida: 10 neuronas con función de activación softmax para clasificación
])

# Paso 4: Compilar el modelo
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',   # Función de pérdida para clasificación multiclase
              metrics=['accuracy'])

# Paso 5: Entrenar el modelo
model.fit(train_images, train_labels, epochs=5)

# Paso 6: Evaluar el modelo
test_loss, test_acc = model.evaluate(test_images, test_labels)
print('\nPrecisión en el conjunto de prueba:', test_acc)

#--------------------------------------------------------------------------------------------
# 1.- Importar las bibliotecas necesarias: Importamos TensorFlow y otras bibliotecas necesarias.
# 2.- Cargar y preparar los datos: Cargamos el conjunto de datos MNIST, que contiene imágenes de dígitos escritos a mano. Luego, 
#     normalizamos los valores de píxeles al rango [0, 1].
# 3.- Definir la arquitectura del modelo: Creamos un modelo secuencial, que es una pila lineal de capas. La primera capa Flatten 
#     convierte cada imagen 28x28 en un vector de 784 elementos. Luego, agregamos una capa densa (totalmente conectada) con 128 neuronas 
#     y función de activación ReLU. Después, aplicamos dropout para regularizar el modelo y prevenir el sobreajuste. Finalmente, añadimos una
#     capa densa de salida con 10 neuronas (una para cada clase) y función de activación softmax para obtener las probabilidades de cada clase.
# 4.- Compilar el modelo: Configuramos el proceso de entrenamiento del modelo especificando el optimizador, la función de pérdida y
#     las métricas que queremos calcular.
# 5.- Entrenar el modelo: Entrenamos el modelo con los datos de entrenamiento.
# 6.- Evaluar el modelo: Evaluamos el rendimiento del modelo en el conjunto de prueba y mostramos la precisión.