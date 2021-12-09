# Requirement: 
# - Read frame from your camera and display it on screen with gray color

import cv2

# read video from camera
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    # Convert frame to gray and flip it 
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.flip(frame, 1)
    cv2.imshow('Frame', frame)
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break
    
cap.release()
cv2.destroyAllWindows()
