# Reconocimiento de texto manuscrito
El núcleo de la detección de texto es el diseño de features que permitan distinguir texto del fondo en el que se encuentra. Un enfoque tradicional a esto ha sido el diseñar manualmente features que capturen las propiedades del texto, al mismo tiempo que con métodos basados en Deep Learning se pueda aprender y entrenar
## Instalación de librerías y edición del archivo principal. 🔧
* La parte realmente importante para poder ejecutar el proyecto es tener instaladas las versiones de Python 2.7.9 y OpenCV 3.4.3. Esto se puede comprobar con el CMD de Windows.<br>
```Consola
> Python --version
> Python
>>> import cv2
>>> cv2.__version__
```
* De la misma manera, se deben tener instaladas las siguientes librerías para que al momento de importarlas no se genere ningún tipo de error.<br>
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
```Consola
> pip install opencv-python
> pip install opencv-contrib-pytho
> pip install opencv-contrib-python-headless
> pip install numpy
> pip install pytesseract
> pip install pillow
> pip install imutils
```

* Ya que se tienen las librerías instaladas correctamente, el directorio del proyecto debe ser el siguiente: <br>
```Consola
|
|--- ProyectoFinal
    |--- results
       |--- Ignore.txt
    |--- east_detection.pb
    |--- final.py
    |--- ProyectoFinal.pdf
    |--- prueba01.jpg
    |--- prueba02.jpg
    |--- prueba03.jpg
    |--- README.md
```
* El archivo llamado "east_detection.pb" puede ser descargado de https://drive.google.com/file/d/1Slsqq6MXYMuCHe3sqkxtabz_Us-P909n/view?usp=sharing <br>

* Una vez teniendo todos los archivos en orden, será necesario editar el archivo "final.py" con cualquier editor de texto. La parte que debe corregirse es la ruta de ejecución del proyecto. Las líneas a editar son las siguientes: <br>
```Python
path = 'C:/Users/Barajas/Downloads/9no Semestre/Computer Vision/ProyectoFinal/results/' #Localización del directorio "results"
path2 = 'C:/Users/Barajas/Downloads/9no Semestre/Computer Vision/ProyectoFinal' #Localizacion del directorio del proyecto
```
* Ejecutar el archivo "final.py" <br>

## Navegación a través del programa principal. ⌨️
Una vez ejecutado el archivo "final.py" se pueden presentar dos situaciones: <br>
1.- Si el programa no puede encontrar la cámara principal de la computadora, el archivo que será analizado como prueba del proyecto será "prueba02.jpg" <br>
2.- Si la cámara es detectada correctamente, se abrirá una ventana con los frames de la cámara. Para tomar una fotografía se debe presionar la tecla _Espacio_ e inmediatamente se tomará la captura. Se le permitirá al usuario seleccionar entre la fotografía tomada (volviendo a presionar la tecla _Espacio_ antes de 5 segundos) o la opción de tomar otra fotografía (presionar cualquier tecla a excepción de _Espacio_ o esperar 5 segundos). <br>

## Versiones 📌
-- Version 1 (Proyecto inicial) <br>
-- <br>

## Autores ✒️
* **Rubén Barajas Curiel** - *Desarrollo del software, documentación y soporte* - [Barajas95](https://github.com/Barajas95)
* **Víctor Daniel Green Silva** - *Desarrollo del software* - [VictorGreen](https://github.com/VictorGreen)
* **Ismael Lizárraga González** - *Desarrollo del software*

## Licencia 📄
Este proyecto está bajo la licencia de código libre. El software puede ser utilizado o alterado bajo su consentimiento.

