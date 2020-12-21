import cv2

img = cv2.imread('/home/tavo/Imágenes/figurasColores.png')
#Imagen en escala de grises
grises = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Imagen binarizada por detección de bordes
canny = cv2.Canny(grises, 10, 150)
#Aplicando dilatación y erosión a la imagen 
#para corregir errores de dibujo
canny = cv2.dilate(canny, None, iterations=1)
canny = cv2.erode(canny, None, iterations=1)
#Encontrando los contornos
conts, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#Dibujando los contornos
for c in conts:
    #Curva: vector de entrada
    #epsilon: precisión de la aproximación
    #closed: indica si la curva es cerrada
    epsilon = 0.01 * cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, epsilon, True)

    #Cantidad de vértices
    lados = len(approx)

    x,y,w,h = cv2.boundingRect(approx)

    if lados == 3:
        cv2.putText(img, 'Triangulo', (x,y-5), 1, 1, (0,255,0), 1)
    
    if lados == 4:
        #Aspect Ratio = ancho/alto
        aspect_ratio = float(w) / h
        
        if aspect_ratio > 0.95 and aspect_ratio < 1.05:
            cv2.putText(img, 'Cuadrado', (x,y-5), 1, 1, (0,255,0), 1)
        else:
            cv2.putText(img, 'Rectangulo', (x,y-5), 1, 1, (0,255,0), 1)
    
    if lados == 5:
        cv2.putText(img, 'Pentagono', (x,y-5), 1, 1, (0,255,0), 1)

    if lados == 6:
        cv2.putText(img, 'Exagono', (x,y-5), 1, 1, (0,255,0), 1)

    if lados > 10:
        cv2.putText(img, 'Circulo', (x,y-5), 1, 1, (0,255,0), 1)


    cv2.drawContours(img, [approx], 0, (0,255,0), 2)
    cv2.imshow('Imagen', img)
    cv2.waitKey(0)

#cv2.imshow('Imagen', img)
#cv2.imshow('Canny', canny)

cv2.waitKey(0)
cv2.destroyAllWindows()