import numpy as np
import cv2
import sys
from glob import glob
import itertools as it

hog = cv2.HOGDescriptor()
hog.setSVMDetector( cv2.HOGDescriptor_getDefaultPeopleDetector() )
img = cv2.imread('personas.jpg')

found, aa = hog.detectMultiScale(img, winStride=(8,8), padding=(32,32), scale=1.05)
for x, y, w, h in found:
    pad_w, pad_h = int(0.15*w), int(0.05*h)
    cv2.rectangle(img, (x+pad_w, y+pad_h), (x+w-pad_w, y+h-pad_h), (0, 255, 0), 1)

cv2.imshow('Deteccion', img)
    
#SALIR (ESC)
while(1):
    tecla = cv2.waitKey(5) & 0xFF
    if tecla == 27:
        break
cv2.destroyAllWindows()
