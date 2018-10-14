import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while(True):
    #Capturar frames.
    ret, img = cap.read()
    gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    
    #Sift y key point.
    sift = cv.xfeatures2d.SIFT_create()
    kp, des = sift.detectAndCompute(gray,None)
    cv.drawKeypoints(gray, kp, img, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    
    #Mostrar imagen.
    cv.imshow('Sift', img)

    #Salir con ESC
    tecla = cv.waitKey(5) & 0xFF
    if tecla == 27:
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
