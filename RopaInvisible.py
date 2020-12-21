#No funciona - mejorar colores

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

bg = None
i = 0

#Color que se quiere esconder

#Rojo
rojoBajo1 = np.array([0,150,40], np.uint8)
rojoAlto1 = np.array([8,255,155], np.uint8)
rojoBajo2 = np.array([170,150,40], np.uint8)
rojoAlto2 = np.array([180,255,255], np.uint8)

#Azul
azulBajo = np.array([70,100,20], np.uint8)
azulAlto = np.array([90,155,255], np.uint8)

while True:
    ret, frame = cap.read()
    if not ret: break
    #Imagen del fondo para que se vea sobre la ropa
    #Se toma al inicio del frame
    if i == 0:
        cv2.waitKey(10)
        if bg is None: bg = frame
        i += 1

    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    maskRojo1 = cv2.inRange(frameHSV, rojoBajo1, rojoAlto1)
    maskRojo2 = cv2.inRange(frameHSV, rojoBajo2, rojoAlto2)
    maskRojo = cv2.add(maskRojo1, maskRojo2)

    maskAzul = cv2.inRange(frameHSV, azulBajo, azulAlto)

    #filtro para eliminar ruido del fondo
    mask = cv2.medianBlur(maskAzul, 13)
    #Dilatando la máscara para eliminar bordes de colores
    kernel = np.ones((5,5), np.uint8)
    mask = cv2.dilate(mask, kernel, iterations=1)

    #Operando la imagen del fondo con la máscara actual
    areaColor = cv2.bitwise_and(bg, bg, mask=mask)

    #Invirtiendo máscara
    maskInv = cv2.bitwise_not(mask)

    #Operando la imagen del fondo con la máscara actual
    sinAreaColor = cv2.bitwise_and(frame, frame, mask=maskInv)

    #Sumando areaColor y sinAreaColor
    finalFrame = cv2.addWeighted(areaColor, 1, sinAreaColor, 1, 0)

    cv2.imshow('Frame', frame)
    #cv2.imshow('Mask', mask)
    cv2.imshow('AreaColor', areaColor)
    #cv2.imshow('MaskInv', maskInv)
    cv2.imshow('sinAreaColor', sinAreaColor)
    cv2.imshow('FinalFrame', finalFrame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
