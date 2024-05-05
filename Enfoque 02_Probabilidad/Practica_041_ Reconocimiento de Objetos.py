#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.
#-----------------TEORIA----------------------------------------
# El reconocimiento de objetos es una tarea fundamental en el campo de la visión por computadora e inteligencia artificial. 
# Consiste en identificar y localizar objetos específicos dentro de imágenes o videos. Se utiliza en una amplia gama de aplicaciones, como:

# 1.- Seguridad y vigilancia: Para detectar personas, vehículos u objetos sospechosos en entornos de seguridad.
# 2.- Automatización industrial: Para inspeccionar y clasificar productos en líneas de producción.
# 3.- Reconocimiento facial: Para identificar y reconocer caras en imágenes y videos.
# 4.- Conducción autónoma: Para detectar peatones, vehículos y señales de tráfico en tiempo real.
# 5.- Aplicaciones médicas: Para identificar y localizar estructuras anatómicas en imágenes médicas, como radiografías y tomografías computarizadas.
# 6.- Interacción humano-computadora: Para permitir la interacción natural entre humanos y dispositivos electrónicos, como la detección de gestos y movimientos.
#--------------- PROGRAMA --------------------------------------
import cv2

# Cargamos el clasificador Haar preentrenado para detección de caras
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Cargamos la imagen en la que queremos detectar caras
image = cv2.imread('face_image.jpg')

# Convertimos la imagen a escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detectamos caras en la imagen
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Dibujamos rectángulos alrededor de las caras detectadas
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Mostramos la imagen con las caras detectadas
cv2.imshow('Detected Faces', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#-------------------------------------------------------------------
# Línea 3: Importamos la biblioteca OpenCV, que nos proporciona herramientas para procesamiento de imágenes y visión por computadora.
# Línea 6: Cargamos el clasificador Haar preentrenado para la detección de caras. Este archivo XML contiene información sobre cómo detectar caras en una imagen.
# Línea 9: Cargamos la imagen en la que queremos detectar caras. Asegúrate de tener una imagen válida en el mismo directorio que este script, o cambia 
#  la ruta de la imagen en la línea 9.
# Línea 12: Convertimos la imagen a escala de grises. La detección de caras suele funcionar mejor en imágenes en escala de grises.
# Línea 15: Utilizamos el método detectMultiScale del clasificador Haar para detectar caras en la imagen. Este método devuelve una lista de rectángulos
#  que representan las posiciones de las caras detectadas en la imagen.
# Líneas 18-21: Iteramos sobre la lista de rectángulos y dibujamos un rectángulo alrededor de cada cara detectada en la imagen original.
# Línea 24: Mostramos la imagen resultante con los rectángulos dibujados alrededor de las caras detectadas. La función imshow muestra la imagen en una ventana,
#  waitKey(0) espera hasta que se presione una tecla y destroyAllWindows() cierra todas las ventanas abiertas.