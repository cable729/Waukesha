#For interacting with opencv functions
import cv2.cv as cv

HAAR_CASCADE_PATH = "C:\\opencv\\data\\haarcascades\\haarcascade_frontalface_default.xml"


def DetectFacesInImage(image):
    faces = []
    detected = cv.HaarDetectObjects(cv.LoadImage(image), cv.Load(HAAR_CASCADE_PATH), cv.CreateMemStorage(), 1.2, 2, cv.CV_HAAR_DO_CANNY_PRUNING, (100,100))
    if detected:
        for (x, y, w, h), n in detected:
            faces.append((x, y, w, h))
    return faces
