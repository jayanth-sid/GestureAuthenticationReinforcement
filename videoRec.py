import cv2
import time
def cap(duartion):
    vidcap = cv2.VideoCapture(0,)

    count = 0
    frames = []
    started = False
    while True:
        success,image = vidcap.read()
        if success and not started:
            start_time = time.time()*1000
            started = True
            curr_time = start_time
        cv2.imshow("as",image)
        frames.append(image)
        count += 1
        curr_time = time.time() * 1000
        if cv2.waitKey(1) & int(curr_time - start_time) > duartion*1000:
            vidcap.release()
            cv2.destroyAllWindows()
            return frames


