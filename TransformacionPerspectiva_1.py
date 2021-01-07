import cv2
import numpy as np

#Función para definir con clics las esquinas de la imagen
def clics(event, x, y, flags, param):
    global puntos
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(imagen, (x,y), 5, (0,255,0), 2)
        puntos.append([x,y])

def uniendopuntos(puntos):
    cv2.line(imagen, tuple(puntos[0]), tuple(puntos[1]), (255,0,0), 1)
    cv2.line(imagen, tuple(puntos[0]), tuple(puntos[2]), (255,0,0), 1)
    cv2.line(imagen, tuple(puntos[2]), tuple(puntos[3]), (255,0,0), 1)
    cv2.line(imagen, tuple(puntos[1]), tuple(puntos[3]), (255,0,0), 1)

puntos = []
imagen = cv2.imread('/home/tavo/Imágenes/gato.jpeg')
aux = imagen.copy()
cv2.namedWindow('Imagen')
cv2.setMouseCallback('Imagen', clics)

while True:

    if len(puntos) == 4:
        uniendopuntos(puntos)
        pts1 = np.float32([puntos])
        pts2 = np.float32([[0,0], [480,0], [0,300], [480,300]])

        M = cv2.getPerspectiveTransform(pts1, pts2)
        dst = cv2.warpPerspective(imagen, M, (480,300))

        cv2.imshow('dst', dst)

    cv2.imshow('Imagen', imagen)
    k = cv2.waitKey(1)
    if k == ord('n'): 
        imagen = aux.copy()
        puntos = []
    if k == ord('q'): break

cv2.destroyAllWindows()