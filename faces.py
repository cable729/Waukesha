#For interacting with opencv functions
import cv2 as cv

HAAR_CASCADE_PATH = "C:\\opencv\\data\\haarcascades\\haarcascade_frontalface_default.xml"


def DetectFacesInImage(image):
    faces = []
    detected = cv.cv.HaarDetectObjects(cv.cv.LoadImage(image), cv.cv.Load(HAAR_CASCADE_PATH), cv.cv.CreateMemStorage(), 1.2, 2, cv.cv.CV_HAAR_DO_CANNY_PRUNING, (100,100))
    if detected:
        for (x, y, w, h), n in detected:
            faces.append((x, y, w, h))
    return faces
