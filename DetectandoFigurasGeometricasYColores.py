import cv2
import numpy as np

def selColor(im_hsv, color):

    #Colores
    rojoBajo1 = np.array([0,100,20], np.uint8)
    rojoAlto1 = np.array([8,255,255], np.uint8)

    rojoBajo2 = np.array([175,100,20], np.uint8)
    rojoAlto2 = np.array([179,255,255], np.uint8)

    naranjaBajo = np.array([11,100,20], np.uint8)
    naranjaAlto = np.array([19,255,255], np.uint8)

    amarilloBajo = np.array([20,100,20], np.uint8)
    amarilloAlto = np.array([32,255,255], np.uint8)

    verdeBajo = np.array([36,100,20], np.uint8)
    verdeAlto = np.array([70,255,255], np.uint8)

    moradoBajo = np.array([130,100,20], np.uint8)
    moradoAlto = np.array([145,255,255], np.uint8)

    rosaBajo = np.array([146,100,20], np.uint8)
    rosaAlto = np.array([170,255,255], np.uint8)

    #Máscaras
    maskRojo1 = cv2.inRange(im_hsv, rojoBajo1, rojoAlto1)
    maskRojo2 = cv2.inRange(im_hsv, rojoBajo2, rojoAlto2)
    maskRojo = cv2.add(maskRojo1, maskRojo2)

    maskNaranja = cv2.inRange(im_hsv, naranjaBajo, naranjaAlto)

    maskAmarillo = cv2.inRange(im_hsv, amarilloBajo, amarilloAlto)

    maskVerde = cv2.inRange(im_hsv, verdeBajo, verdeAlto)

    maskMorado = cv2.inRange(im_hsv, moradoBajo, moradoAlto)

    maskRosa = cv2.inRange(im_hsv, rosaBajo, rosaAlto)

    #Contornos
    contRojo = cv2.findContours(maskRojo, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    contNaranja = cv2.findContours(maskNaranja, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    contAmarillo = cv2.findContours(maskAmarillo, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    contVerde = cv2.findContours(maskVerde, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    contMorado = cv2.findContours(maskMorado, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    contRosa = cv2.findContours(maskRosa, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

    #Retornando el color
    if len(contRojo) > 0: color = 'Rojo'
    elif len(contNaranja) > 0: color = 'Naranja'
    elif len(contAmarillo) > 0: color = 'Amarillo'
    elif len(contVerde) > 0: color = 'Verde'
    elif len(contMorado) > 0: color = 'Morado'
    elif len(contRosa) > 0: color = 'Rosa'

    return color

def selFigura(contorno, width, height):
    epsilon = 0.01 * cv2.arcLength(contorno, True)
    approx = cv2.approxPolyDP(contorno, epsilon, True)
    lados = len(approx)

    if lados == 3:
        name = 'Triángulo'

    if lados == 4:
        aspec_ratio = float(width) / height

        if aspec_ratio > 0.95 and aspec_ratio < 1.05:
            name = 'Cuadrado'
        else:
            name = 'Rectangulo'

    if lados == 5:
        name = 'Pentagono'

    if lados == 6:
        name = 'Exagono'

    if lados > 10:
        name = 'Circulo'

    return name


img = cv2.imread('/home/tavo/Imágenes/figurasColores2.png')

cv2.imshow('img', img)

grises = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Imagen binarizada
canny = cv2.Canny(grises, 10, 150)
#Mejorando la imagen binaria (dilatación y erosión)
canny = cv2.dilate(canny, None, iterations=1)
canny = cv2.erode(canny, None, iterations=1)

#Contornos
conts, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#BGR to HSV
im_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

for c in conts:
    
    x,y,w,h = cv2.boundingRect(c)
    imAux = np.zeros(img.shape[:2], dtype='uint8')
    imAux = cv2.drawContours(imAux, [c], -1, 255, -1)
    maskHSV = cv2.bitwise_and(im_hsv, im_hsv, mask=imAux)
    name = selFigura(c,w,h)
    color = ''
    color = selColor(maskHSV, color)
    nameColor = name + ' ' + color
    cv2.putText(img, nameColor, (x,y-5), 1, 0.8, (0,255,0), 1)

    cv2.imshow('Imagen', img)
    cv2.waitKey(0)

cv2.destroyAllWindows()