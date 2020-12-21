import cv2

imagen1 = cv2.imread('/home/tavo/Imágenes/636x460design_01 (79).jpg')
imagen2 = cv2.imread('/home/tavo/Imágenes/im1.jpeg')

img1 = cv2.resize(imagen1, (300,300))
img2 = cv2.resize(imagen2, (300,300))

#Adicionar
suma = cv2.add(img1, img2)

#Mostrando adición
print(img1[0:3, 0:3, 0])
print(img2[0:3, 0:3, 0])
print(suma[0:3, 0:3, 0])

#Sumando con transparencia
sumat = cv2.addWeighted(img1, 0.9, img2, 0.5, 0)

cv2.imshow('Suma', suma)
cv2.imshow('Suma Pesos', sumat)

#Restando
rest = cv2.subtract(img1, img2)

print(rest[0:3, 0:3, 0])

#Valor absoluto
rest_abs = cv2.absdiff(img1, img2)

print(rest_abs[0:3, 0:3, 0])

cv2.imshow('Resta', rest)
cv2.imshow('Resta Abs', rest_abs)

cv2.waitKey(0)
cv2.destroyAllWindows()