# Con las imágenes de tipo vectorial aplique sklearn y detecte algún patrón.
#en este caso aplicare PCA y KMeans para encontrar patrones/clusters

pca = PCA(n_components=2)
imagenes_pca = pca.fit_transform(imagenes_array)

kmeans = KMeans(n_clusters=5)
clusters = kmeans.fit_predict(imagenes_pca)
silhouette_avg = silhouette_score(imagenes_pca, clusters)
print(f"Puntaje de silueta: {silhouette_avg}")

