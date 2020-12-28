import cv2
import os
import numpy as np

def emotionImage(emocion):
    if emocion == 'Felicidad': image = cv2.imread('/home/tavo/Documentos/OpenCV/ReconocimientoFacial/Emociones/Emojis/felicidad.jpeg')
    if emocion == 'Enojo': image = cv2.imread('/home/tavo/Documentos/OpenCV/ReconocimientoFacial/Emociones/Emojis/enojo.jpeg')
    if emocion == 'Sorpresa': image = cv2.imread('/home/tavo/Documentos/OpenCV/ReconocimientoFacial/Emociones/Emojis/sorpresa.jpeg')
    if emocion == 'Tristeza': image = cv2.imread('/home/tavo/Documentos/OpenCV/ReconocimientoFacial/Emociones/Emojis/tristeza.jpeg')
    
    return image

dataPath = '/home/tavo/Documentos/OpenCV/ReconocimientoFacial/Emociones/Data'
imagePath = os.listdir(dataPath)

# METODOS
#metodo = 'EigenFaces'
#metodo = 'FisherFaces'
metodo = 'LBPH'

if metodo == 'EigenFaces': 
    emotion_recognizer = cv2.face.EigenFaceRecognizer_create()
    emotion_recognizer.read('/home/tavo/Documentos/OpenCV/ReconocimientoFacial/Emociones/modeloEigenFaces.xml')
if metodo == 'FisherFaces': 
    emotion_recognizer = cv2.face.FisherFaceRecognizer_create()
    emotion_recognizer.read('/home/tavo/Documentos/OpenCV/ReconocimientoFacial/Emociones/modeloFisherFaces.xml')
if metodo == 'LBPH': 
    emotion_recognizer = cv2.face.LBPHFaceRecognizer_create()
    emotion_recognizer.read('/home/tavo/Documentos/OpenCV/ReconocimientoFacial/Emociones/modeloLBPH.xml')


#Video test
#cap = cv2.VideoCapture('/home/tavo/Documentos/OpenCV/ReconocimientoFacial/Gustavo_3.mp4')
cap = cv2.VideoCapture(0)

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()
    if ret == False: break

    frame = cv2.flip(frame, 1)

    #Rotando frame
    #Mrot = cv2.getRotationMatrix2D((frame.shape[1]//2, frame.shape[0]//2), 90, 1)
    #frame = cv2.warpAffine(frame, Mrot, (frame.shape[1],frame.shape[0]))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = gray.copy()

    nFrame = cv2.hconcat([frame, np.zeros((480,300,3), dtype=np.uint8)])

    faces = faceClassif.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        rostro = auxFrame[y:y+h, x:x+w]
        rostro = cv2.resize(rostro, (150,150), interpolation=cv2.INTER_CUBIC)
        #Prediciendo etiqueta y confianza
        result = emotion_recognizer.predict(rostro)

        cv2.putText(frame, '{}'.format(result), (x,y-5), 1, 1.3, (255,255,0), 1, cv2.LINE_AA)
        cv2.putText(frame, '{}'.format(imagePath[result[0]]), (x,y-25), 2, 1.1, (0,255,0), 1, cv2.LINE_AA)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

        image = emotionImage(imagePath[result[0]])
        nFrame = cv2.hconcat([frame, image])

    cv2.imshow('Frame', nFrame)

    k = cv2.waitKey(10)
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()