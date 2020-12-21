import cv2

cap = cv2.VideoCapture(0)

faceClassif = faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
count = 0

while True:
    ret, frame = cap.read()

    if not ret: break

    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = frame.copy()

    faces = faceClassif.detectMultiScale(gray, 1.3, 5)

    k = cv2.waitKey(1)
    if k == ord('q'):
        break

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (128,0,255), 2)
        rostro = auxFrame[y:y+h,x:x+w]
        rostro = cv2.resize(rostro, (150,150), interpolation=cv2.INTER_CUBIC)
        if k == ord('s'):
            cv2.imwrite('/home/tavo/Imágenes/Rostros/Rostro_{}.jpg'.format(count), rostro)
            cv2.imshow('Rostro', rostro)
            count += 1
        
    cv2.imshow('Frame', frame)

cap.release()
cv2.destroyAllWindows()