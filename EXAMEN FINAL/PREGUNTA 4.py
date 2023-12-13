# 4. Con las imágenes de tipo matriz aplique tensorflow y detecte algún patrón.
# ya que se tiene las matrices de imágenes y etiquetas
# se deifinirá y entrenará una red neuronal convolucional (CNN)

model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(100, 100, 3)))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))