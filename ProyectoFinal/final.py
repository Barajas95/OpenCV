import cv2
import numpy as np
import pytesseract
from PIL import Image, ImageEnhance
from imutils.object_detection import non_max_suppression
import os
import glob
import sys

path = 'C:/Users/Barajas/Downloads/9no Semestre/Computer Vision/Proyecto Final/results/'
path2 = 'C:/Users/Barajas/Downloads/9no Semestre/Computer Vision/Proyecto Final'

#Azules:
azul_bajos = np.array([100,65,75], dtype=np.uint8)
azul_altos = np.array([130, 255, 255], dtype=np.uint8)

contador=1
kernel = np.ones((3,3),np.uint8)

#Delete previous files
files = glob.glob(path + '*.png')
for f in files:
    os.remove(f)

#Delete previous files (Filtrada.png, Foto.png y Detector.png)
files = glob.glob(path2 + '*.png')
for f in files:
    os.remove(f)

#Camara
print("Presione espacio para tomar foto")
cap = cv2.VideoCapture(0)
while(1):
	leido, frame = cap.read()
	if(leido == True):
		cv2.imshow('Camara', frame)
		teclado = cv2.waitKey(5) & 0xFF
		if teclado == 32:
			cv2.destroyAllWindows()
			cv2.imshow("Foto", frame)
			print("Foto tomada correctamente, desea trabajar con esa foto")
			teclado = cv2.waitKey(5000) & 0xFF
			if teclado == 32:
				print("Fotografia seleccionada correctamente")
				cv2.imwrite('Foto.png',frame)
				image = Image.open('Foto.png')
				cap.release()
				cv2.destroyAllWindows()
				break
			else:
				print("No se selecciono la fotografia, tomar otra")
				cv2.destroyAllWindows()
	else:
		print("Error al acceder a la camara")
		cap.release()
		image = Image.open('prueba02.jpg')
		break

print("ARRANCANDO PROGRAMA...")
#Contraste
contrast = ImageEnhance.Contrast(image)
image = contrast.enhance(3)
image = np.asarray(image)
r, g, b = cv2.split(image)
contrast = cv2.merge([b, g, r])
image = cv2.cvtColor(contrast, cv2.COLOR_BGR2GRAY)
cv2.imshow('Contraste', image)

#Filtro
img_filter1 = cv2.fastNlMeansDenoising(image, None, 9, 13)
img_filter2 = cv2.bilateralFilter(img_filter1,9,75,75)
cv2.imshow('Filtro', img_filter2)

#Binarizacion
adaptativeThresholdGaussian = cv2.adaptiveThreshold(img_filter2,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)

#Operaciones morfologicas
#adaptativeThresholdGaussian = cv2.erode(adaptativeThresholdGaussian ,kernel,iterations = 1)
#adaptativeThresholdGaussian = cv2.dilate(adaptativeThresholdGaussian ,kernel,iterations = 1)

#Guardar imagen binaria
cv2.imwrite('Filtrada.png', adaptativeThresholdGaussian)
cv2.imshow('Binarizada', adaptativeThresholdGaussian)

#Dimensiones de la imagen y el marco
image = cv2.imread('Filtrada.png')
orig = image.copy()
(H, W) = image.shape[:2]
(newW, newH) = (320, 320)
rW = W / float(newW)
rH = H / float(newH)
image = cv2.resize(image, (newW, newH))
(H, W) = image.shape[:2]

print("DETECTANDO PALABRAS...")
#Definir las capas del EAST detector y crear la CNN.
layerNames = [
	"feature_fusion/Conv_7/Sigmoid",
	"feature_fusion/concat_3"]
net = cv2.dnn.readNet('east_detection.pb')

#Crear blob
blob = cv2.dnn.blobFromImage(image, 1.0, (W, H), (123.68, 116.78, 103.94), swapRB=True, crop=False)
net.setInput(blob)
(scores, geometry) = net.forward(layerNames)

# grab the number of rows and columns from the scores volume, then initialize our set of bounding box rectangles and corresponding confidence scores
(numRows, numCols) = scores.shape[2:4]
rects = []
confidences = []

# loop over the number of rows
for y in range(0, numRows):
	# extract the scores (probabilities), followed by the geometrical data used to derive potential bounding box coordinates that surround text
	scoresData = scores[0, 0, y]
	xData0 = geometry[0, 0, y]
	xData1 = geometry[0, 1, y]
	xData2 = geometry[0, 2, y]
	xData3 = geometry[0, 3, y]
	anglesData = geometry[0, 4, y]

	# loop over the number of columns
	for x in range(0, numCols):
		# if our score does not have sufficient probability, ignore it
		if scoresData[x] < 0.3:
			continue

		# compute the offset factor as our resulting feature maps will be 4x smaller than the input image
		(offsetX, offsetY) = (x * 4.0, y * 4.0)

		# extract the rotation angle for the prediction and then compute the sin and cosine
		angle = anglesData[x]
		cos = np.cos(angle)
		sin = np.sin(angle)

		# use the geometry volume to derive the width and height of the bounding box
		h = xData0[x] + xData2[x]
		w = xData1[x] + xData3[x]

		# compute both the starting and ending (x, y)-coordinates for the text prediction bounding box
		endX = int(offsetX + (cos * xData1[x]) + (sin * xData2[x]))
		endY = int(offsetY - (sin * xData1[x]) + (cos * xData2[x]))
		startX = int(endX - w)
		startY = int(endY - h)

		# add the bounding box coordinates and probability score to our respective lists
		rects.append((startX, startY, endX, endY))
		confidences.append(scoresData[x])

# apply non-maxima suppression to suppress weak, overlapping bounding boxes
boxes = non_max_suppression(np.array(rects), probs=confidences)

# loop over the bounding boxes
for (startX, startY, endX, endY) in boxes:
	# scale the bounding box coordinates based on the respective ratios
	startX = int(startX * rW)
	startY = int(startY * rH)
	endX = int(endX * rW)
	endY = int(endY * rH)

	# draw the bounding box on the image
	cv2.rectangle(orig, (startX-10, startY-10), (endX+10, endY+10), (255, 0, 0), 1)

print("PROCESANDO PALABRAS...")
#Proccess words.
hsv = cv2.cvtColor(orig, cv2.COLOR_BGR2HSV)
mascara_azul = cv2.inRange(hsv, azul_bajos, azul_altos)
hsv2,ctrs, hier = cv2.findContours(mascara_azul, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])
for i, ctr in enumerate(ctrs):
	# Get bounding box
	x, y, w, h = cv2.boundingRect(ctr)

	# Getting ROI
	roi = image[y:y+h, x:x+w]

	#Image to text
	try:
		print(pytesseract.image_to_string(roi))
	except:
		print("")

	#Crop and save ROI
	cv2.imwrite(path+str(contador)+'window.png', roi)
	contador = contador+1

#Output
cv2.imshow('Detector EAST', orig)
cv2.imwrite('Detector.png', orig)

#Close program (ESC)
while(1):
    tecla = cv2.waitKey(5) & 0xFF
    if tecla == 27:
        break

print("CERRANDO PROGRAMA...")
cv2.destroyAllWindows()
