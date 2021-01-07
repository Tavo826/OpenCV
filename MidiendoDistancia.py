import cv2
import numpy as np
import imutils

def ordenar_puntos(puntos):
    #Convierte los puntos de las esquinas de la hoja en una lista
    n_puntos = np.concatenate([puntos[0], puntos[1], puntos[2], puntos[3]])

    #ordena los puntos en y
    y_order = sorted(n_puntos, key=lambda n_puntos: n_puntos[1])

    #ordena los 2 primeros puntos en x
    x1_order = y_order[:2]
    x1_order = sorted(x1_order, key=lambda x1_order: x1_order[0])

    #ordena los últimos 2 puntos en x
    x2_order = y_order[2:4]
    x2_order = sorted(x2_order, key=lambda x2_order: x2_order[0])

    return [x1_order[0], x1_order[1], x2_order[0], x2_order[1]]

def roi(imagen, ancho, alto):
    imagen_alineada = None

    #escala de grises
    gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    #binaria
    _, th = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    #contornos externos
    cnts = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    #contorno más grande
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:1]

    for c in cnts:
        epsilon = 0.01 * cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, epsilon, True)

        #si el contorno es rectangular
        if len(approx) == 4:
            puntos = ordenar_puntos(approx)
            pts1 = np.float32(puntos)
            pts2 = np.float32([[0,0], [ancho,0], [0,alto], [ancho,alto]])
            #Redimensiona la vista de la hoja
            M = cv2.getPerspectiveTransform(pts1, pts2)
            imagen_alineada = cv2.warpPerspective(imagen, M, (ancho,alto))

    return imagen_alineada

cap = cv2.VideoCapture('/home/tavo/Imágenes/diezcm.mp4')

while True:
    ret, frame = cap.read()
    if ret == False: break

    #Alineación de la hoja A4
    imagen_A4 = roi(frame, 720, 509) #Tamaño en px

    if imagen_A4 is not None:
        puntos = []
        imagenHSV = cv2.cvtColor(imagen_A4, cv2.COLOR_BGR2HSV)

        #detección de objetos verdes
        verdeBajo = np.array([36,14,0], np.uint8)
        verdeAlto = np.array([56,120,255], np.uint8)
        maskVerde = cv2.inRange(imagenHSV, verdeBajo, verdeAlto)

        #contornos de los objetos verdes
        cnts = cv2.findContours(maskVerde, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:2]

        #Se recorren los contornos
        for c in cnts:

            #Se obtienen las dimensiones de los objetos
            x, y, w, h = cv2.boundingRect(c)
            #Se encierran los objetos en rectángulos
            cv2.rectangle(imagen_A4, (x,y), (x+w, y+h), (255,0,0), 2)
            #Se añaden las dimensiones a la lista
            puntos.append([x,y,w,h])
        
        #Si se tienenlas dimensiones de los 2 objetos
        if len(puntos) == 2:
            #puntos del primer objeto
            x1, y1, w1, h1 = puntos[0]
            #puntos del segundo objeto
            x2, y2, w2, h2 = puntos[1]

            #Si el objeto 1 está a la izquierda del objeto 2
            if x1 < x2:
                distancia_pixeles = abs(x2 - (x1+w1))
                #720 px equivalen a 29.7 cm (tamaño de la hoja)
                distancia_cm = (distancia_pixeles * 29.7) / 720
                cv2.putText(imagen_A4, "{:.2f} cm".format(distancia_cm), (x1 + w1 + distancia_pixeles // 2, y1 - 30), 2, 0.8, (0,0,255), 1, cv2.LINE_AA)
                #Se dibuja una línea guía de distancia
                cv2.line(imagen_A4, (x1 + w1, y1 - 20), (x2, y1 - 20), (0,0,255), 2)
                cv2.line(imagen_A4, (x1 + w1, y1 - 30), (x1 + w1, y1 - 10), (0,0,255), 2)
                cv2.line(imagen_A4, (x2, y1 - 30), (x2, y1 - 10), (0,0,255), 2)
            #Si el objeto 2 está a la izquierda del objeto 1
            else:
                distancia_pixeles = abs(x1 - (x2+w2))
                distancia_cm = (distancia_pixeles * 29.7) / 720
                cv2.putText(imagen_A4, "{:.2f} cm".format(distancia_cm), (x2 + w2 + distancia_pixeles // 2, y2 - 30), 2, 0.8, (0,0,255), 1, cv2.LINE_AA)
                cv2.line(imagen_A4, (x2 + w2, y2 - 20), (x1, y2 - 20), (0,0,255), 2)
                cv2.line(imagen_A4, (x2 + w2, y2 - 30), (x2 + w2, y2 - 10), (0,0,255), 2)
                cv2.line(imagen_A4, (x1, y2 - 30), (x1, y2 - 10), (0,0,255), 2)

        cv2.imshow('Imagen_A4', imagen_A4)        
    
    cv2.imshow('Frame', frame)
    k = cv2.waitKey(30)
    if k == ord('q'): break

cap.release()
cv2.destroyAllWindows()