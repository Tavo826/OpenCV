import cv2
import os
import numpy as np

def obtenerModelo(metodo, facesData, labels):
    if metodo == 'EigenFaces': emotion_recognizer = cv2.face.EigenFaceRecognizer_create()
    if metodo == 'FisherFaces': emotion_recognizer = cv2.face.FisherFaceRecognizer_create()
    if metodo == 'LBPH': emotion_recognizer = cv2.face.LBPHFaceRecognizer_create()

    #Entrenando el reconocimiento
    print('entrenando ('+metodo+')...')
    emotion_recognizer.train(facesData, np.array(labels))

    #Almacenando el modelo
    emotion_recognizer.write('/home/tavo/Documentos/OpenCV/ReconocimientoFacial/Emociones/modelo'+metodo+'.xml')


dataPath = '/home/tavo/Documentos/OpenCV/ReconocimientoFacial/Emociones/Data'
emotionList = os.listdir(dataPath)

labels = []
facesData = []
label = 0

for nameDir in emotionList:
    #ruta del directorio
    emotionPath = dataPath + '/' + nameDir

    for fileName in os.listdir(emotionPath):
        #Leyendo las imágenes
        #Etiquetas
        labels.append(label)
        #Agregando las imágenes en escala de grises
        facesData.append(cv2.imread(emotionPath + '/' + fileName, 0))
    
    label = label + 1 #Gustavo -> 0, Juancho -> 1, ...

#cv2.destroyAllWindows()

obtenerModelo('EigenFaces', facesData, labels)
obtenerModelo('FisherFaces', facesData, labels)
obtenerModelo('LBPH', facesData, labels)