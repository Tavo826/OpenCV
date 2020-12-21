import cv2
import os

dataPath = '/home/tavo/Documentos/OpenCV/ReconocimientoFacial/Data'
imagePath = os.listdir(dataPath)

face_EigenFaces = cv2.face.EigenFaceRecognizer_create()
face_FisherFaces = cv2.face.FisherFaceRecognizer_create()
face_LBPH = cv2.face.LBPHFaceRecognizer_create()

#-----Leyendo el modelo------

#EigenFaces
face_EigenFaces.read('/home/tavo/Documentos/OpenCV/ReconocimientoFacial/Modelos/modeloEigenFaces.xml')

#FisherFaces
face_FisherFaces.read('/home/tavo/Documentos/OpenCV/ReconocimientoFacial/Modelos/modeloFisherFaces.xml')

#Local Binary Paterns Histograms (LBPH)

face_LBPH.read('/home/tavo/Documentos/OpenCV/ReconocimientoFacial/Modelos/modeloLBPHFaces.xml')

#Video test
#cap = cv2.VideoCapture('/home/tavo/Documentos/OpenCV/ReconocimientoFacial/Gustavo_3.mp4')
cap = cv2.VideoCapture(0)

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()
    if ret == False: break

    #Rotando frame
    #Mrot = cv2.getRotationMatrix2D((frame.shape[1]//2, frame.shape[0]//2), 90, 1)
    #frame = cv2.warpAffine(frame, Mrot, (frame.shape[1],frame.shape[0]))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = gray.copy()

    faces = faceClassif.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        rostro = auxFrame[y:y+h, x:x+w]
        rostro = cv2.resize(rostro, (150,150), interpolation=cv2.INTER_CUBIC)
        #Prediciendo etiqueta y confianza
        result_EigenFaces = face_EigenFaces.predict(rostro)
        result_FisherFaces = face_FisherFaces.predict(rostro)
        result_LBPH = face_LBPH.predict(rostro)

        cv2.putText(frame, '{}'.format(result_EigenFaces), (x,y-5), 1, 1.3, (255,255,0), 1, cv2.LINE_AA)
        cv2.putText(frame, '{}'.format(result_FisherFaces), (x,y+15), 1, 1.3, (255,255,0), 1, cv2.LINE_AA)
        cv2.putText(frame, '{}'.format(result_LBPH), (x,y+35), 1, 1.3, (255,255,0), 1, cv2.LINE_AA)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

    cv2.imshow('Frame', frame)

    k = cv2.waitKey(10)
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()