'''
Se leen las imágenes y se generan las etiquetas
posteriormente se entrenan los modelos de reconocimiento
'''

import cv2
import os
import numpy as np

dataPath = '/home/tavo/Documentos/OpenCV/ReconocimientoFacial/Data'
peopleList = os.listdir(dataPath)

labels = []
facesData = []
label = 0

for nameDir in peopleList:
    #ruta del directorio
    personPath = dataPath + '/' + nameDir

    for fileName in os.listdir(personPath):
        #Leyendo las imágenes
        #Etiquetas
        labels.append(label)
        #Agregando las imágenes en escala de grises
        facesData.append(cv2.imread(personPath + '/' + fileName, 0))

        #image = cv2.imread(personPath + '/' + fileName, 0)
        #cv2.imshow('Image', image)
        #cv2.waitKey(10)
    
    label = label + 1 #Gustavo -> 0, Juancho -> 1, ...

#cv2.destroyAllWindows()

print('Numero de elementos: ', len(labels))
print('Etiquetas 0: ', np.count_nonzero(np.array(labels) == 0))
print('Etiquetas 1: ', np.count_nonzero(np.array(labels) == 1))

#------ MODELOS ----------

#EigenFaces

#(Las imágenes deben estar en escala de grises
# Las imágenes deben tener el mismo tamaño)

face_EigenFaces = cv2.face.EigenFaceRecognizer_create()

print("Entrenando EigenFaces...")
face_EigenFaces.train(facesData, np.array(labels))
face_EigenFaces.write('/home/tavo/Documentos/OpenCV/ReconocimientoFacial/Modelos/modeloEigenFaces.xml')
print('Modelo almacenado')

#FisherFaces

#(Las imágenes deben estar en escala de grises
# Las imágenes deben tener el mismo tamaño)

face_FisherFaces = cv2.face.FisherFaceRecognizer_create()

print("Entrenando FisherFaces...")
face_FisherFaces.train(facesData, np.array(labels))
face_FisherFaces.write('/home/tavo/Documentos/OpenCV/ReconocimientoFacial/Modelos/modeloFisherFaces.xml')
print('Modelo almacenado')

#Local Binary Paterns Histograms (LBPH)

#(Las imágenes deben estar en escala de grises)

face_LBPHFaces = cv2.face.LBPHFaceRecognizer_create()

print("Entrenando LBPHFaces...")
face_LBPHFaces.train(facesData, np.array(labels))
face_LBPHFaces.write('/home/tavo/Documentos/OpenCV/ReconocimientoFacial/Modelos/modeloLBPHFaces.xml')
print('Modelo almacenado')