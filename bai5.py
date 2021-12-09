import cv2 as cv
import imutils as im

# Load image
image = cv.imread("./assets/sample1.png")
blur = cv.blur(image, (5, 5))
gray_image = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)

# threshold = cv.adaptiveThreshold(
#     gray_image, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

ret, threshold = cv.threshold(gray_image, 127, 255, cv.THRESH_BINARY)
cv.imshow("Threshold", threshold)

contours = cv.findContours(threshold, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
contours = im.grab_contours(contours)
contours = sorted(contours, key=cv.contourArea, reverse=False)

num = 0
for c in contours:
    (x, y, w, h) = cv.boundingRect(c)

    if (40 < w < 90) and (100 < h < 180) and (h/w > 1.5):
        num += 1
        print(num, x, y, w, h)
        cv.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv.imshow("Image", image)
cv.waitKey(0)
cv.destroyAllWindows()
