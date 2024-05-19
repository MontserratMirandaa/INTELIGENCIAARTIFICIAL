import numpy as np
from keras.preprocessing import image
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

# Inicializar el modelo
classifier = Sequential()

# Paso 1 - Convolución
classifier.add(Conv2D(32, (3, 3), input_shape=(64, 64, 3), activation='relu'))

# Paso 2 - MaxPooling
classifier.add(MaxPooling2D(pool_size=(2, 2)))

# Segunda capa de convolución para mejorar la precisión
classifier.add(Conv2D(64, (3, 3), activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2)))

# Paso 3 - Flattening
classifier.add(Flatten())

# Paso 4 - Full connection
classifier.add(Dense(units=128, activation='relu'))
classifier.add(Dense(units=2, activation='softmax')) # Cambiar a la cantidad de clases que tengas

# Compilar la red neuronal convolucional
classifier.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Preprocesamiento de las imágenes
train_datagen = ImageDataGenerator(rescale=1./255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory('dataset/training_set', target_size=(64, 64), batch_size=32, class_mode='categorical')
test_set = test_datagen.flow_from_directory('dataset/test_set', target_size=(64, 64), batch_size=32, class_mode='categorical')

# Entrenar la red
history = classifier.fit(training_set, steps_per_epoch=8000/32, epochs=25, validation_data=test_set, validation_steps=2000/32)

# Evaluar el modelo
loss, accuracy = classifier.evaluate(test_set)
print(f'Test accuracy: {accuracy}')

# Guardar el modelo entrenado
classifier.save('face_recognition_model.h5')

# Graficar la precisión y la pérdida
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()
