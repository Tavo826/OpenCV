import cv2
import numpy as np

cap = cv2.VideoCapture('/home/tavo/Imágenes/aeropuerto.mp4')

bgsMOG = cv2.bgsegm.createBackgroundSubtractorMOG()
#Para mejorar la imagen binaria
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))

while True:
    ret, frame = cap.read()
    if ret == False: break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Se dibuja un rectángulo para el texto que avisa el estado del área de análisis
    cv2.rectangle(frame, (0,0), (frame.shape[1], 40), (0,0,0), -1)
    texto_color = (0,255,0)
    texto_estado = 'Estado: No hay movimiento'

    #Puntos del área que se quiere analizar
    area_pts = np.array([[240,320], [480,320], [620,frame.shape[0]], [50,frame.shape[0]]])

    #Se usa una imagen auxiliar se determina el área sobre la cual actuará el detector
    imAux = np.zeros((frame.shape[:2]), np.uint8)
    imAux = cv2.drawContours(imAux, [area_pts], -1, (255), -1)
    #area en escala de grises para sustraer el fondo
    imagen_area = cv2.bitwise_and(gray, gray, mask=imAux)

    #Imagen binaria del área
    fgmask = bgsMOG.apply(imagen_area)
    #reduciendo el ruido
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    fgmask = cv2.dilate(fgmask, None, iterations=2)

    #Obteniendo los contornos que representen personas
    cnts = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

    for c in cnts:
        if cv2.contourArea(c) > 500:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
            texto_estado = 'Estado: Movimiento detectado'
            texto_color = (0,0,255)
    
    #Visualizando el contorno del área en el frame
    cv2.drawContours(frame, [area_pts], -1, texto_color, 2)
    cv2.putText(frame, texto_estado, (10,30), cv2.FONT_HERSHEY_COMPLEX, 1, texto_color, 2)

    cv2.imshow('Frame', frame)
    cv2.imshow('Fgmask', fgmask)
    k = cv2.waitKey(30)
    if k == ord('q'): break

cap.release()
cv2.destroyAllWindows()