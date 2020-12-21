import cv2
import numpy as np

#Se muestra en blanco
image = 255*np.ones((400, 600, 3), dtype=np.uint8)

#Dibujar una línea
#(Imagen,
# punto inicial,
# punto final,
# color de línea,
# grosor de línea)
cv2.line(image, (0,0), (600,400), (255,0,0), 4)

#Dibujar rectángulo
#(Imagen,
# punto inicial,
# punto final,
# color rectángulo,
# grosor líneas)
cv2.rectangle(image, (50,80), (200,200), (0,255,0), 2)

#Dibujar circulo
#(Imagen,
# punto cenral,
# radio,
# color,
# grosor (relleno -1))
cv2.circle(image, (300,200), 100, (255,25,0), -1)

#Texto
#(Imagen,
# texto,
# posición,
# fuente,
# tamaño,
# color,
# grosor,
# cv2.LINE_AA)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, 'Figuritas re makias', (50,30), font, 1, (0,0,0)\
            , 2, cv2.LINE_AA)

#Con diferentes fuentes
cv2.putText(image, 'Figuritas re makias', (50,60), 0, 1, (0,0,0)\
            , 2, cv2.LINE_AA)
cv2.putText(image, 'Figuritas re makias', (50,90), 1, 1, (0,0,0)\
            , 2, cv2.LINE_AA)
cv2.putText(image, 'Figuritas re makias', (50,120), 2, 1, (0,0,0)\
            , 2, cv2.LINE_AA)
cv2.putText(image, 'Figuritas re makias', (50,150), 3, 1, (0,0,0)\
            , 2, cv2.LINE_AA)
cv2.putText(image, 'Figuritas re makias', (50,180), 4, 1, (0,0,0)\
            , 2, cv2.LINE_AA)
cv2.putText(image, 'Figuritas re makias', (50,210), 5, 1, (0,0,0)\
            , 2, cv2.LINE_AA)
cv2.putText(image, 'Figuritas re makias', (50,240), 6, 1, (0,0,0)\
            , 2, cv2.LINE_AA)
cv2.putText(image, 'Figuritas re makias', (50,270), 7, 1, (0,0,0)\
            , 2, cv2.LINE_AA)

cv2.imshow('Imagen', image)
cv2.waitKey(0)
cv2.destroyAllWindows()