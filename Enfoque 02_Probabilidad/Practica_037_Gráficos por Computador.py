#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.
#-----------------TEORIA----------------------------------------

# Los gráficos por computadora son un área de la informática que se enfoca en la generación y visualización de imágenes digitales en una pantalla de 
# computadora o dispositivo similar. Estas imágenes pueden representar objetos tridimensionales, escenas bidimensionales, datos científicos, 
# gráficos estadísticos y mucho más. Los algoritmos de gráficos por computadora se utilizan en una amplia gama de aplicaciones, que van desde los 
# videojuegos y la animación hasta la visualización de datos científicos y médicos.

#--------------- PROGRAMA --------------------------------------
import matplotlib.pyplot as plt

# Datos para el gráfico
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Crear el gráfico
plt.plot(x, y, marker='o', linestyle='-', color='b', label='Datos')

# Añadir etiquetas y título
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Gráfico de ejemplo')

# Añadir una leyenda
plt.legend()

# Mostrar el gráfico
plt.show()

#---------------------------------------------------------------------
# 1.- mportación de la biblioteca: Importamos la biblioteca Matplotlib con el alias plt para poder acceder a sus funciones.
# 2.- Definición de datos: Creamos dos listas x y y, que representan los valores de los ejes x e y, respectivamente.
# 3.- Crear el gráfico: Utilizamos la función plot() de Matplotlib para trazar los puntos (x, y). Especificamos el marcador (marker), el estilo de línea 
#     (linestyle), el color (color) y una etiqueta (label) para el gráfico.
# 4.- Añadir etiquetas y título: Utilizamos las funciones xlabel(), ylabel() y title() para añadir etiquetas a los ejes y un título al gráfico.
# 5.- Añadir una leyenda: Utilizamos la función legend() para añadir una leyenda al gráfico, que mostrará la etiqueta especificada en el paso anterior.
# 6.- Mostrar el gráfico: Utilizamos la función show() para mostrar el gráfico en una ventana emergente.