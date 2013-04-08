import faces
import os

imageDirectory = "Images\\"

for f in os.listdir(imageDirectory):
    for face in faces.DetectFacesInImage(imageDirectory + str(f)):
        print face
