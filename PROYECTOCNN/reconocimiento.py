import face_recognition
import cv2
import numpy as np


# Obtén una referencia a la cámara web #0 (la predeterminada)
video_capture = cv2.VideoCapture(0)

# Carga una imagen de muestra y aprende a reconocerla.
montserrat_image = face_recognition.load_image_file("MontserratMiranda/MontserratMiranda.jpg")
montserrat_face_encoding = face_recognition.face_encodings(montserrat_image)[0]

# Carga una segunda imagen de muestra y aprende a reconocerla.
harry_image = face_recognition.load_image_file("HarryStyles/HarryStyles.jpg")
harry_face_encoding = face_recognition.face_encodings(harry_image)[0]

# Crea arrays de codificaciones de caras conocidas y sus nombres
known_face_encodings = [
    montserrat_face_encoding,
    harry_face_encoding
]
known_face_names = [
    "Montserrat Miranda",
    "Harry Styles"
]

# Inicializa algunas variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # Captura un solo cuadro de vídeo
    ret, frame = video_capture.read()

    # Solo procesa cada segundo cuadro de vídeo para ahorrar tiempo
    if process_this_frame:
        # Redimensiona el cuadro de vídeo a 1/4 de tamaño para un procesamiento más rápido del reconocimiento facial
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convierte la imagen de color BGR (que usa OpenCV) a RGB (que usa face_recognition)
        rgb_small_frame = small_frame[:, :, ::-1]
        
        # Encuentra todas las caras y codificaciones faciales en el cuadro actual de vídeo
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # Verifica si la cara coincide con alguna de las caras conocidas
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Desconocido"

            # En lugar de eso, usa la cara conocida con la menor distancia a la nueva cara
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame

    # Muestra los resultados
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Escala de nuevo las ubicaciones de las caras ya que el cuadro detectado estaba escalado a 1/4 de tamaño
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Dibuja un cuadro alrededor de la cara
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Dibuja una etiqueta con un nombre debajo de la cara
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Muestra la imagen resultante
    cv2.imshow('Video', frame)

    # Pulsa 'q' en el teclado para salir!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera el control de la cámara web
video_capture.release()
cv2.destroyAllWindows()
