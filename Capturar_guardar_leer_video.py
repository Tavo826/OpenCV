import cv2

captura = cv2.VideoCapture(0)#No de la cámara
#Guardar video (nombre, code video, rate frame (im/seg), tamaño img)
salida = cv2.VideoWriter('/home/tavo/Documentos/OpenCV/Videos/VideoReMakia.avi', cv2.VideoWriter_fourcc(*'XVID'), 20.0, (640, 480))

while(captura.isOpened()):
    ret, imagen = captura.read()

    if ret == True: #Se tiene una imagen
        cv2.imshow('Video re makia', imagen)
        salida.write(imagen)
        #Espera que se oprima una tecla
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break

#Finaliza la captura
captura.release()
salida.release()
cv2.destroyAllWindows()

