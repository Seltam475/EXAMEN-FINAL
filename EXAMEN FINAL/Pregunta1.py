from sklearn.datasets import fetch_california_housing
housing = fetch_california_housing()
data = housing.data


# Calcular la media
def cal_media(columna):
    suma = sum(columna)
    total = len(columna)
    media = suma / total
    return media


# Calcular la moda
def cal_moda(columna):
    cont = {}
    for valor in columna:
        cont[valor] = cont.get(valor, 0) + 1
    moda = [key for key, value in cont.items() if value == max(cont.values())]
    return moda


# Calcular cuartiles
def cal_cuartiles(columna):
    col_ordenada = sorted(columna)
    n = len(col_ordenada)
    q1 = col_ordenada[n // 4]
    q2 = col_ordenada[n // 2]
    q3 = col_ordenada[3 * n // 4]
    return q1, q2, q3

#1. Seleccione un dataset de su interés (de cualquier repositorio, que contenga 
#datos tabulares mínimo de 1500 filas y al menos 10 columnas). Realice el cálculo 
#de la media, moda, cuartiles de datos y de percentiles por columna; explique qué 
#significa en cada caso graficando los resultados (sin numpy y pandas).



# Calcular percentiles
def cal_percentiles(columna, percentil):
    col_ordenada = sorted(columna)
    n = len(col_ordenada)
    indice = int((percentil / 100) * (n - 1))
    return col_ordenada[indice]


# Calcular estadísticas para cada columna
num_columnas = data.shape[1]
for i in range(num_columnas):
    col_actual = data[:, i]
    media = cal_media(col_actual)
    moda = cal_moda(col_actual)
    q1, q2, q3 = cal_cuartiles(col_actual)
    p25 = cal_percentiles(col_actual, 25)
    p50 = cal_percentiles(col_actual, 50)
    p75 = cal_percentiles(col_actual, 75)
    
    print(f"Columna {i + 1}:")
    print(f"Media: {media}")
    print(f"Moda: {moda}")
    print(f"Cuartiles: Q1 = {q1}, Q2 = {q2}, Q3 = {q3}")
    print(f"Percentiles: P25 = {p25}, P50 = {p50}, P75 = {p75}")
    print("---------------------------")