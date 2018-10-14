import cv2 as cv
import numpy as np

img = cv.imread('casa.png')
gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    
sift = cv.xfeatures2d.SIFT_create()
kp, des = sift.detectAndCompute(gray,None)

cv.drawKeypoints(gray, kp, img, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.imshow('Sift', img)

while(1):
    #Salir con ESC
    tecla = cv.waitKey(5) & 0xFF
    if tecla == 27:
        break

cv.destroyAllWindows()