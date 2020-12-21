'''
Se leen los videos y se obtienen las imágenes 
para luego entrenarlas en "EntrenandoRF.py"
'''

import cv2
import os
import imutils

videoName = 'Gustavo'
#videoName = 'Juancho'
dataPath = '/home/tavo/Documentos/OpenCV/ReconocimientoFacial/Data'
videoPath = dataPath + '/' + videoName

if not os.path.exists(videoPath):
    os.makedirs(videoPath)

cap = cv2.VideoCapture('/home/tavo/Documentos/OpenCV/ReconocimientoFacial/Gustavo_1.mp4')
cap = cv2.VideoCapture('/home/tavo/Documentos/OpenCV/ReconocimientoFacial/Juancho.mp4')

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
count = 0

while True:
    
    ret, frame = cap.read()
    if ret == False: break

    #Rotando
    Mrot = cv2.getRotationMatrix2D((frame.shape[1]//2, frame.shape[0]//2), 90, 1)
    frame = cv2.warpAffine(frame, Mrot, (frame.shape[1],frame.shape[0]))
    #Escalando
    frame = imutils.resize(frame, width=640)
    
    auxFrame = frame.copy()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = faceClassif.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
        rostro = auxFrame[y:y+h,x:x+w]
        rostro = cv2.resize(rostro, (150,150), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(videoPath + '/rostro_{}.jpg'.format(count), rostro)
        count += 1

    cv2.imshow('Frame', frame)

    k = cv2.waitKey(1)
    if k == ord('q') or count >= 415:
        break

cap.release()
cv2.destroyAllWindows()