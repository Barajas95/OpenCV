import cv2
import numpy as np

img = cv2.imread('lena.png',0)
rows,cols = img.shape

M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('Original',img)
cv2.imshow('Desplazamiento',dst)

#SALIR (ESC)
while(1):
    tecla = cv2.waitKey(5) & 0xFF
    if tecla == 27:
        break

cv2.destroyAllWindows()
