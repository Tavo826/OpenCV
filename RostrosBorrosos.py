import cv2

def nothing(val):
    pass

#Para una imagen
img = cv2.imread('/home/tavo/Imágenes/Toonify/Images/20190420_221414.jpg')
faceClassif = cv2.CascadeClassifier('/home/tavo/.virtualenvs/Yolo/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml')
cv2.namedWindow('Imagen')

#(nombre de la barra,
# nombre de la ventana,
# valor del slider,
# pocisión máxima del slider,
# puntero a una función)
cv2.createTrackbar('Borroso', 'Imagen', 0, 15, nothing)
cv2.createTrackbar('Gris', 'Imagen', 0, 1, nothing)

while True:

#   (nombre de la barra,
#   nombre de la ventana)
    valBorroso = cv2.getTrackbarPos('Borroso', 'Imagen')
    valGris = cv2.getTrackbarPos('Gris', 'Imagen')

    if valGris == 1:
        imagen = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY)
    else: imagen = img.copy()

    faces = faceClassif.detectMultiScale(img\
    , scaleFactor = 1.1\
    , minNeighbors = 5\
    , minSize = (60,60)\
    , maxSize = (200,200))

    for (x,y,w,h) in faces:
        if valBorroso > 0:
            imagen[y:y+h, x:x+w] = cv2.blur(imagen[y:y+h, x:x+w], (valBorroso,valBorroso))

    cv2.imshow('Imagen', imagen)
    k = cv2.waitKey(1)
    if k == 27:
        break

cv2.destroyAllWindows()