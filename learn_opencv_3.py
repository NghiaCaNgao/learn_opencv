import numpy as np
import cv2 as cv

image = np.zeros((512, 512, 3), np.uint8)

# Draw a line
cv.line(image, (0, 0), (511, 511), (255, 0, 0), 5)

# Draw a rectangle
cv.rectangle(image, (20, 20), (100, 100), (255, 255, 0), 3)

# Draw a circle and fill red color
cv.circle(image, (200, 200), 50, (0, 255, 255), -1)

# Draw polygon
cv.polylines(image, [np.array([[100, 100], [200, 300], [300, 200]])], True, (255, 0, 255), 3)

# Put a text
cv.putText(image,"Hello",(150,150),cv.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)

cv.imshow("Image", image)

cv.waitKey(0)
cv.destroyAllWindows()
