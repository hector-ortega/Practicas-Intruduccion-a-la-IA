#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.
#-----------------TEORIA----------------------------------------

# El reconocimiento del habla es una tecnología que permite a las computadoras interpretar y comprender el lenguaje humano hablado. 
# Se utiliza en una variedad de aplicaciones, como asistentes virtuales, sistemas de navegación, sistemas de dictado de voz, control
# de voz para dispositivos electrónicos, entre otros.

# El funcionamiento básico de un algoritmo de reconocimiento del habla implica los siguientes pasos:

# 1.- Captura de audio: El primer paso es capturar la señal de audio que contiene el habla humana. Esta señal puede provenir de varios dispositivos,
#     como micrófonos o archivos de audio grabados previamente.
# 2.- Preprocesamiento de audio: Antes de que el habla pueda ser procesada por el algoritmo de reconocimiento, a menudo se realiza un preprocesamiento 
#     de la señal de audio. Esto puede incluir la eliminación de ruido, la normalización de la amplitud y la segmentación de la señal en unidades más pequeñas,
#     como tramas o ventanas de tiempo.
# 3.- Extracción de características: En esta etapa, se extraen características acústicas relevantes de la señal de audio preprocesada. 
#     Estas características pueden incluir la energía de la señal, la frecuencia fundamental (tono), las frecuencias de los formantes, 
#     la duración de los segmentos de habla, entre otras.
# 4.- Modelado acústico: Con las características de la señal de audio extraídas, se utilizan modelos estadísticos o de aprendizaje automático 
#     para representar los patrones de habla. Esto puede implicar el uso de modelos ocultos de Markov (HMM), redes neuronales convolucionales (CNN),
#     redes neuronales recurrentes (RNN) u otros modelos.
# 5.- Decodificación y reconocimiento: En esta etapa, el algoritmo de reconocimiento del habla utiliza los modelos acústicos para decodificar la 
#     secuencia de características y determinar la transcripción de habla más probable. Esto implica encontrar la secuencia de palabras o fonemas
#     que mejor se ajusta a las características de la señal de audio.
# 6.- Postprocesamiento: Una vez que se ha realizado el reconocimiento del habla, a menudo se realiza un postprocesamiento para mejorar la precisión
#     de la transcripción. Esto puede incluir la corrección de errores gramaticales o de pronunciación, la contextualización del texto reconocido y 
#     la eliminación de palabras irrelevantes o ambiguas.
#--------------- PROGRAMA --------------------------------------
import speech_recognition as sr

# Función para reconocer el habla desde un archivo de audio
def reconocer_habla(archivo_audio):
    # Crear un reconocedor de voz
    reconocedor = sr.Recognizer()
    
    # Inicializar el texto reconocido como una cadena vacía
    texto_reconocido = ""
    
    try:
        # Abrir el archivo de audio
        with sr.AudioFile(archivo_audio) as audio:
            # Leer el contenido del archivo de audio
            audio_data = reconocedor.record(audio)
            
            # Utilizar el reconocedor de voz de Google para transcribir el audio
            texto_reconocido = reconocedor.recognize_google(audio_data, language="es-ES")
            print("Texto reconocido:", texto_reconocido)
    except sr.UnknownValueError:
        print("No se pudo entender el habla")
    except sr.RequestError as e:
        print("Error al recuperar los resultados del servicio de reconocimiento de voz; {0}".format(e))
    
    # Devolver el texto reconocido
    return texto_reconocido

# Archivo de audio de entrada
archivo_audio = "audio.wav"

# Llamar a la función para reconocer el habla desde el archivo de audio
texto_reconocido = reconocer_habla(archivo_audio)
 
 #--------------------------------------------------------------------------
# 1.- import speech_recognition as sr: Importa la biblioteca SpeechRecognition y la renombra como sr para facilitar su uso.
# 2.- def reconocer_habla(archivo_audio):: Define una función llamada reconocer_habla que toma como argumento el nombre del archivo de audio.
# 3.- reconocedor = sr.Recognizer(): Crea un objeto Recognizer que se utilizará para reconocer el habla.
# 4.- texto_reconocido = "": Inicializa una cadena vacía para almacenar el texto reconocido.
# 5.- with sr.AudioFile(archivo_audio) as audio:: Abre el archivo de audio especificado y lo almacena en el objeto audio.
# 6.- audio_data = reconocedor.record(audio): Lee el contenido del archivo de audio y lo guarda en audio_data.
# 7.- texto_reconocido = reconocedor.recognize_google(audio_data, language="es-ES"): Utiliza el reconocedor de voz de Google para transcribir el audio y guarda el texto reconocido en texto_reconocido.
# 8.- except sr.UnknownValueError:: Captura el error UnknownValueError que ocurre cuando el motor de reconocimiento de voz no puede entender lo que se dijo.
# 9.- except sr.RequestError as e:: Captura el error RequestError que ocurre cuando hay un problema al conectarse al servicio de reconocimiento de voz.
# 10.- return texto_reconocido: Devuelve el texto reconocido.
# 11.- archivo_audio = "audio.wav": Especifica el nombre del archivo de audio de entrada.
# 12.- texto_reconocido = reconocer_habla(archivo_audio): Llama a la función reconocer_habla con el archivo de audio de entrada y guarda el texto reconocido en texto_reconocido.