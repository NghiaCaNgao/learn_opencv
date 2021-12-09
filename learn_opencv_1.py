import cv2 as cv
print(cv.__version__)


def thresholdImage(image):
    # Convert to gray before processing
    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    # Apply threshold
    ret, image = cv.threshold(image, 210, 255, cv.THRESH_BINARY)

    # Apply adaptive threshold
    imageThreshold = cv.adaptiveThreshold(
        image, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 5, 2)
    return imageThreshold


def cannyImage(image):
    # Convert to gray before processing
    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(image, 100, 200)
    return edges


def blurImage(image):
    # blur = cv.blur(image, (5, 5))
    blur = cv.GaussianBlur(image, (5, 5), 0)
    return blur

def contourImage(image):
    processedImage = thresholdImage(image)
    contours, hierarchy = cv.findContours(processedImage, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(processedImage, contours, -1, (0, 255, 0), 1)
    cv.imshow("Contours", processedImage)





def readImage(imageDir="./assets/sample.png"):
    try:
        # read an image
        image = cv.imread(imageDir, cv.IMREAD_COLOR)
        if image is None:
            raise Exception("Invalid image path")

        # read the dimension of the image
        (height, width) = image.shape[:2]
        print("The dimension of the image is: ", height, width)

        # display the original image
        cv.imshow("The original image", image)

        threshold_Image = thresholdImage(image)
        cv.imshow("The image after thresholding", threshold_Image)

        # canny_Image = cannyImage(image)
        # cv.imshow("The image after canny", canny_Image)

        # blur_Image = blurImage(image)
        # cv.imshow("The image after blur", blur_Image)

        contourImage(image)

    except Exception as e:
        print(e)
        exit(1)

    cv.waitKey(0)
    cv.destroyAllWindows()


def videoCapture(videoDir=0):
    try:
        cap = cv.VideoCapture(videoDir)
        if not cap.isOpened():
            raise Exception("Invalid video path")

        while(True):
            # Capture frame-by-frame
            ret, frame = cap.read()
            # frame = cv.rotate(frame, cv.ROTATE_180)
            frame = cv.flip(frame, 1)

            # read the dimension of the frame
            # (height, width) = frame.shape[:2]
            # print("The dimension of the frame is: ", height, width)

            # Convert BGR to GRAY
            # frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

            # Resize the image
            # frame = cv.resize(frame, dsize=None, fx=0.5, fy=0.5)

            # Display the resulting frame
            contourImage(frame)
            # cv.imshow('frame', frame)
            if (cv.waitKey(1) & 0xFF == ord('q')) or not ret:
                break

        # Release the capture
        cap.release()
        cv.destroyAllWindows()

    except Exception as e:
        print(e)
        exit(1)


# readImage("./assets/test.jpg")
# videoCapture("./assets/sample.avi")
videoCapture(0)
# readImage()
