import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while(True):
    #Capturar frames
    ret, img = cap.read()
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    
    # Initiate STAR detector
    orb = cv.ORB_create()

    # find the keypoints with ORB
    kp = orb.detect(img,None)

    # compute the descriptors with ORB
    kp, des = orb.compute(img, kp)

    # draw only keypoints location,not size and orientation
    cv.drawKeypoints(gray,kp,img,color=(0,255,0), flags=0)
    
    #Mostrar imagen
    cv.imshow('ORB', img)

    #Salir con ESC
    tecla = cv.waitKey(5) & 0xFF
    if tecla == 27:
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
