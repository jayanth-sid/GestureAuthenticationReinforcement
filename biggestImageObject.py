import cv2
import numpy as np
import time

def larestObj(img):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert to grayscale
    # threshold to get just the signature (INVERTED)
    retval, thresh_gray = cv2.threshold(gray, thresh=100, maxval=255,type=cv2.THRESH_BINARY_INV)


    contours, hierarchy = cv2.findContours(thresh_gray,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

    # Find object with the biggest bounding box
    mx = (0,0,0,0)      # biggest bounding box so far
    mx_area = 0
    for cont in contours:
        x,y,w,h = cv2.boundingRect(cont)
        area = w*h
        if area > mx_area:
            mx = x,y,w,h
            mx_area = area
    x,y,w,h = mx

    # Output to files
    roi=img[y-10:y+h+10,x-10:x+w+10]

    return roi
