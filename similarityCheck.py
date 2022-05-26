import cv2
from skimage.metrics import structural_similarity

class similarityCheck():
    def __init__(self):
        None
    def check_orb_similarity(self,img1,img2):
        orb = cv2.ORB_create()

        kp_a , desc_a = orb.detectAndCompute(img1,None)
        kp_b , desc_b = orb.detectAndCompute(img2,None)

        bf = cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck = True)

        matches = bf.match(desc_a , desc_b)

        similar_regions = [i for i in matches if i.distance < 50]
        if len(matches) == 0:
            return 0
        return len(similar_regions)/len(matches)

    def check_structural_similarity(self,img1,img2):
        sim,diff = structural_similarity(img1,img2,full = True)
        return sim

def main():
    pass

if __name__ == "__main__":
    main()
