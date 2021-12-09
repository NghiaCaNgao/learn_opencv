# Blend two images
import cv2 as cv

src1 = cv.imread("./assets/anh2.jpg")
src2 = cv.imread("./assets/faces.jpg")

alpha = 0.1
beta = 1.0 - alpha
dst = cv.addWeighted(src1, alpha, src2, beta, 0)
dst = cv.resize(dst, (0, 0), fx=0.1, fy=0.1)

cv.imshow("dst", dst)
cv.waitKey(0)