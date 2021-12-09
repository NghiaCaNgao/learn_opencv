#  Requirement:
# - Input an image or video file or webcam
# - Detect face
# - Draw rectangle around face
# - Show the image and save it into your directory if press 's'

import cv2 as cv

def loadModel():
    face_cascade = cv.CascadeClassifier(
        "./models/haarcascade_frontalface_default.xml")
    return face_cascade


def detectFace(frame, face_cascade):
    grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        grayFrame, 1.2, 10, minSize=(100, 100))

    if (faces is not None):
        print("Found {0} faces!".format(len(faces)))

    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 4)

    return frame


def videoMode():
    # Load model
    face_cascade = loadModel()
    # Load for webcam
    cap = cv.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if ret:
            frame = cv.flip(frame, 1)
            frame = cv.resize(frame, dsize=None, fx=2, fy=2)
            frame = detectFace(frame, face_cascade)
            cv.imshow("Face Detection", frame)

            if (cv.waitKey(1) & 0xFF == ord('q')):
                break
    cap.release()
    cv.destroyAllWindows()


def imageMode(path):
    # Load model
    face_cascade = loadModel()
    # Load image
    img = cv.imread(path)
    if (img is None):
        print("Image not found!")
        return

    img = cv.resize(img, dsize=None, fx=2, fy=2)
    img = detectFace(img, face_cascade)
    cv.imwrite("./output/output.jpg", img)
    img = cv.resize(img, dsize=None, fx=0.05, fy=0.05)
    cv.imshow("Face Detection", img)
    cv.waitKey(0)
    cv.destroyAllWindows()


videoMode()
# imageMode("./assets/face.jpg")
# imageMode("./assets/anh3.jpg")
