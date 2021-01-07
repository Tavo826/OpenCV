import cv2

cap = cv2.VideoCapture('/home/tavo/Imágenes/vtest.avi')

#BackgroundSubstactorMOG: Segmentación de fondo en primer plano basado en una mezcla gaussiana
bgsMOG = cv2.bgsegm.createBackgroundSubtractorMOG()

#BackgroundSubstactorMOG2: Segmentación de fondo en primer plano basado en una mezcla gaussiana, permite una mayor adaptabilidad en diferentes escenas debido a cambios de iluminación
bgsMOG2 = cv2.createBackgroundSubtractorMOG2()

#BackgroundSubstractorGMG: combina la estimación estadística de la imagen de fondo y la segmentación bayesiana por pixel
bgsGMG = cv2.bgsegm.createBackgroundSubtractorGMG()
#Utiliza los primeros 120 fotogramas para el modelado del fondo

while True:
    ret, frame = cap.read()
    if ret == False: break

    #bgsMOG_mask = bgsMOG.apply(frame)
    #bgsMOG2_mask = bgsMOG2.apply(frame)
    bgsGMG_mask = bgsGMG.apply(frame)

    cv2.imshow('Frame', frame)
    #cv2.imshow('bgsMOG', bgsMOG_mask)
    #cv2.imshow('bgsMOG2', bgsMOG2_mask)
    cv2.imshow('bgsGMG', bgsGMG_mask)
    k = cv2.waitKey(30)
    if k == ord('q'): break

cap.release()
cv2.destroyAllWindows()