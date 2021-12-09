import cv2 as cv
import imutils as im

# load webcam
cap = cv.VideoCapture(0)
print(cap.isOpened())
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv.imshow("Webcam", frame)
    out.write(frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv.destroyAllWindows()
