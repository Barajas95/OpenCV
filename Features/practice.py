from helpers import pyramid
from helpers import sliding_window
import cv2
import time

face_cascade = cv2.CascadeClassifier('C:\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_default.xml')
path = 'C:/Users/Barajas/Downloads/9no Semestre/Computer Vision/Features/pruebaWindows/'
image = cv2.imread('sliding_window.jpg')
(winW, winH) = (128, 128)
contador=0

for resized in pyramid(image, scale=1.5):
	for (x, y, window) in sliding_window(resized, stepSize=32, windowSize=(winW, winH)):
		if window.shape[0] != winH or window.shape[1] != winW:
			continue
		clone = resized.copy()
		crop = clone[y:y+window.shape[1], x:x+window.shape[0]]
		gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(gray, 1.3, 5)
		for (x,y,w,h) in faces:
			cv2.rectangle(crop,(x,y),(x+w,y+h),(255,0,0),2)
			roi_gray = gray[y:y+h, x:x+w]
			roi_color = crop[y:y+h, x:x+w]
		cv2.imwrite(path+str(contador)+'window.png', crop)
		cv2.rectangle(clone, (x, y), (x + winW, y + winH), (0, 255, 0), 2)
		cv2.imshow("Window", clone)
		contador=contador+1
		cv2.waitKey(1)
		time.sleep(0.025)
cv2.destroyAllWindows()
