# Genere un agente que detecte diferencias de cadenas de palabras. 
# Ej. "Mabru se fue a la guerra", que tan diferente es de "Manbru se fue a la guerra"

pip install editdistance

import editdistance

def calcular_diferencia(cadena1, cadena2):
    distancia = editdistance.eval(cadena1, cadena2)
    return distancia

cadena1 = "Mabru se fue a la guerra"
cadena2 = "Manbru se fue a la guerra"

diferencia = calcular_diferencia(cadena1, cadena2)
print(f"La diferencia entre las cadenas es: {diferencia}")
