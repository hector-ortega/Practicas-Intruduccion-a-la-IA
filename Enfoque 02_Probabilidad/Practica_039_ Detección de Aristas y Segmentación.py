#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.
#-----------------TEORIA----------------------------------------
# El algoritmo de detección de aristas y segmentación es una técnica fundamental en el procesamiento de imágenes que se utiliza 
# para identificar los bordes y las regiones de interés en una imagen. 

# Detección de Aristas:
# La detección de aristas es el proceso de identificar los bordes en una imagen, donde un borde es una transición significativa en la intensidad de los píxeles. Los algoritmos de detección de aristas son críticos para muchas aplicaciones de visión por computadora, como la segmentación de objetos, el reconocimiento de patrones y el seguimiento de objetos en movimiento.

# El algoritmo más comúnmente utilizado para la detección de aristas es el operador de Canny. Este algoritmo funciona de la siguiente manera:

# 1.- Suavizado de la imagen: La imagen original se suaviza utilizando un filtro gaussiano para reducir el ruido y las pequeñas variaciones de intensidad.
# 2.- Cálculo del gradiente de intensidad: Se calcula el gradiente de intensidad de la imagen suavizada para determinar la dirección y 
#     la magnitud del cambio de intensidad en cada píxel.
# 3.- Supresión de no máximos: Se realiza una supresión de no máximos para eliminar los píxeles que no son máximos locales en la dirección del gradiente.
# 4.- Umbralización por histéresis: Se utilizan dos umbrales para identificar los bordes débiles y los bordes fuertes. Los píxeles por 
#     encima del umbral alto se consideran bordes fuertes, mientras que los píxeles entre los umbrales alto y bajo se consideran bordes débiles. 
#     Los bordes débiles se mantienen solo si están conectados a bordes fuertes.

# Segmentación:
# La segmentación es el proceso de dividir una imagen en regiones o segmentos con características similares. La segmentación puede ser utilizada 
# para identificar objetos y separarlos del fondo, o para dividir una imagen en partes significativas para análisis posteriores.

# La umbralización es una técnica comúnmente utilizada para la segmentación, donde se aplica un umbral a la imagen para separar los píxeles en dos clases: 
# aquellos que están por encima del umbral (foreground) y aquellos que están por debajo del umbral (background).

#--------------- PROGRAMA --------------------------------------
import cv2
import numpy as np

# Cargar la imagen
image = cv2.imread('imagen.jpg', 0)  # Lee la imagen en escala de grises

# Aplicar el detector de bordes Canny
edges = cv2.Canny(image, 100, 200)  # Umbral mínimo y máximo para el detector de bordes

# Realizar la segmentación utilizando la técnica de umbralización
ret, thresholded = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Mostrar las imágenes resultantes
cv2.imshow('Original Image', image)
cv2.imshow('Canny Edges', edges)
cv2.imshow('Thresholded Image', thresholded)

# Esperar a que se presione una tecla y cerrar las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()

#---------------------------------------------------------------------
# 1.-Importamos las bibliotecas necesarias, incluyendo OpenCV (cv2) y NumPy.
# 2.- Cargamos la imagen en escala de grises utilizando la función cv2.imread(). Asegúrate de cambiar 'imagen.jpg' por la ruta de tu propia imagen.
# 3.- Aplicamos el detector de bordes Canny utilizando la función cv2.Canny(). Los dos últimos parámetros son los umbrales mínimo y máximo para el detector de bordes.
# 4.- Realizamos la segmentación utilizando la técnica de umbralización. En este caso, simplemente binarizamos la imagen utilizando un umbral fijo.
# 5.- Mostramos las imágenes resultantes utilizando la función cv2.imshow().
# 6.- Esperamos a que se presione una tecla y luego cerramos todas las ventanas utilizando cv2.waitKey() y cv2.destroyAllWindows() respectivamente.