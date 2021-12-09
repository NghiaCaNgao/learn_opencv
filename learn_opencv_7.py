# Using applyColorMap() to change the color of an image

import cv2 as cv

img_gray = cv.imread('assets/faces.jpg',cv.IMREAD_GRAYSCALE)
img_gray = cv.resize(img_gray, dsize=None, fx=0.1, fy=0.1)
img_color = cv.applyColorMap(img_gray, cv.COLORMAP_JET)

cv.imshow("Original Image", img_gray)
cv.imshow('Color Map', img_color)

cv.waitKey(0)
cv.destroyAllWindows()