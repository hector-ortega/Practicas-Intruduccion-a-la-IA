#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# El encadenamiento hacia adelante, también conocido como forward chaining, comienza con los hechos iniciales disponibles 
# y aplica iterativamente las reglas de la base de conocimiento para deducir nuevas conclusiones. Se sigue avanzando hasta 
# que se alcance una conclusión deseada o hasta que ya no se puedan deducir más hechos. Este enfoque es útil cuando se 
# tienen muchos hechos iniciales y se busca derivar nuevas conclusiones.

# El proceso de encadenamiento hacia adelante generalmente sigue estos pasos:

# 1.- Inicialización: Se comienza con los hechos iniciales conocidos.
# 2.- Aplicación de reglas: Se aplican las reglas de la base de conocimiento para deducir nuevas conclusiones.
# 3.- Verificación: Se verifica si las nuevas conclusiones pueden llevar a la meta deseada. Si no, se continúa aplicando
#     las reglas hasta que se alcance la meta o hasta que ya no se puedan deducir más hechos.
# 4.- Finalización: El proceso se detiene cuando se alcanza la meta deseada o cuando ya no se pueden deducir más hechos.

# Encadenamiento hacia atrás:

# El encadenamiento hacia atrás, también conocido como backward chaining, comienza con el objetivo o conclusión deseada y
# busca hacia atrás las reglas que podrían conducir a esa conclusión. Se continúa retrocediendo hasta llegar a los hechos 
# disponibles o hasta que se agoten las posibles ramificaciones. Este enfoque es útil cuando se conoce el objetivo deseado 
# y se busca determinar qué hechos son necesarios para alcanzar esa meta.

# El proceso de encadenamiento hacia atrás generalmente sigue estos pasos:

# 1.- Inicialización: Se comienza con el objetivo deseado.
# 2.- Búsqueda de reglas: Se buscan las reglas en la base de conocimiento que puedan conducir al objetivo deseado.
# 3.- Aplicación de reglas: Se aplican las reglas encontradas para deducir nuevos hechos que puedan llevar al objetivo deseado.
# 4.- Recursión: Se repite el proceso recursivamente para cada nuevo hecho deducido hasta que se alcance un punto donde todos
#     los hechos necesarios para alcanzar el objetivo estén presentes.
# 5.- Finalización: El proceso se detiene cuando se alcanzan todos los hechos necesarios para alcanzar el objetivo o cuando 
#     ya no se pueden deducir más hechos.
#--------------- PROGRAMA ------------------------------------
class SistemaExperto:
    def __init__(self, base_conocimiento):
        self.base_conocimiento = base_conocimiento

    def encadenamiento_hacia_adelante(self, hechos_iniciales):
        """Realiza encadenamiento hacia adelante."""
        hechos = hechos_iniciales.copy()  # Copia de los hechos iniciales
        while True:
            nuevos_hechos = set()  # Almacena nuevos hechos deducidos en esta iteración
            for regla, conclusion in self.base_conocimiento.items():
                if all(hecho in hechos for hecho in regla):  # Verifica si se cumplen todas las condiciones de la regla
                    if conclusion not in hechos:  # Verifica si la conclusión no ha sido deducida previamente
                        nuevos_hechos.add(conclusion)  # Agrega la conclusión a los nuevos hechos deducidos
            if not nuevos_hechos:  # Si no se encontraron nuevos hechos, se detiene el proceso
                break
            hechos.update(nuevos_hechos)  # Actualiza los hechos con los nuevos hechos deducidos
        return hechos

    def encadenamiento_hacia_atras(self, objetivo):
        """Realiza encadenamiento hacia atrás."""
        hechos = set()  # Almacena los hechos necesarios para llegar al objetivo
        return self.buscar_reglas(objetivo, hechos)

    def buscar_reglas(self, objetivo, hechos):
        """Busca las reglas que puedan conducir al objetivo."""
        reglas_aplicables = []
        for regla, conclusion in self.base_conocimiento.items():
            if conclusion == objetivo:
                if all(hecho in hechos for hecho in regla):
                    return True
                else:
                    for hecho in regla:
                        if hecho not in hechos:
                            if self.buscar_reglas(hecho, hechos):
                                reglas_aplicables.append(regla)
                                hechos.add(objetivo)
                                return reglas_aplicables
        return False

# Crear una instancia del sistema experto
base_conocimiento = {
    ("p", "q"): "r",
    ("s", "r"): "t",
    ("u", "v"): "s",
    ("a", "t"): "u",
    ("a", "b"): "v",
    ("c", "d"): "v"
}
sistema = SistemaExperto(base_conocimiento)

# Ejemplo de encadenamiento hacia adelante
hechos_iniciales = {"p", "q", "s"}
print("Encadenamiento hacia adelante:")
print(sistema.encadenamiento_hacia_adelante(hechos_iniciales))

# Ejemplo de encadenamiento hacia atrás
objetivo = "v"
print("\nEncadenamiento hacia atrás:")
print(sistema.encadenamiento_hacia_atras(objetivo))

#--------------------------------------------------------------

# 1.- Definimos la clase SistemaExperto, que contendrá los métodos para realizar el encadenamiento hacia adelante y hacia atrás.
# 2.- El método encadenamiento_hacia_adelante implementa el encadenamiento hacia adelante. Itera sobre las reglas en la base de 
#     conocimiento y verifica si se cumplen todas las condiciones de una regla para deducir una nueva conclusión.
# 3.- El método encadenamiento_hacia_atras implementa el encadenamiento hacia atrás. Utiliza la recursión para buscar hacia atrás 
#     las reglas que puedan conducir al objetivo deseado.
# 4.- El método buscar_reglas es un auxiliar del encadenamiento hacia atrás. Recorre las reglas de la base de conocimiento para 
#     encontrar las que puedan conducir al objetivo.
# 5.- Creamos una instancia de la clase SistemaExperto con una base de conocimiento dada.
# 6.- Probamos los métodos de la clase con ejemplos de encadenamiento hacia adelante y hacia atrás y mostramos los resultados.