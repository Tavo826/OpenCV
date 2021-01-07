import cv2
import numpy as np
import imutils

cap = cv2.VideoCapture('/home/tavo/Imágenes/autos.mp4')
#Detector de movimiento
bgsMOG = cv2.bgsegm.createBackgroundSubtractorMOG()
#Para mejorar la imagen binaria
kernel = cv2.getStructuringElement(cv2.MORPH_OPEN, (3,3))
car_counter = 0

while True:
    ret, frame = cap.read()
    if ret == False: break

    frame = imutils.resize(frame, 640)

    #Puntos extremos del área a analizar
    area_pts = np.array([[330, 216], [frame.shape[1] - 80, 216], [frame.shape[1] - 80, 271], [330, 271]])

    #Determinando el área usando imagen auxiliar
    imAux = np.zeros(frame.shape[:2], np.uint8)
    imAux = cv2.drawContours(imAux, [area_pts], -1, (255), -1)
    image_area = cv2.bitwise_and(frame, frame, mask=imAux)

    #Obteniendo imagen binaria
    fgmask = bgsMOG.apply(image_area)
    #Mejorando la imagen binaria
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel)
    fgmask = cv2.dilate(fgmask, None, iterations=5)

    #Detectando contornos
    cnts = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

    for c in cnts:
        if cv2.contourArea(c) > 1500:
            x, y, w, h = cv2.boundingRect(c)
            #Encierra el auto cuando lo detecta
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,255), 1)
            #Si el auto cruza entre 440 y 460 se cuenta
            if 440 < (x+w) < 460:
                car_counter += 1
                #La línea amarilla cambia a verde
                cv2.line(frame, (450, 216), (450, 271), (0,255,0), 3)

    #Dibujando el área en el frame
    cv2.drawContours(frame, [area_pts], -1, (255,0,255), 2)
    cv2.line(frame, (450, 216), (450, 271), (0,255,255), 1)
    cv2.rectangle(frame, (frame.shape[1] - 70, 215), (frame.shape[1] - 5, 270), (0,255,0), 2)
    cv2.putText(frame, str(car_counter), (frame.shape[1] - 55, 270), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,255,0), 2)

    print(car_counter)

    cv2.imshow('Frame', frame)
    k = cv2.waitKey(30)
    if k == ord('q'): break

cap.release()
cv2.destroyAllWindows()