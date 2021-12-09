import cv2 as cv
import numpy as np

events = [i for i in dir(cv) if 'EVENT' in i]
print(events)

def drawCircle(event,x,y,flags, param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img,(x,y),100,(255,0,0),-1)

img = np.zeros((1000,1000,3), np.uint8)

cv.namedWindow('Image')
cv.setMouseCallback('Image', drawCircle)

while True:
    cv.imshow('Image', img)
    if cv.waitKey(1)& 0xFF == ord('q'):
        break

cv.destroyAllWindows()