#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.
#-----------------TEORIA----------------------------------------
# 1.- Detección de Texturas:
# - La detección de texturas se refiere al proceso de identificar y resaltar regiones en una imagen que exhiben ciertas características texturales,
#     como patrones repetitivos, variaciones de color o contraste.
# - Estos algoritmos suelen basarse en el análisis de la distribución de los valores de píxeles en la imagen, la frecuencia de las transiciones de 
#   intensidad y la estructura local de la imagen.
# - Un enfoque común para la detección de texturas es utilizar operadores de filtrado, como el filtro de Sobel, para resaltar bordes y 
#   gradientes en la imagen. También se pueden utilizar técnicas de transformación de Fourier para analizar la frecuencia de los componentes 
#   de la imagen y detectar patrones texturales.
# - La detección de texturas es útil en una variedad de aplicaciones, como la clasificación de objetos en imágenes, la segmentación de regiones de 
#   interés y el reconocimiento de patrones.

# 2.- Detección de Sombras:
# - La detección de sombras se refiere al proceso de identificar y separar las regiones oscuras en una imagen que pueden ser causadas por la presencia de sombras.
# - Estos algoritmos suelen basarse en técnicas de umbralización para segmentar áreas con bajos niveles de intensidad en la imagen.
# - Las sombras pueden causar problemas en aplicaciones de visión por computadora, como la detección de objetos o la estimación de la forma, ya que pueden 
#   alterar la apariencia de los objetos y afectar negativamente la precisión de los algoritmos de procesamiento de imágenes.
# - La detección y eliminación de sombras es importante para mejorar la calidad de las imágenes y garantizar la precisión de los sistemas de visión por 
#   computadora en una variedad de aplicaciones, como la vigilancia, la conducción autónoma y la robótica.
#--------------- PROGRAMA --------------------------------------
import cv2
import numpy as np

# Función para detectar texturas en la imagen
def detect_texture(image):
    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Calcular el gradiente de la imagen utilizando el operador Sobel
    grad_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    
    # Calcular la magnitud del gradiente
    grad_magnitude = np.sqrt(grad_x**2 + grad_y**2)
    
    # Normalizar la magnitud del gradiente para resaltar las texturas
    normalized_gradient = cv2.normalize(grad_magnitude, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    
    return normalized_gradient

# Función para detectar sombras en la imagen
def detect_shadows(image):
    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Aplicar umbralización para detectar áreas oscuras (posibles sombras)
    _, thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY_INV)
    
    return thresh

# Cargar la imagen
image_path = 'tu_imagen.jpg'  # Cambia 'tu_imagen.jpg' por la ruta de tu imagen
image = cv2.imread(image_path)

# Detectar texturas en la imagen
texture_image = detect_texture(image)

# Detectar sombras en la imagen
shadow_image = detect_shadows(image)

# Mostrar la imagen original y las imágenes resaltadas de texturas y sombras
cv2.imshow('Original', image)
cv2.imshow('Texturas', texture_image)
cv2.imshow('Sombras', shadow_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#----------------------------------------------------------------------------------------------
# 1.- Importamos las bibliotecas necesarias: cv2 para el procesamiento de imágenes y numpy para operaciones numéricas.
# 2.- Definimos una función detect_texture(image) para detectar texturas en la imagen utilizando el gradiente de la imagen.
# 3.- Dentro de detect_texture(), convertimos la imagen a escala de grises y calculamos el gradiente utilizando el operador Sobel.
# 4.- Calculamos la magnitud del gradiente y la normalizamos para resaltar las texturas.
# 5.- Definimos una función detect_shadows(image) para detectar sombras en la imagen utilizando umbralización.
# 6.- Dentro de detect_shadows(), convertimos la imagen a escala de grises y aplicamos umbralización para detectar áreas oscuras.
# 7.- Cargamos la imagen de entrada, llamamos a las funciones de detección de texturas y sombras, y mostramos las imágenes resultantes junto con la imagen original.