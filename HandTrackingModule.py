import cv2
import mediapipe as mp
import time

class handDetector():
    def __init__(self,mode=False,maxHands = 2,modelComp = 1,detectionCon = 0.5,trackCon = 0.5 ):
        self.mode = mode
        self.maxHands = maxHands
        self.modelComp = modelComp
        self.detectionCon = detectionCon
        self.trackingCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,self.maxHands,self.modelComp,self.detectionCon,self.trackingCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.tipIds = [4,8,12,16,20]

    def findHands(self,img,draw = True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handlms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handlms,self.mpHands.HAND_CONNECTIONS)
        return img


    def findPosition(self,img,handNumber=0,draw=True):
        self.lmList = []
        if self.results.multi_hand_landmarks:
            currHand = self.results.multi_hand_landmarks[handNumber]
            for id,lm in enumerate(currHand.landmark):
                h , w, c = img.shape
                cx , cy = int(lm.x*w),int(lm.y*h)
                self.lmList.append([id,cx,cy])
                if draw :
                    cv2.circle(img,(cx,cy),7,(0,0,0),cv2.FILLED)

        return self.lmList


def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()
    while True:
        success, img = cap.read()
        img = detector.findHands(img,draw=False)
        lmList = detector.findPosition(img)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 0, 0), 3)
        cv2.imshow("image", img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()