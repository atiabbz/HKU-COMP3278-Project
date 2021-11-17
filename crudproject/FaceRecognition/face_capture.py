import cv2
import os
import shutil


def main():

    cascade_path = os.path.abspath(
        "./FaceRecognition/haarcascade/haarcascade_frontalface_default.xml"
    )
    faceCascade = cv2.CascadeClassifier(cascade_path)

    video_capture = cv2.VideoCapture(0)

    # Specify the `user_name` and `NUM_IMGS` here.
    user_name = "Jack"
    NUM_IMGS = 400

    dataPath = os.path.abspath("./FaceRecognition/data")
    shutil.rmtree(dataPath)
    dataPath = os.path.abspath(f"./FaceRecognition/data/{user_name}")
    os.makedirs(dataPath)

    # if not os.path.exists("data/{}".format(user_name)):
    #     os.mkdir("data/{}".format(user_name))

    cnt = 1
    font = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (80, 50)
    fontScale = 1
    fontColor = (102, 102, 225)
    lineType = 2

    # Open camera
    while cnt <= NUM_IMGS:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        """
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE,
        )

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        msg = "Saving {}'s Face Data [{}/{}]".format(user_name, cnt, NUM_IMGS)
        cv2.putText(frame, msg,
                    bottomLeftCornerOfText,
                    font,
                    fontScale,
                    fontColor,
                    lineType)
        """

        # Display the resulting frame
        cv2.imshow("Video", frame)
        # Store the captured images in `data/Jack`
        imagePath = os.path.abspath(
            "./FaceRecognition/data/{}/{}{:03d}.jpg".format(user_name, user_name, cnt)
        )
        # cv2.imwrite("data/{}/{}{:03d}.jpg".format(user_name, user_name, cnt), frame)
        cv2.imwrite(imagePath, frame)
        cnt += 1

        key = cv2.waitKey(100)

    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()
