# HAAR CASCADE

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
faceClassif = cv2.CascadeClassifier('/home/tavo/.virtualenvs/Yolo/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml')

img = cv2.imread('/home/tavo/Imágenes/Toonify/Images/20190420_221414.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceClassif.detectMultiScale(gray\
    , scaleFactor = 1.1\
    , minNeighbors = 5\
    , minSize = (60,60)\
    , maxSize = (200,200))

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

cv2.imshow('Img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

while True:
    ret, frame = cap.read()
    if not ret: break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceClassif.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)

    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()