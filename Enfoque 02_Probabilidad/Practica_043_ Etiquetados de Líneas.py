#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.
#-----------------TEORIA----------------------------------------
# El objetivo principal del etiquetado de líneas es identificar las regiones de una imagen que representan líneas o segmentos de líneas,
# y asignarles una etiqueta única para su posterior procesamiento o análisis. Este algoritmo se puede utilizar como paso previo en sistemas
# más complejos de reconocimiento de patrones o en aplicaciones de visión por computadora.

# El funcionamiento básico del algoritmo de etiquetado de líneas implica los siguientes pasos:

# 1.- Preprocesamiento de la imagen: La imagen de entrada se procesa para mejorar su calidad y facilitar la detección de líneas. 
#     Esto puede incluir la conversión a escala de grises, la eliminación de ruido, la corrección de la iluminación, entre otros.
# 2.- Binarización de la imagen: Se aplica un umbral a la imagen para convertirla en una imagen binaria, donde los píxeles se clasifican 
#     como blanco o negro según un valor umbral. Esto facilita la detección de bordes y líneas en la imagen.
# 3.- Detección de contornos: Se identifican los contornos en la imagen binaria utilizando técnicas como el algoritmo de detección de contornos
#     de Canny o el algoritmo de búsqueda de contornos de OpenCV.
# 4.- Etiquetado de líneas: Se identifican los segmentos de líneas en los contornos detectados y se les asigna una etiqueta única. Esto puede implicar 
#     la agrupación de píxeles contiguos que forman parte de la misma línea.
# 5.- Análisis y procesamiento de resultados: Una vez etiquetadas las líneas en la imagen, se pueden realizar diversas operaciones de análisis y 
#     procesamiento, como la extracción de características, el reconocimiento de patrones, la segmentación de objetos, entre otros.
#--------------- PROGRAMA --------------------------------------
import cv2
import numpy as np

# Función para etiquetar líneas en una imagen
def etiquetar_lineas(imagen):
    # Convertir la imagen a escala de grises
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    
    # Aplicar umbralización para binarizar la imagen
    _, umbral = cv2.threshold(gris, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # Encontrar contornos en la imagen binarizada
    contornos, jerarquia = cv2.findContours(umbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Dibujar los contornos encontrados en la imagen original
    imagen_etiquetada = imagen.copy()
    cv2.drawContours(imagen_etiquetada, contornos, -1, (0, 255, 0), 2)
    
    # Mostrar la imagen etiquetada
    cv2.imshow('Imagen etiquetada', imagen_etiquetada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Cargar la imagen de entrada
imagen = cv2.imread('imagen.png')

# Llamar a la función para etiquetar líneas
etiquetar_lineas(imagen)

#-------------------------------------------------------------------
# 1.- Importamos las bibliotecas necesarias, como OpenCV (cv2) y NumPy (np), que utilizaremos para manipular la imagen.
# 2.- Definimos una función llamada etiquetar_lineas que toma una imagen como entrada y realiza el etiquetado de líneas.
# 3.- Convertimos la imagen a escala de grises utilizando cv2.cvtColor.
# 4.- Aplicamos umbralización para binarizar la imagen utilizando el método de Otsu con cv2.threshold.
# 5.- Encontramos los contornos en la imagen binarizada utilizando cv2.findContours.
# 6.- Dibujamos los contornos encontrados en la imagen original utilizando cv2.drawContours.
# 7.- Mostramos la imagen etiquetada en una ventana utilizando cv2.imshow.
# 8.- Cargamos la imagen de entrada utilizando cv2.imread.
# 9.- Llamamos a la función etiquetar_lineas con la imagen como argumento.