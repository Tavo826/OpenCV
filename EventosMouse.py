import cv2
import numpy as np

def dibujando(event, x, y, flags, param):

    global angulo, imagen_rotar

    print('------------------')
    print('Event: ', event)
    print('x: ', x)
    print('y: ', y)
    print('Flag: ', flags)
    print('Angulo: ', angulo)

    if event == cv2.EVENT_LBUTTONDOWN:
        #cv2.circle(image, (x,y), 20, (255,255,255), 2)
        angulo = angulo + 15
        M = cv2.getRotationMatrix2D((ancho//2, alto//2), angulo, 1)
        imagen_rotar = cv2.warpAffine(image, M, (ancho,alto))

    if event == cv2.EVENT_RBUTTONDOWN:
        #cv2.circle(image, (x,y), 20, (0,0,255), 2)
        angulo = angulo - 15
        M = cv2.getRotationMatrix2D((ancho//2, alto//2), angulo, 1)
        imagen_rotar = cv2.warpAffine(image, M, (ancho,alto))

    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(image, (x,y), 10, (255,0,0), -1)

    if event == cv2.EVENT_RBUTTONDBLCLK:
        cv2.circle(image, (x,y), 10, (0,255,0), -1)

    if event == cv2.EVENT_LBUTTONUP:
        cv2.putText(image, 'Ha dejado de presionar (Izquierdo)', (x,y), 2, 0.4, (255,255,0), 1, cv2.LINE_AA)

    if event == cv2.EVENT_RBUTTONUP:
        cv2.putText(image, 'Ha dejado de presionar (Derecho)', (x,y), 2, 0.4, (0,255,255), 1, cv2.LINE_AA)

#image = np.zeros((480,640,3), np.uint8)
image = cv2.imread('/home/tavo/Imágenes/224831_399119443457821_265864961_n.jpg')
imagen_rotar = image.copy()
ancho = image.shape[1]
alto = image.shape[0]
angulo = 0

cv2.namedWindow('Eventos')
cv2.setMouseCallback('Eventos', dibujando)

while True:
    cv2.imshow('Eventos', imagen_rotar)

    k = cv2.waitKey(1)
    if k == ord('l'):
        #image = np.zeros((480,640,3), np.uint8)
        image = cv2.imread('/home/tavo/Imágenes/224831_399119443457821_265864961_n.jpg')
    if k == ord('q'): break


cv2.destroyAllWindows()