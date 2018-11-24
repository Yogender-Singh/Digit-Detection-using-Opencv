# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 11:28:10 2018

@author: YOGENDER
"""

from __future__ import print_function
from sklearn.externals import joblib
from hog import HOG
import dataset
import argparse
import mahotas
import cv2
import imutils
import time

FPS = 500
last_time = time.time()

# command line parsing
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", required = True,
help = "path to where the model will be stored")
#ap.add_argument("-i", "--image", required = True,
#help = "path to the image file")
args = vars(ap.parse_args())

#loading pretrain model from disk
model = joblib.load(args["model"])


# the HOG descriptor is instantiated with the exact same parameters as during the training phase 
hog = HOG(orientations = 18, pixelsPerCell = (10, 10),
cellsPerBlock = (1, 1), transform = True)


# initializing camera
video_capture = cv2.VideoCapture(0)
while True:
    _, frame = video_capture.read() # extract frame live camera
    
    


    # Image processing
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 30, 150)
    (_, cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)

    cnts = sorted([(c, cv2.boundingRect(c)[0]) for c in cnts], key =
    lambda x: x[1])



    for (c, _) in cnts:
      (x, y, w, h) = cv2.boundingRect(c)

      if w >= 7 and h >= 20:
          roi = gray[y:y + h, x:x + w] #cropping the image
          thresh = roi.copy()
          T = mahotas.thresholding.otsu(roi) # finding the best threshold value
          thresh[thresh > T] = 255
          thresh = cv2.bitwise_not(thresh) # set pixels in ON and OFF 

          thresh = dataset.deskew(thresh, 20)
          thresh = dataset.center_extent(thresh, (20, 20))
          #cv2.imshow("thresh", thresh)
          hist = hog.describe(thresh)
          
          # prediction using pretrain model
          digit = model.predict([hist])[0]
          print("I think that number is: {}".format(digit))
          
          new_time = time.time()
    # see how many milliseconds we have to sleep for
    # then divide by 1000.0 since time.sleep() uses seconds
          sleep_time = ((1000.0 / FPS) - (new_time - last_time)) / 1000.0
          if sleep_time > 0:
               time.sleep(sleep_time)
               last_time = new_time
          # creating rectangle around the image putting and predicted label 
          cv2.rectangle(frame, (x, y), (x + w, y + h),
          (0, 255, 0), 1)
          cv2.putText(frame, str(digit), (x - 10, y - 10),
          cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)
          #cv2.imshow("image", frame)
          
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    
video_capture.release()
cv2.destroyAllWindows()    
