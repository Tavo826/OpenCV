import cv2
import urllib.request
import numpy as np
import time
import imutils

url = 'http://192.168.1.57:8080/shot.jpg'

face_LBPH = cv2.face.LBPHFaceRecognizer_create()

face_LBPH.read('/home/tavo/Documentos/OpenCV/ReconocimientoFacial/Modelos/modeloLBPHFaces.xml')
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

while True:

    imgResp = urllib.request.urlopen(url)

    imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)

    img = cv2.imdecode(imgNp, -1)

    #Rotando
    Mrot = cv2.getRotationMatrix2D((img.shape[1]//2, img.shape[0]//2), 90, 1)
    frame = cv2.warpAffine(img, Mrot, (img.shape[1],img.shape[0]))
    #Escalando
    frame = imutils.resize(frame, width=640)
    frame = cv2.flip(frame, 1)
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = gray.copy()

    faces = faceClassif.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        rostro = auxFrame[y:y+h, x:x+w]
        rostro = cv2.resize(rostro, (150,150), interpolation=cv2.INTER_CUBIC)
        #Prediciendo etiqueta y confianza
        result_LBPH = face_LBPH.predict(rostro)

        cv2.putText(frame, '{}'.format(result_LBPH), (x,y-5), 1, 1.3, (255,255,0), 1, cv2.LINE_AA)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

    cv2.imshow('Beo el celuko', frame)
    time.sleep(0.1)

    k = cv2.waitKey(1)
    if k == ord('q'): break

cv2.destroyAllWindows()