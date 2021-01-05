import cv2
import numpy as np
import imutils

rojoBajo1 = np.array([0, 140, 90], np.uint8)
rojoAlto1 = np.array([8, 255, 255], np.uint8)
rojoBajo2 = np.array([160, 140, 90], np.uint8)
rojoAlto2 = np.array([180, 255, 255], np.uint8)

image = cv2.imread('/home/tavo/Imágenes/img_01.jpeg')
image = imutils.resize(image, width=640)

imGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#Para poder sumar
imGray = cv2.cvtColor(imGray, cv2.COLOR_GRAY2BGR)
imHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#Detectando el rojo
maskRojo1 = cv2.inRange(imHSV, rojoBajo1, rojoAlto1)
maskRojo2 = cv2.inRange(imHSV, rojoBajo2, rojoAlto2)
maskRojo = cv2.add(maskRojo1, maskRojo2)
maskRojo = cv2.medianBlur(maskRojo, 7)

redDetected = cv2.bitwise_and(image, image, mask=maskRojo)

#Fondo escala de grises
invMask = cv2.bitwise_not(maskRojo)
bgGray = cv2.bitwise_and(imGray, imGray, mask=invMask)

#Sumando
sumImage = cv2.add(bgGray, redDetected)

cv2.imshow('Image', image)
cv2.imshow('Red', redDetected)
cv2.imshow('Bg', bgGray)
cv2.imshow('Final Image', sumImage)
cv2.waitKey(0)
cv2.destroyAllWindows()