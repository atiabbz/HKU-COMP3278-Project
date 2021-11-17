import os
import shutil
import numpy as np
from PIL import Image
import cv2
import pickle


def main():

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # image_dir = os.path.join(BASE_DIR, "data")
    image_dir = os.path.abspath("./FaceRecognition/data")

    # Load the OpenCV face recognition detector Haar
    cascade_path = os.path.abspath(
        "./FaceRecognition/haarcascade/haarcascade_frontalface_default.xml"
    )
    face_cascade = cv2.CascadeClassifier(cascade_path)
    # Create OpenCV LBPH recognizer for training
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    current_id = 0
    label_ids = {}
    y_label = []
    x_train = []

    # Traverse all face images in `data` folder
    for root, dirs, files in os.walk(image_dir):
        for file in files:
            if file.endswith("png") or file.endswith("jpg"):
                path = os.path.join(root, file)
                label = os.path.basename(root).replace("", "").upper()  # name
                print(label, path)

                if label in label_ids:
                    pass
                else:
                    label_ids[label] = current_id
                    current_id += 1
                id_ = label_ids[label]
                print(label_ids)

                pil_image = Image.open(path).convert("L")
                image_array = np.array(pil_image, "uint8")
                print(image_array)
                # Using multiscle detection
                faces = face_cascade.detectMultiScale(
                    image_array, scaleFactor=1.5, minNeighbors=3
                )

                for (x, y, w, h) in faces:
                    roi = image_array[y : y + h, x : x + w]
                    x_train.append(roi)
                    y_label.append(id_)

    # labels.pickle store the dict of labels.
    # {name: id}
    # id starts from 0
    try:
        os.remove(os.path.join(os.path.abspath("./FaceRecognition"), "labels.pickle"))
    except:
        pass
    pickle_path = os.path.join(os.path.abspath("./FaceRecognition"), "labels.pickle")
    with open(pickle_path, "wb") as f:
        pickle.dump(label_ids, f)

    # Train the recognizer and save the trained model.
    recognizer.train(x_train, np.array(y_label))
    try:
        os.remove((os.path.join(os.path.abspath("./FaceRecognition"), "train.yml")))
    except:
        pass
    train_path = os.path.join(os.path.abspath("./FaceRecognition"), "train.yml")
    recognizer.save(train_path)
