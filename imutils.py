# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 19:33:02 2018

@author: YOGENDER-PC
"""

import numpy as np
import cv2

def translation(image, x, y):
    m = np.float32([[1,0,x], [0,1,y]])
    shifted = cv2.warpAffine(image, m, (image.shape[1], image.shape[0]))
    return shifted


def rotate(image,center, degree, size):
    if center == None :
        (h,w) = image.shape[:2]
        center = (w//2, h//2)
    M = cv2.getRotationMatrix2D(center, degree, size)
    rotate = cv2.warpAffine(image,M, (image.shape[1], image.shape[0]))
    return rotate 

def resize(image, width = None, height = None, inter = cv2.INTER_CUBIC):
    
    dim = None
    (h, w) = image.shape[:2]
    
    if width is None and height is None :
        return image
    if width is None:
        r = height/float(h)
        dim = (int(w * r), height)
    else :
        
        r = width/float(w)
        dim = (width, int(h * r))
        
    resized = cv2.resize(image, dim, interpolation = inter)
    return resized
