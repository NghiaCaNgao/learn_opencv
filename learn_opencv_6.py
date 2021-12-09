# adjust contrast and brightness of an image

import cv2 as cv
import numpy as np

# read an image
img = cv.imread('./assets/shape.jpg')

if img is None:
    print('Failed to read image')
    exit(0)

# This is contrast. Value can be float type with value [0,3]
alpha = 1.3
# this is brightness. Value can be int type with value [0,100]
beta = 40

# Method 1:
# Fill a matrix image with zero values
# newImg = np.zeros(img.shape, img.dtype)

# Method 2:
newImg = cv.convertScaleAbs(img, alpha=alpha, beta=beta)
cv.imshow('Original Image', img)
cv.imshow('New Image by alpha anh beta', newImg)

# Gamma method
# Create lookup table or colormap
gamma = 2
lookupTable = np.empty((1, 256), np.uint8)
for i in range(256):
    lookupTable[0, i] = np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255)
res = cv.LUT(img, lookupTable)
cv.imshow('New Image by gamma', res)
cv.waitKey(0)
cv.destroyAllWindows()
