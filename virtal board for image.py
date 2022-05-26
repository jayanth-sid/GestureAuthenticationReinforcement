import cv2
import numpy as np
import time
import os
import HandTrackingModule as htm
from datetime import datetime
import biggestImageObject

thickness = 7
xp = 0
yp = 0

white_img = np.zeros((720,720,3),np.uint8)
h = len(white_img)
w = len(white_img[0])

for y in range(h):
    for x in range(w):
        white_img[y,x] = [255,255,255]

imgCanvas = white_img

cap = cv2.VideoCapture(1,cv2.CAP_DSHOW)
cap.set(3,720)
cap.set(4,720)

detector = htm.handDetector(detectionCon=0.6)

while True:

    success , img = cap.read()
    img = cv2.flip(img,1)
    img = detector.findHands(img)
    lmList = detector.findPosition(img,draw=False)
    if len(lmList) != 0:

        #index finger
        x1,y1 = lmList[8][1::]
        #middle finger
        x2,y2 = lmList[12][1::]

    fingers = detector.fingersUp()
    #print(fingers)

    if fingers.count(1) == 5:
        #print("5 up")
        white_img = np.zeros((720, 720, 3), np.uint8)
        h = len(white_img)
        w = len(white_img[0])

        for y in range(h):
            for x in range(w):
                white_img[y, x] = [255, 255, 255]

        imgCanvas = white_img

    elif fingers.count(1) == 4:
        imgCanvas = biggestImageObject.larestObj(imgCanvas)
        imgCanvas = cv2.resize(imgCanvas,(150,150))
        cv2.imwrite('image1.jpg',imgCanvas)
        print('saved')
        cap.release()
        cv2.destroyAllWindows()
        break




    elif fingers[1] and fingers[2]:
        #print('free move')
        cv2.rectangle(img, (x1, y1 - 15), (x2, y2 + 15), (255, 0, 255), cv2.FILLED)
        xp,yp = 0,0
    elif fingers[1] and fingers[2]!=1:
        #print('draw')
        if xp==0 and yp == 0:
            xp , yp = x1,y1
        cv2.circle(img, (x1, y1),6, (255, 0, 255), cv2.FILLED)
        cv2.line(imgCanvas,(xp,yp),(x1,y1),(0,0,0),thickness)
        xp,yp = x1,y1

    cv2.imshow("img",img)
    cv2.imshow("canvas",imgCanvas)
    cv2.waitKey(1)
