# Cargar el modelo guardado
from keras.models import modelo
classifier = modelo('face_recognition_model.h5')

# Predecir una nueva imagen
def predict_image(image_path):
    test_image = image.load_img(image_path, target_size=(64, 64))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    result = classifier.predict(test_image)
    return result

# Ruta de la imagen que deseas predecir
image_path = r"C:/Users/monts/Desktop/IA/CNN/dataset/test_set/propios/propio_test1.jpg" # Usa una cadena en bruto
# o
# image_path = "C:/Users/monts/Desktop/IA/CNN/dataset/test_set/propios/propio_test1.jpg" # Usa barras inclinadas hacia adelante

prediction = predict_image(image_path)

# Decodificar la predicción
if prediction[0][0] == 1:
    print('Predicción: Famoso')
else:
    print('Predicción: Propio')