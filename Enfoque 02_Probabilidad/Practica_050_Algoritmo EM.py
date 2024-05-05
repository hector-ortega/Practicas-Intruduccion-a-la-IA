#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.
#-----------------TEORIA----------------------------------------
# El algoritmo de Expectation-Maximization (EM) es un método iterativo utilizado para estimar los parámetros de modelos estadísticos incompletos o
# con datos faltantes. Fue propuesto por Arthur Dempster, Nan Laird y Donald Rubin en 1977. Este algoritmo se utiliza en una variedad de aplicaciones 
# en el campo del aprendizaje automático y la inteligencia artificial, incluyendo clustering, clasificación y modelado de datos con distribuciones probabilísticas.

# Funcionamiento del algoritmo EM:
# El algoritmo EM consta de dos pasos iterativos que se repiten hasta converger a una solución:

# 1.- Paso de Expectativa (E-step): En este paso, se calculan las probabilidades (o responsabilidades) de pertenencia de cada punto de datos a cada componente 
#     del modelo. Estas probabilidades se utilizan para estimar los valores de los datos no observados o faltantes.
# 2.- Paso de Maximización (M-step): En este paso, se utilizan las probabilidades calculadas en el paso de expectativa para actualizar los parámetros 
#     del modelo. Se buscan los parámetros que maximizan la verosimilitud de los datos observados, teniendo en cuenta las probabilidades calculadas en el paso anterior.
#--------------- PROGRAMA --------------------------------------
import numpy as np
from scipy.stats import multivariate_normal

def expectation_maximization(X, K, max_iters=100, tol=1e-4):
    # X: Datos de entrada
    # K: Número de componentes en el modelo de mezcla gaussiana
    # max_iters: Número máximo de iteraciones
    # tol: Tolerancia para la convergencia del algoritmo

    # Inicializar parámetros aleatorios
    N, D = X.shape
    mu = X[np.random.choice(N, K, replace=False)]  # Inicializar medias aleatorias
    sigma = np.tile(np.eye(D), (K, 1, 1))           # Inicializar matrices de covarianza como matrices identidad
    pi = np.ones(K) / K                            # Inicializar pesos de mezcla uniformemente

    # Algoritmo EM
    for iter in range(max_iters):
        # Paso de expectativa (E-step)
        gamma = np.zeros((N, K))  # Inicializar las responsabilidades
        for k in range(K):
            gamma[:, k] = pi[k] * multivariate_normal.pdf(X, mu[k], sigma[k])

        gamma /= np.sum(gamma, axis=1, keepdims=True)  # Normalizar las responsabilidades

        # Paso de maximización (M-step)
        Nk = np.sum(gamma, axis=0)  # Número de puntos asignados a cada componente
        mu_new = np.dot(gamma.T, X) / Nk.reshape(-1, 1)  # Nuevas medias
        sigma_new = np.zeros_like(sigma)  # Nuevas matrices de covarianza
        for k in range(K):
            diff = X - mu_new[k]
            sigma_new[k] = np.dot(gamma[:, k] * diff.T, diff) / Nk[k]  # Covarianza ponderada

        pi_new = Nk / N  # Nuevos pesos de mezcla

        # Calcular la log-verosimilitud para verificar la convergencia
        log_likelihood = np.sum(np.log(np.sum(pi[k] * multivariate_normal.pdf(X, mu[k], sigma[k]), axis=1)))

        # Verificar convergencia
        if iter > 0 and np.abs(log_likelihood - prev_log_likelihood) < tol:
            break

        # Actualizar parámetros
        mu, sigma, pi = mu_new, sigma_new, pi_new
        prev_log_likelihood = log_likelihood

    return mu, sigma, pi

# Ejemplo de uso
# Generar datos de ejemplo
np.random.seed(0)
N = 1000
X = np.vstack([
    np.random.multivariate_normal([0, 0], [[1, 0.5], [0.5, 1]], int(0.1 * N)),
    np.random.multivariate_normal([3, 3], [[1, -0.5], [-0.5, 1]], int(0.4 * N)),
    np.random.multivariate_normal([-3, 3], [[1, 0], [0, 1]], int(0.3 * N)),
    np.random.multivariate_normal([0, -2], [[1, 0], [0, 1]], int(0.2 * N))
])
np.random.shuffle(X)

# Aplicar el algoritmo EM
K = 4  # Número de componentes en el modelo de mezcla gaussiana
mu, sigma, pi = expectation_maximization(X, K)

# Imprimir los parámetros aprendidos
print("Medias:")
print(mu)
print("\nMatrices de covarianza:")
print(sigma)
print("\nPesos de mezcla:")
print(pi)

#-------------------------------------------------------------------------------

# 1.- Importamos las bibliotecas necesarias: numpy para cálculos numéricos y multivariate_normal de scipy.stats para trabajar con distribuciones normales multivariadas.
# 2.- Definimos una función llamada expectation_maximization que toma los datos de entrada X, el número de componentes K, y los parámetros opcionales max_iters
#     y tol que controlan el número máximo de iteraciones y la tolerancia para la convergencia del algoritmo, respectivamente.
# 3.- Inicializamos los parámetros del modelo (medias, matrices de covarianza y pesos de mezcla) de manera aleatoria.
# 4.- Implementamos el bucle principal del algoritmo EM, que consiste en el paso de expectativa (E-step) y el paso de maximización (M-step), alternativamente,
#     hasta que se cumple un criterio de convergencia (en este caso, la convergencia de la log-verosimilitud).
# 5.- En el paso de expectativa, calculamos las responsabilidades de cada punto respecto a cada componente de la mezcla.
# 6.- En el paso de maximización, actualizamos los parámetros del modelo (medias, matrices de covarianza y pesos de mezcla) utilizando las 
#     responsabilidades calculadas en el paso anterior.
# 7.- Verificamos la convergencia del algoritmo comparando la log-verosimilitud actual con la log-verosimilitud anterior.
# 8.- Finalmente, devolvemos los parámetros aprendidos del modelo: las medias, las matrices de covarianza y los pesos de mezcla.