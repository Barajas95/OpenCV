import cv2
import numpy as np
from matplotlib import pyplot as plt

kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])

cap = cv2.VideoCapture(0)

while(True):
    # Capturar frames y pasarlos a escala de grises.
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    #Filtro gaussiano
    img_gaussian = cv2.GaussianBlur(gray,(3,3),0)

    #Canny
    img_canny = cv2.Canny(img_gaussian,100,200)

    #Sobel
    img_sobelx = cv2.Sobel(img_gaussian,cv2.CV_8U,1,0,ksize=5)
    img_sobely = cv2.Sobel(img_gaussian,cv2.CV_8U,0,1,ksize=5)
    img_sobel = img_sobelx + img_sobely

    #Prewitt
    img_prewittx = cv2.filter2D(img_gaussian, -1, kernelx)
    img_prewitty = cv2.filter2D(img_gaussian, -1, kernely)
    img_prewitt = img_prewittx + img_prewitty
    
    #Mostrar imagen
    cv2.imshow('Original', img)
    cv2.imshow('Canny', img_canny)
    cv2.imshow('Sobel', img_sobel)
    cv2.imshow('Prewitt', img_prewitt)
    
    #Salir con ESC
    tecla = cv2.waitKey(5) & 0xFF
    if tecla == 27:
        break
    
cv2.destroyAllWindows()
