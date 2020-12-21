import cv2

imagen = cv2.imread('/home/tavo/Imágenes/moneda.jpg')
imagen = cv2.resize(imagen, (400,400))
grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

#Detectando bordes
#(imagen,
# umbral bajo, 
# umbral alto)
bordes = cv2.Canny(grises, 123, 225)

cont, _ = cv2.findContours(bordes, cv2.RETR_EXTERNAL\
    , cv2.CHAIN_APPROX_SIMPLE)

print('Contornos: ', len(cont))

cv2.drawContours(imagen, cont, -1, (0,0,255), 1)

cv2.imshow('Bordes', bordes)
cv2.imshow('Imagen', imagen)

cv2.waitKey(0)
cv2.destroyAllWindows()