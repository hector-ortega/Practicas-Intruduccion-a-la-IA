#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.
#-----------------TEORIA----------------------------------------

# Los algoritmos de preprocesado con filtros se utilizan para mejorar la calidad de los datos de entrada antes de ser procesados por un modelo de inteligencia 
#     artificial. Estos algoritmos son comúnmente aplicados en el procesamiento de imágenes, señales de audio, texto y otros tipos de datos.

# En el caso específico de los filtros, se utilizan para eliminar o reducir el ruido, realzar características importantes, suavizar la señal y 
#     resaltar detalles relevantes, entre otros propósitos. El objetivo principal es mejorar la calidad de los datos de entrada para que el modelo 
#     de IA pueda obtener mejores resultados durante el entrenamiento y la inferencia.

# Existen diferentes tipos de filtros que se pueden utilizar en el preprocesado de datos, algunos de los más comunes son:

# 1.- Filtros de suavizado (o de paso bajo): Estos filtros se utilizan para reducir el ruido y suavizar una señal o una imagen. El filtro de media y el 
#     filtro gaussiano son ejemplos comunes de filtros de suavizado.
# 2.- Filtros de realce (o de paso alto): Estos filtros se utilizan para resaltar bordes y detalles importantes en una imagen o señal. El filtro de Sobel
#     y el filtro de Laplace son ejemplos de filtros de realce.
# 3.- Filtros de eliminación de ruido: Estos filtros se utilizan específicamente para eliminar el ruido de una señal o imagen. El filtro de mediana y el 
#     filtro bilateral son ejemplos comunes de filtros de eliminación de ruido.
# 4.- Filtros de binarización: Estos filtros se utilizan para convertir una imagen en una imagen binaria, donde los píxeles se clasifican como blanco o 
#     negro según cierto umbral. El filtro de umbralización es un ejemplo de filtro de binarización.

#--------------- PROGRAMA --------------------------------------
import cv2
import numpy as np

def apply_mean_filter(image, kernel_size):
    """
    Aplica un filtro de media a una imagen.

    Args:
    - image: la imagen de entrada (en formato numpy array).
    - kernel_size: el tamaño del kernel del filtro (debe ser impar).

    Returns:
    - La imagen suavizada.
    """
    # Creamos un kernel de filtro de media
    kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size * kernel_size)
    
    # Aplicamos el filtro de convolución
    smoothed_image = cv2.filter2D(image, -1, kernel)
    
    return smoothed_image

# Cargamos una imagen de ejemplo
input_image = cv2.imread('input_image.jpg')

# Aplicamos el filtro de media con un tamaño de kernel de 5x5
smoothed_image = apply_mean_filter(input_image, kernel_size=5)

# Mostramos la imagen original y la imagen suavizada
cv2.imshow('Original Image', input_image)
cv2.imshow('Smoothed Image', smoothed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#---------------------------------------------------------------------
# 1.- Importamos las bibliotecas necesarias:
# - cv2: OpenCV, una biblioteca de visión por computadora.
# - numpy: NumPy, una biblioteca para operaciones matemáticas en Python.
# 2.- Definimos una función llamada apply_mean_filter que toma una imagen y un tamaño de kernel como entrada y aplica un filtro de media a la imagen.
# - Creamos un kernel de filtro de media utilizando la función np.ones para crear una matriz de unos y luego dividimos por el tamaño del kernel al cuadrado para normalizar.
# - Aplicamos el filtro de convolución utilizando la función cv2.filter2D, que realiza la convolución entre la imagen y el kernel.
# 3.- Cargamos una imagen de ejemplo utilizando cv2.imread.
# 4.- Aplicamos el filtro de media llamando a la función apply_mean_filter con la imagen de entrada y un tamaño de kernel de 5x5.
# 5.- Mostramos la imagen original y la imagen suavizada utilizando las funciones cv2.imshow, cv2.waitKey y cv2.destroyAllWindows.