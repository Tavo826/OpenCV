import cv2
import numpy as np

#BGR
bgr = np.zeros((300,300,3), dtype=np.uint8)
bgr[:,:,:] = [255,0,0] #Imagen BGR
cv2.imshow('BGR', bgr)
cv2.waitKey(0)

#BGR a RGB
img_bgr = cv2.imread('/home/tavo/Imágenes/636x460design_01 (79).jpg')
c1 = img_bgr[:,:,0]
c2 = img_bgr[:,:,1]
c3 = img_bgr[:,:,2]
cv2.imshow('BGR', np.hstack([c1,c2,c3]))

img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
c1 = img_rgb[:,:,0]
c2 = img_rgb[:,:,1]
c3 = img_rgb[:,:,2]
cv2.imshow('RGB', np.hstack([c1,c2,c3]))

#Escala de grises
gris = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gris', gris)

cv2.waitKey(0)
cv2.destroyAllWindows()