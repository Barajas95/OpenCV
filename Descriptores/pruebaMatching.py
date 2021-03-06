import cv2 as cv
import numpy as np

img1 = cv.imread('box.png',0)
img2 = cv.imread('box_in_scene.png',0)

# Initiate STAR detector
orb = cv.ORB_create()

# Find the keypoints and descriptors with SIFT
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

# Create BFMatcher object
bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)

# Match descriptors
matches = bf.match(des1,des2)

# Sort them in the order of their distance
matches = sorted(matches, key = lambda x:x.distance)

# Draw first 10 matches
img3 = cv.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)
    
#Mostrar imagen.
cv.imshow('Matching', img3)

while(1):
    #Salir con ESC
    tecla = cv.waitKey(5) & 0xFF
    if tecla == 27:
        break

cv.destroyAllWindows()
