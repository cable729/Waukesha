#/usr/bin/env python

import Image
import cv2
import cv2.cv as cv
import sys
import os
import numpy
from scipy.misc import imresize


cascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_alt.xml")

def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30), flags = cv.CV_HAAR_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    return rects


def crop_to_face(img, dim):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    rects = detect(gray, cascade)

    if len(rects) > 0:
        cropped = img[rects[0][1]:rects[0][3], rects[0][0]:rects[0][2]]
        cropped = Image.fromarray(cropped)
        thumb = cropped.resize((dim,dim), Image.BILINEAR)
        return thumb

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "USAGE: python crop_to_face <directory of original images> <directory for new images>"
        sys.exit()

    original_dir = sys.argv[1]
    new_dir = sys.argv[2]

    if not os.path.exists(new_dir):
        os.makedirs(new_dir)

    for f in os.listdir(original_dir):
        old_file = original_dir + "\\" + f
        if os.path.isfile(old_file):
            img = Image.open(old_file)
            numpy_img = numpy.array(img)
            cropped = crop_to_face(numpy_img, 100)
            if not cropped:
                print 'Could not find a face in ' + old_file
            else:
                cropped.save(new_dir + "\\" + f)