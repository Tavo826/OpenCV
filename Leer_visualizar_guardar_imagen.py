import cv2

imagen = cv2.imread('/home/tavo/Imágenes/Captura de pantalla -2020-08-13 12-56-38.png', 0) #1 colores, 0 grises
cv2.imshow('Silas', imagen)
#Guardar imagen
cv2.imwrite('/home/tavo/Documentos/OpenCV/Images/Gris.jpg', imagen)
#Espera 1 segundo
#cv2.waitKey(1000)
#Espera que se presione una tecla
cv2.waitKey(0)
cv2.destroyAllWindows()