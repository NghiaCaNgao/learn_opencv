# Requirement:
# - Count the number of shapes in the image

import cv2 as cv
import imutils as im

# Load image
image = cv.imread("./assets/shape2.jpg")
image = cv.resize(image, (0, 0), fx=0.5, fy=0.5)
gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
blurred = cv.GaussianBlur(gray_image, (5, 5), 0)
ret, threshold_image = cv.threshold(blurred, 220, 255, cv.THRESH_BINARY)

cv.imshow("Threshold", threshold_image)
# threshold_image = cv.adaptiveThreshold(gray_image, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 15, 2)

contours = cv.findContours(threshold_image, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
contours = im.grab_contours(contours)

# Sort contours by area
contours = sorted(contours, key=cv.contourArea, reverse=True)

number_of_bubbles = 0

for c in contours:
    (x, y, w, h) = cv.boundingRect(c)
    if (20<w) and(20<h):
        number_of_bubbles += 1
        cv.drawContours(image, [c], -1, (0, 255, 0), 2)
        cv.putText(image, "Shape {}".format(number_of_bubbles), (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 1)

print("Number of bubbles: {}".format(number_of_bubbles))
cv.imshow("Image", image)
cv.waitKey(0)
cv.destroyAllWindows()
