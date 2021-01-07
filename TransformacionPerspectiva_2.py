import cv2
import numpy as np

def clics(event, x, y, flags, param):
    global puntos
    if event == cv2.EVENT_LBUTTONDOWN:
        puntos.append([x,y])

def dibujarPuntos(puntos):
    for x, y in puntos:
        cv2.circle(frame, (x,y), 5, (0,255,0), 2)

def uniendoPuntos(puntos):
    cv2.line(frame, tuple(puntos[0]), tuple(puntos[1]), (255,0,0), 1)
    cv2.line(frame, tuple(puntos[0]), tuple(puntos[2]), (255,0,0), 1)
    cv2.line(frame, tuple(puntos[2]), tuple(puntos[3]), (255,0,0), 1)
    cv2.line(frame, tuple(puntos[1]), tuple(puntos[3]), (255,0,0), 1)

puntos = []
cap = cv2.VideoCapture('/home/tavo/Imágenes/Video1.mp4')
cv2.namedWindow('frame')
cv2.setMouseCallback('frame', clics)

while True:
    ret, frame = cap.read()
    if ret == False: break

    dibujarPuntos(puntos)

    if len(puntos) == 4:
        uniendoPuntos([puntos])
        pts1 = np.float32([puntos])
        pts2 = np.float32([[0,0], [500,0], [0,300], [500,300]])

        M = cv2.getPerspectiveTransform(pts1, pts2)
        dst = cv2.warpPerspective(frame, M, (500,300))

        cv2.imshow('dst', dst)

    cv2.imshow('frame', frame)
    k = cv2.waitKey(30)
    if k == ord('n'): pruntos = []
    if k == ord('q'):break

cap.release()
cv2.destroyAllWindows()