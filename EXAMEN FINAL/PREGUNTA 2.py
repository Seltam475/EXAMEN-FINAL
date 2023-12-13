# Seleccione un dataset gráfico (mínimo 100 imágenes). Realice morfología de imágenes, estandarice tamaños y colores. 
#Manejelo como matriz y vector.

import cv2
import numpy as np
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

import os
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

#seleccione un dataset gráfico
directorio_imagenes = 'ruta/a/tu/directorio'  # Ruta al directorio que contiene las imágenes
lista_archivos = os.listdir(directorio_imagenes)

#Realizar la morfología de imágenes, estandarice tamaños y colores.

imagenes = []
for nombre_archivo in lista_archivos:
    ruta_imagen = os.path.join(directorio_imagenes, nombre_archivo)
    imagen = cv2.imread(ruta_imagen)
    if imagen is not None:
        # Aplicar morfología, redimensionar, cambiar color, etc.
        # ...

        # Convertir la imagen a matriz y vector
        
	matriz_imagen = np.array(imagen)
        vector_imagen = matriz_imagen.flatten()
        imagenes.append(vector_imagen)

# Convertir la lista de vectores de imágenes a una matriz NumPy
imagenes_array = np.array(imagenes)