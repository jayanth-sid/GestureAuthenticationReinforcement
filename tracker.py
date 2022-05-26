import videoRec
import HandTrackingModule as htm
import cv2
import numpy as np
import biggestImageObject

def run():
    frames = videoRec.cap(3)
    #################################################
    white_img = np.zeros((720,720,3),np.uint8)
    h = len(white_img)
    w = len(white_img[0])
    xp,yp = 0,0
    ##################################################
    detector = htm.handDetector(detectionCon=0.6)
    ##################################################



    for y in range(h):
        for x in range(w):
            white_img[y,x] = [255,255,255]
    imgCanvas = white_img

    for img in frames:
        img = cv2.flip(img, 1)
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)
        if len(lmList) != 0:

            x1,y1 = lmList[8][1::]
            if xp == 0 and yp == 0:
                xp, yp = x1, y1
            cv2.line(imgCanvas, (xp, yp), (x1, y1), (0,0,0), 15)
            xp, yp = x1, y1

    imgCanvas = biggestImageObject.larestObj(imgCanvas)
    return imgCanvas