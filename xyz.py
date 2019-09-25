#!/usr/bin/python
# -*- coding: utf-8 -*-
## This program first ensures if the face of a person exists in the given image or not then if it exists, it crops
## the image of the face and saves to the given directory.

## Importing Modules

import cv2
import os

#################################################################################

##Make changes to these lines for getting the desired results.

## DIRECTORY of the images

directory = "E:\\env\\tensorflow-for-poets-2-master\\tf_files\\gestures\\P\\"

## directory where the images to be saved:

f_directory = "E:\\env\\gestures\\P\\"


################################################################################

def facecrop(image):

    # # Crops the face of a person from any image!

    # # OpenCV XML FILE for Frontal Facial Detection using HAAR CASCADES.

    facedata = 'abc.xml'
    cascade = cv2.CascadeClassifier(facedata)

    # # Reading the given Image with OpenCV
    print(image)
    img = cv2.imread(image)
    print(img)

    try:

        # # Some downloaded images are of unsupported type and should be ignored while raising Exception, so for that
        # # I'm using the try/except functions.

        minisize = (img.shape[1], img.shape[0])
        miniframe = cv2.resize(img, minisize)

        faces = cascade.detectMultiScale(miniframe)

        for f in faces:
            (x, y, w, h) = [v for v in f]
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            sub_face = img[y:y + h, x:x + w]

            f_name = list(image.split('\\'))
            f_name = f_name[-1]
            print(f_name)
            # # Change here the Desired directory.

            cv2.imwrite(f_directory+f_name , sub_face)
            print( 'Writing:' + str(f_name))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    images = os.listdir(directory)
    i = 0

    for img in images:
        file = directory + img
        print (i)
        facecrop(file)
        i += 1
