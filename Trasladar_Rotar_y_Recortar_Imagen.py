import cv2
import numpy as np
import imutils

image = cv2.imread('/home/tavo/Imágenes/636x460design_01 (79).jpg')

ancho = image.shape[1]
alto = image.shape[0]

#Trasladando imagen
#Matriz de traslación
Mtras = np.float32([[1,0,10],[0,1,100]])
#(imagen
# matriz de transformación,
# tamaño imagen de salida)
imTras = cv2.warpAffine(image, Mtras, (ancho-200,alto-100))

#Rotar imagen
#Matriz de rotación
#(centro de rotación
# angulo de rotación, grados
# escala isotrópica)
Mrot = cv2.getRotationMatrix2D((ancho//2, alto//2), 15, 1)
imRot = cv2.warpAffine(image, Mrot, (ancho,alto))

#Escalar imagen
#(imagen
# ancho,alto de la nueva imagen
# método de interpolación)
imEsc = cv2.resize(image, (ancho//2,alto//2), interpolation=cv2.INTER_CUBIC)

#Escalar imagen con aspect ratio
imEscAR = imutils.resize(image, width=500)

print(image.shape)
#Recortar imagen
imRec = image[115:250, 460:585]


cv2.imshow('Imagen', image)
#cv2.imshow('Imagen trasladada', imTras)
cv2.imshow('Imagen rotada', imRot)
#cv2.imshow('Imagen escalada', imEsc)
#cv2.imshow('Imagen escalada aspect ratio', imEscAR)
#cv2.imshow('Imagen recortada', imRec)
cv2.waitKey(0)
cv2.destroyAllWindows()