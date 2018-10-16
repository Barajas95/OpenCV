import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    # Capturar frames y pasarlos a escala de grises.
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    #ret,th = cv2.threshold(gray,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)  #Binarizacion OTSU
    #th = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2) #Binarizacion adaptativa
    th = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2) #Binarizacion adaptativa gaussiana

    #Mostrar imagen
    cv2.imshow('Original', img)
    cv2.imshow('Binarizacion', th)
    
    #Salir con ESC
    tecla = cv2.waitKey(5) & 0xFF
    if tecla == 27:
        break
        
# Cuando todo termine, liberar la camara y cerrar todo
cap.release()
cv2.destroyAllWindows()