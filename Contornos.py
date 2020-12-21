import cv2
import numpy as np

imagen = cv2.imread('/home/tavo/Imágenes/Toonify/Images/120854121_821183025289750_3255552354193723623_n.jpg')
gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
_, th = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

#Jerarquía 

#RETR_LIST -> todos los contornos
#RETR_EXTERNAL -> contornos externos
#RETR_CCOMP -> todos los contornos
#RETR_TREE -> todos los contornos

#(imagen binarizada,
# modo de recuperación de contorno,
# método de aproximación de contorno,
# desplazamiento del contorno)
contornos, hierarchy = cv2.findContours(th, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

#Contornos
print('Contornos ', len(contornos))
#Tamaño de 1 contorno
print('tamaño ', len(contornos[500]))

cv2.drawContours(imagen, contornos, 500, (0,255,0), 3)

cv2.imshow('Imagen', imagen)
cv2.imshow('Th', th)

cv2.waitKey(0)
cv2.destroyAllWindows()