import cv2

captura = cv2.VideoCapture('/home/tavo/Documentos/OpenCV/Videos/VideoReMakia.avi')

while (captura.isOpened()):
    ret, imagen = captura.read()
    if ret == True:
        cv2.imshow('Que Se Dice', imagen)
        #Se modifica la velocidad del video
        if cv2.waitKey(30) & 0xFF == ord('s'):
            break
    else: break

captura.release()
cv2.destroyAllWindows()