#Usando espacio de color HSV (Hue Saturation Value)
# Hue        0 - 179
# Saturation 0 - 255
# Value      0 - 255

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

redBajo1 = np.array([0,100,20], np.uint8)
redAlto1 = np.array([8,255,255], np.uint8)

redBajo2 = np.array([175,100,20], np.uint8)
redAlto2 = np.array([179,255,255], np.uint8)

while True:
    ret, frame = cap.read()
    if ret == True:
        #BGR a HSV
        frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #Rangos de color (detectar rojo)
        #Rojo se muestra blanco, lo demás en negro
        maskRed1 = cv2.inRange(frameHSV, redBajo1, redAlto1)
        maskRed2 = cv2.inRange(frameHSV, redBajo2, redAlto2)
        maskRed = cv2.add(maskRed1, maskRed2)
        #En lugar de blanco muestra el color en la imagen
        maskRedvis = cv2.bitwise_and(frame, frame, mask=maskRed)
        
        cv2.imshow('Frame', frame)
        cv2.imshow('MaskRed', maskRed)
        cv2.imshow('MaskRedvis', maskRedvis)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break

cap.release()
cv2.destroyAllWindows()
