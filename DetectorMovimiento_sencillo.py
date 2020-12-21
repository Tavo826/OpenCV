#Como toma el fondo estático, no se puede mover la cámara luego de correrlo
#Aparecen problemas si cambia la iluminación del fondo

import cv2

cap = cv2.VideoCapture(0)
i = 0

while True:
    ret, frame = cap.read()
    if not ret: break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Se toma la imagen 20
    if i == 20:
        bgGray = gray
    #Se diferencia el objeto que se mueve
    if i > 20:
        dif = cv2.absdiff(gray, bgGray)
        _, th = cv2.threshold(dif, 40, 255, cv2.THRESH_BINARY)
        conts, _ = cv2.findContours(th, cv2.RETR_EXTERNAL\
            , cv2.CHAIN_APPROX_SIMPLE)
        cv2.imshow('Th', th)
        #cv2.imshow('Dif', dif)

        for c in conts:
            area = cv2.contourArea(c)
            if area > 9000:
                x, y, w, h = cv2.boundingRect(c)
                cv2.rectangle(frame, (x,y), (x+w, y+h)\
                    , (0,255,0), 2)

    cv2.imshow('Frame', frame)

    i += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()