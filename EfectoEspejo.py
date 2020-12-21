import cv2

cap = cv2.VideoCapture(0)

# 0 invierte horizontal
# 1 invierte vertical
# -1 invierte las 2

while True:
    ret, frame = cap.read()
    if not ret: break
    flip1 = cv2.flip(frame, 0)
    flip2 = cv2.flip(frame, 1)
    flip3 = cv2.flip(frame, -1)

    #cv2.imshow('Horizonta', flip1)
    #cv2.imshow('Vertical', flip2)
    #cv2.imshow('Horizontal y vertical', flip3)

    #Espejo
    anchoMitad = frame.shape[1] // 2
    frame[:,:anchoMitad] = cv2.flip(frame[:,anchoMitad:], 1)
    cv2.imshow('Flip', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()