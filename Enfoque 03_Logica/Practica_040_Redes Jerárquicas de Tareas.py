#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# Las Redes Jerárquicas de Tareas (HAN, por sus siglas en inglés) son una representación de tareas y sus dependencias en un
# grafo dirigido acíclico (DAG). Estas redes se utilizan en la planificación y gestión de proyectos para modelar la estructura de 
# las tareas y las relaciones de dependencia entre ellas. Cada tarea se representa como un nodo en el grafo, y las dependencias entre
# tareas se representan como arcos dirigidos de un nodo a otro.

# El objetivo principal de las Redes Jerárquicas de Tareas es organizar las tareas de un proyecto en una estructura jerárquica, de modo que 
# las dependencias entre ellas se respeten y se pueda determinar un orden de ejecución adecuado para completar el proyecto de manera eficiente.

# Los algoritmos que operan sobre estas redes suelen realizar operaciones como la determinación del orden topológico de las tareas, la 
# identificación de caminos críticos (rutas de tareas que, si se retrasan, pueden retrasar todo el proyecto), la asignación de recursos, 
# y la planificación de tiempos y costos.
#--------------- PROGRAMA ------------------------------------
class Task:
    def __init__(self, name):
        self.name = name
        self.dependencies = set()  # Conjunto de dependencias

    def add_dependency(self, task):
        self.dependencies.add(task)

    def __repr__(self):
        return self.name

class TaskGraph:
    def __init__(self):
        self.tasks = {}  # Diccionario de tareas

    def add_task(self, name):
        task = Task(name)
        self.tasks[name] = task
        return task

    def add_dependency(self, task_name, dependency_name):
        if task_name not in self.tasks:
            self.add_task(task_name)
        if dependency_name not in self.tasks:
            self.add_task(dependency_name)
        self.tasks[task_name].add_dependency(self.tasks[dependency_name])

    def topological_sort(self):
        order = []  # Orden topológico de las tareas
        visited = set()  # Conjunto de nodos visitados

        def dfs(task):
            if task in visited:
                return
            visited.add(task)
            for dependency in task.dependencies:
                dfs(dependency)
            order.append(task)

        for task in self.tasks.values():
            dfs(task)

        return order[::-1]  # Invertimos el orden para obtener el orden topológico correcto

# Ejemplo de uso
graph = TaskGraph()
graph.add_dependency("Cocinar", "Comprar ingredientes")
graph.add_dependency("Comprar ingredientes", "Ir al supermercado")
graph.add_dependency("Cocinar", "Hacer la lista de recetas")

# Orden topológico de las tareas
order = graph.topological_sort()
print("Orden topológico de las tareas:")
for task in order:
    print(task)

#-----------------------------------------------------------------------------
# 1.- Creamos una clase Task para representar cada tarea. Cada tarea tiene un nombre y un conjunto de dependencias.
# 2.- Creamos una clase TaskGraph para representar el grafo de tareas. Utilizamos un diccionario para almacenar las tareas, donde la clave es 
#     el nombre de la tarea y el valor es el objeto Task correspondiente.
# 3.- La función add_task añade una tarea al grafo.
# 4.- La función add_dependency añade una dependencia entre dos tareas.
# 5.- La función topological_sort realiza un recorrido en profundidad (DFS) sobre el grafo para obtener el orden topológico de las tareas.
# 6.- Finalmente, creamos un objeto TaskGraph, añadimos tareas y dependencias, y obtenemos el orden topológico de las tareas.