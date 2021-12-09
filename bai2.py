# Requirement:
# - Read frames from your webcam
# - Show the frames in a window
# - Press 'q' to exit
# - Press 'a' to rotate 90 clockwise
# - Press 'd' to rotate 90 counter-clockwise
#

import cv2 as cv

# read video
cap = cv.VideoCapture(0)

state = 2
while True:
    ret, frame = cap.read()

    if (state == 0):
        frame = cv.rotate(frame, cv.ROTATE_90_CLOCKWISE)
    elif (state == 1):
        frame = cv.rotate(frame, cv.ROTATE_90_COUNTERCLOCKWISE)

    key = cv.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('a'):
        state = 0
    elif key == ord('d'):
        state = 1
    elif key == ord('f'):
        state = 2
    elif key == ord('s'):
        cv.imwrite('./assets/frame.jpg', frame)

    cv.imshow('frame', frame)

cap.release()
cv.destroyAllWindows()
