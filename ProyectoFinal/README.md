# Reconocimiento de texto manuscrito
Descripción.
## Instalación de librerías y edición del archivo principal. 🔧
La parte realmente importante para poder ejecutar el proyecto es tener instaladas las versiones de Python 2.7.9 y OpenCV 3.4.3. Esto se puede comprobar con el CMD de Windows.<br>
```Consola
> Python --version
> Python
>>> import cv2
>>> cv2.__version__
```
De la misma manera, se deben tener instaladas las siguientes librerías para que al momento de importarlas no se genere ningún tipo de error.<br>
```Python
import cv2
import numpy as np
import pytesseract
from PIL import Image, ImageEnhance
from imutils.object_detection import non_max_suppression
import os
import glob
import sys
```
Ya que se tienen las librerías instaladas correctamente, el directorio del proyecto debe ser el siguiente: <br>
```Consola
|
|--- ProyectoFinal
    |--- results
    |--- east_detection.pb
    |--- final.py
    |--- prueba01.jpg
    |--- prueba02.jpg
    |--- prueba03.jpg
```
El archivo llamado "east_detection.pb" puede ser descargado de https://drive.google.com/file/d/1Slsqq6MXYMuCHe3sqkxtabz_Us-P909n/view?usp=sharing <br>

Una vez teniendo todos los archivos en orden, será necesario editar el archivo "final.py" con cualquier editor de texto. La parte que debe corregirse es la ruta de ejecución del proyecto. Las líneas a editar son las siguientes: <br>
```Python
path = 'C:/Users/Barajas/Downloads/9no Semestre/Computer Vision/ProyectoFinal/results/' #Localización del directorio "results"
path2 = 'C:/Users/Barajas/Downloads/9no Semestre/Computer Vision/ProyectoFinal' #Localizacion del directorio del proyecto
```
Ejecutar el archivo "final.py" <br>

## Navegación a través del programa principal. ⌨️
Una vez ejecutado el archivo "final.py" se pueden presentar dos situaciones: <br>
1.- Si el programa no puede encontrar la cámara principal de la computadora, el archivo que será analizado como prueba del proyecto será "prueba03.jpg" <br>
2.- Si la cámara es detectada correctamente, se abrirá una ventana con los frames de la cámara. Para tomar una fotografía se debe presionar la tecla "Espacio" e inmediatamente se tomará la captura. Se le permitirá al usuario seleccionar entre la fotografía tomada (volviendo a presionar la tecla "Espacio" antes de 5 segundos) u la opción de tomar otra (presionar cualquier tecla a excepción de Espacio" o esperar 5 segundos). <br>

## Versiones 📌
-- Version 1 (Proyecto inicial) <br>
-- <br>

## Autores ✒️
* **Rubén Barajas Curiel** - *Desarrollo del software, documentación y soporte* - [Barajas95](https://github.com/Barajas95)
* **Víctor Daniel Green Silva** - *Desarrollo del software* - [VictorGreen](https://github.com/VictorGreen)
* **Ismael Lizárraga González** - *Desarrollo del software*

## Licencia 📄
Este proyecto está bajo la licencia de código libre. El software puede ser utilizado o alterado bajo su consentimiento.

