'''
Método básico de segmentación,
busca separar el fondo del objeto de interés

Umbral entre 0 y 255
'''
import cv2
import numpy as np
import imutils

#Imagen
grises = np.zeros((500,600), dtype=np.uint8)

#Fuente del texto
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(grises, 'Umbral: T=130', (100,70), font, 1.5, (255), 2, cv2.LINE_AA)

#Seccionando la imagen

grises[100:300,:200] = 130
grises[100:300,200:400] = 20
grises[100:300,400:600] = 210
grises[300:600,:200] = 35
grises[300:600,200:400] = 255
grises[300:600,400:600] = 70

grises2 = grises.copy()

#Texto

cv2.putText(grises, '130', (60,150), font, 1, (255), 1, cv2.LINE_AA)
cv2.putText(grises, '20', (200,150), font, 1, (255), 1, cv2.LINE_AA)
cv2.putText(grises, '210', (470,150), font, 1, (0), 1, cv2.LINE_AA)
cv2.putText(grises, '35', (70,350), font, 1, (255), 1, cv2.LINE_AA)
cv2.putText(grises, '255', (270,350), font, 1, (255), 1, cv2.LINE_AA)
cv2.putText(grises, '70', (480,350), font, 1, (255), 1, cv2.LINE_AA)
cv2.putText(grises, '130>T?', (40,230), font, 1, (255), 1, cv2.LINE_AA)
cv2.putText(grises, '20>T?', (250,230), font, 1, (255), 1, cv2.LINE_AA)
cv2.putText(grises, '210>T?', (440,230), font, 1, (255), 1, cv2.LINE_AA)
cv2.putText(grises, '35>T?', (50,430), font, 1, (255), 1, cv2.LINE_AA)
cv2.putText(grises, '255>T?', (240,430), font, 1, (255), 1, cv2.LINE_AA)
cv2.putText(grises, '70>T?', (450,430), font, 1, (255), 1, cv2.LINE_AA)

# Si pasa el umbral 255, si no 0
_, binarizada = cv2.threshold(grises2, 130, 255, cv2.THRESH_BINARY)

cv2.imshow('Grises', grises)
cv2.imshow('Binarizada', binarizada)

cv2.waitKey(0)
cv2.destroyAllWindows()

image = cv2.imread('/home/tavo/Documentos/OpenCV/Images/img_1.jpg', 0) #Imagen escala de grises
image = imutils.resize(image, width=400)

_, binarizada = cv2.threshold(image, 180, 225, cv2.THRESH_BINARY)
_, binarazadaInv = cv2.threshold(image, 180, 225, cv2.THRESH_BINARY_INV)

#Trunc - Si se cumple la condición, toma el color del umbral
_, trunc = cv2.threshold(image, 180, 255, cv2.THRESH_TRUNC)

#ToZero - Si pasa el umbral 0, si no, conserva el color
_, toz = cv2.threshold(image, 180, 255, cv2.THRESH_TOZERO)
_, tozInv = cv2.threshold(image, 180, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow('Imagen', image)
cv2.imshow('Tipos: Binary - Binary Inv - Trunc - To Zero - To Zero Inv', np.hstack([binarizada, binarazadaInv, trunc, toz, tozInv]))

cv2.waitKey(0)
cv2.destroyAllWindows()