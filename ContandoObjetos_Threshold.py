import cv2

imagen = cv2.imread('/home/tavo/Imágenes/moneda.jpg')
imagen = cv2.resize(imagen, (400,400))
grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
_, th = cv2.threshold(grises, 228, 255, cv2.THRESH_BINARY_INV)

cont, _ = cv2.findContours(th, cv2.RETR_EXTERNAL\
    , cv2.CHAIN_APPROX_SIMPLE)

print('Cantidad de contornos: ', len(cont))

font = cv2.FONT_HERSHEY_SIMPLEX
i = 0

for c in cont:
    #Puntos centrales
    M = cv2.moments(c)
    if M['m00'] == 0: M['m00'] == 1
    x = int(M['m10'] / M['m00'])
    y = int(M['m01'] / M['m00'])

    mensaje = 'Obj: ' + str(i+1)
    cv2.putText(imagen, mensaje, (x-40,y), font, 0.75\
        , (255,0,0), 2, cv2.LINE_AA)
    
    cv2.drawContours(imagen, [c], 0, (255,0,0), 2)
    cv2.imshow('Imagen', imagen)
    i += 1

#cv2.imshow('Th', th)
cv2.waitKey(0)
cv2.destroyAllWindows()
