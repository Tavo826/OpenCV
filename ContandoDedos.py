import cv2
import numpy as np
import imutils

cap = cv2.VideoCapture(0)
bg = None

while True:

    ret, frame = cap.read()
    if ret == False: break

    #Efecto espejo
    frame = cv2.flip(frame, 1)

    #Para capturar el fondo
    frameAux = frame.copy()

    if bg is not None:
        #cv2.imshow('Bg', bg)
        ROI = frame[50:400, 350:620]
        cv2.rectangle(frame, (350+2, 50+2), (620+2, 400+2), (0,255,255), 1)
        grayROI = cv2.cvtColor(ROI, cv2.COLOR_BGR2GRAY)

        bgROI = bg[50:400, 350:620]

        #Realizando la diference del frame y el bg
        dif = cv2.absdiff(grayROI, bgROI)
        #Aplicando umbralización
        _, th = cv2.threshold(dif, 30, 255, cv2.THRESH_BINARY)
        th = cv2.medianBlur(th, 7)

        #Detectando contornos
        conts, _ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        #Ordenando los contornos de mayor a menor por área
        conts = sorted(conts, key=cv2.contourArea, reverse=True)[:1]
        #cv2.drawContours(ROI, conts, 0, (0,255,0), 1)
        
        for c in conts:

            #Centro del contorno
            M = cv2.moments(c)
            if M['m00'] == 0: M['m00'] == 1
            x = int(M['m10'] / M['m00'])
            y = int(M['m01'] / M['m00'])

            cv2.circle(ROI, (x,y), 5, (0,255,0), -1)

            #Punto más altos del contorno
            ymin = c.min(axis=1)
            cv2.circle(ROI, tuple(ymin[0]), 5, (0,130,255), -1)

            #Curva convexa
            curv = cv2.convexHull(c)
            cv2.drawContours(ROI, [curv], 0, (0,255,0), 2)

            #Defectos de convexidad (espacios entre los dedos)
            #Devuelve [punto inicial, ounto final, punto más alejado, distancia al punto mś alejado]
            dfct = cv2.convexHull(c, returnPoints=False)
            defects = cv2.convexityDefects(c, dfct)

            if defects is not None:

                inicio = []
                fin = []
                dedos = 

                for i in range(defects.shape[0]):
                    s,e,f,d = defects[i,0]
                    start = c[s][0]
                    end = c[e][0]
                    far = c[f][0]

                    #Angulo entre el punto inicial y el final
                    a = np.linalg(far-end)
                    b = np.linalg(far-start)
                    c = np.linalg(start-end)

                    angulo = np.arccos((np.power(a,2) + np.power(b,2) - np.power(c,2)) / (2*a*b))
                    angulo = np.degrees(angulo)
                    angulo = int(angulo)

                    #Ajustar estos parámetros
                    if np.linalg.norm(start-end) > 20 and d > 12000 and angulo < 90:

                        #Almacenando los puntos para contar los dedos
                        inicio.append(start)
                        fin.append(end)

                        cv2.circle(ROI, tuple(start), 5, (204,204,0), 2)
                        cv2.circle(ROI, tuple(end), 5, (204,0,204), 2)
                        cv2.circle(ROI, tuple(far), 7, (255,0,0), -1)

                        #cv2.putText(ROI, '{}'.format(d), tuple(far), 1, 1, (255,255,0), 1, cv2.LINE_AA)
                
                #Para 1 dedo
                if len(inicio) == 0:
                    minY = np.linalg.norm(ymin[0]-[x,y])
                    #Ajustar valor
                    if minY >= 110:
                        dedos += 1
                        cv2.putText(ROI, '{}'.format(dedos), tuple(ymin[0]), 1, 1, (0,255,255), 1, cv2.LINE_AA)
                
                #Para 2 o más dedos
                for i in range(len(inicio)):
                    dedos += 1
                    cv2.putText(ROI, '{}'.format(dedos), tuple(inicio[i]), 1, 1, (0,255,255), 1, cv2.LINE_AA)
                    #Para el últmo punto contado
                    if i == len(inicio)-1:
                        dedos += 1
                        cv2.putText(ROI, '{}'.format(dedos), tuple(fin[i]), 1, 1, (0,255,255), 1, cv2.LINE_AA)
                    
                cv2.putText(frame, '{}'.format(dedos), (390,45), 1, 4, (0,255,255), 2, cv2.LINE_AA)

    cv2.imshow('Frame', frame)
    
    k = cv2.waitKey(20)
    if k == ord('b'):
        bg = cv2.cvtColor(frameAux, cv2.COLOR_BGR2GRAY)
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
