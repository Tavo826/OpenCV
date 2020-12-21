import cv2
import os
import imutils

#emotionName = 'Enojo'
#emotionName = 'Felicidad'
#emotionName = 'Sorpresa'
emotionName = 'Tristeza'
dataPath = '//home/tavo/Documentos/OpenCV/ReconocimientoFacial/Emociones/Data'
videoPath = dataPath + '/' + emotionName

if not os.path.exists(videoPath):
    os.makedirs(videoPath)

cap = cv2.VideoCapture(0)

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
count = 0

while True:
    
    ret, frame = cap.read()
    if ret == False: break
    
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
    if k == ord('q') or count >= 200:
        break

cap.release()
cv2.destroyAllWindows()