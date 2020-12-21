import cv2
import numpy as np

def dibujarContorno(contorno, color):
    for (i,c) in enumerate(contorno):
        M = cv2.moments(c)
        if M['m00'] == 0: M['m00'] == 1
        x = int(M['m10'] / M['m00'])
        y = int(M['m01'] / M['m00'])
        cv2.drawContours(img, [c], 0, color, 2)
        cv2.putText(img, str(i+1), (x-10,y+10), 1, 1, [0,0,0], 1)

amarilloBajo = np.array([20, 100, 20], np.uint8)
amarilloAlto = np.array([35, 255, 255], np.uint8)

rosadoBajo = np.array([140, 150, 20], np.uint8)
rosadoAlto = np.array([160, 255, 255], np.uint8)

moradoBajo = np.array([165, 220, 20], np.uint8)
moradoAlto = np.array([170, 255, 255], np.uint8)

azulBajo = np.array([80, 100, 20], np.uint8)
azulAlto = np.array([102, 255, 255], np.uint8)

naranjaBajo = np.array([5, 100, 20], np.uint8)
naranjaAlto = np.array([15, 255, 255], np.uint8)

img = cv2.imread('/home/tavo/Imágenes/circulo.jpeg')
img = cv2.resize(img, (300,550))
imhsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#Colores

maskAmarillo = cv2.inRange(imhsv, amarilloBajo, amarilloAlto)
maskRosado = cv2.inRange(imhsv, rosadoBajo, rosadoAlto)
maskMorado = cv2.inRange(imhsv, moradoBajo, moradoAlto)
maskAzul = cv2.inRange(imhsv, azulBajo, azulAlto)
maskNaranja = cv2.inRange(imhsv, naranjaBajo, naranjaAlto)

#Contornos

contAmarillo = cv2.findContours(maskAmarillo, cv2.RETR_EXTERNAL\
    , cv2.CHAIN_APPROX_SIMPLE)[0]
contRosado = cv2.findContours(maskRosado, cv2.RETR_EXTERNAL\
    , cv2.CHAIN_APPROX_SIMPLE)[0]
contMorado = cv2.findContours(maskMorado, cv2.RETR_EXTERNAL\
    , cv2.CHAIN_APPROX_SIMPLE)[0]
contAzul = cv2.findContours(maskAzul, cv2.RETR_EXTERNAL\
    , cv2.CHAIN_APPROX_SIMPLE)[0]
contNaranja = cv2.findContours(maskNaranja, cv2.RETR_EXTERNAL\
    , cv2.CHAIN_APPROX_SIMPLE)[0]

#print(len(contRosado))

#Detectando centros para dibujar y contar

dibujarContorno(contAmarillo, [0,255,255])
dibujarContorno(contRosado, [128,0,255])
dibujarContorno(contMorado, [164,73,163])
dibujarContorno(contAzul, [255,0,0])
dibujarContorno(contNaranja, [26,127,273])

#Imagen resumen

imgRes = 255 * np.ones((250,150,3), dtype=np.uint8)
cv2.circle(imgRes, (30,30), 15, (0,255,255), -1)
cv2.circle(imgRes, (30,70), 15, (128,0,255), -1)
cv2.circle(imgRes, (30,110), 15, (164,73,163), -1)
cv2.circle(imgRes, (30,150), 15, (255,0,0), -1)
cv2.circle(imgRes, (30,190), 15, (26,127,273), -1)

cv2.putText(imgRes, str(len(contAmarillo)), (65,40), 1, 2, (0,0,0), 2)
cv2.putText(imgRes, str(len(contRosado)), (65,80), 1, 2, (0,0,0), 2)
cv2.putText(imgRes, str(len(contMorado)), (65,120), 1, 2, (0,0,0), 2)
cv2.putText(imgRes, str(len(contAzul)), (65,160), 1, 2, (0,0,0), 2)
cv2.putText(imgRes, str(len(contNaranja)), (65,200), 1, 2, (0,0,0), 2)

totalColores = len(contAmarillo)\
    + len(contRosado) + len(contMorado)\
    + len(contAzul) + len(contNaranja)

cv2.line(imgRes, (65, 210), (105, 210), (0,0,0), 1)
cv2.putText(imgRes, str(totalColores), (65, 240), 1, 2, (0,0,0), 2)

cv2.imshow('ImgRes', imgRes)

cv2.imshow('Imagen', img)
#cv2.imshow('mask', maskRosado)
cv2.waitKey(0)
cv2.destroyAllWindows()