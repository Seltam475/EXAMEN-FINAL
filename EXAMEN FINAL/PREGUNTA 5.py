# Realice sin librerías el algoritmo genético de las n-reinas.



import random

# Función para inicializar una población aleatoria de N reinas
def inicializar_poblacion(size, n):
    poblacion = []
    for i in range(size):
        individuo = [random.randint(1, n) for _ in range(n)]
        poblacion.append(individuo)
    return poblacion

# Función para evaluar la aptitud de cada individuo de la población
def evaluar_aptitud(individuo):
    ataques = 0
    n = len(individuo)
    for i in range(n):
        for j in range(i+1, n):
            if individuo[i] == individuo[j] or abs(individuo[i] - individuo[j]) == abs(i - j):
                ataques += 1
    return ataques

# Función para seleccionar los padres (torneo)
def seleccionar_padres(poblacion, n_padres):
    padres = []
    for _ in range(n_padres):
        muestra = random.sample(poblacion, 3)
        mejor_individuo = min(muestra, key=lambda x: evaluar_aptitud(x))
        padres.append(mejor_individuo)
    return padres

# Función para realizar el cruce de dos padres (reinas)
def cruzar_padres(padre1, padre2):
    punto_cruce = random.randint(1, len(padre1) - 1)
    hijo = padre1[:punto_cruce] + padre2[punto_cruce:]
    return hijo

# Función para aplicar una mutación en un individuo
def mutar(individuo, prob_mutacion):
    if random.uniform(0, 1) < prob_mutacion:
        idx = random.randint(0, len(individuo) - 1)
        individuo[idx] = random.randint(1, len(individuo))
    return individuo

# Función principal para resolver el problema de las N reinas con algoritmos genéticos
def resolver_n_reinas(n, size_poblacion, n_generaciones, prob_mutacion):
    poblacion = inicializar_poblacion(size_poblacion, n)
    for _ in range(n_generaciones):
        poblacion = sorted(poblacion, key=lambda x: evaluar_aptitud(x))
        if evaluar_aptitud(poblacion[0]) == 0:
            return poblacion[0]
        padres = seleccionar_padres(poblacion, 2)
        hijos = [cruzar_padres(padres[0], padres[1]) for _ in range(size_poblacion - 2)]
        poblacion = padres + hijos
        poblacion = [mutar(individuo, prob_mutacion) for individuo in poblacion]
    return None

# Resolver el problema de las 8 reinas (tamaño del tablero)
n = 8
size_poblacion = 100
n_generaciones = 1000
prob_mutacion = 0.1

solucion = resolver_n_reinas(n, size_poblacion, n_generaciones, prob_mutacion)
if solucion:
    print("Solución encontrada:")
    print(solucion)
else:
    print("No se encontró solución en las generaciones dadas.")