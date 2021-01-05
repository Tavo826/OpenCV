import cv2
import imutils

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret == False: break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    _, th = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

    gray = imutils.resize(gray, height=frame.shape[0]//2)
    th = imutils.resize(th, height=frame.shape[0]//2)

    concat_v = cv2.vconcat([gray, th])
    concat = cv2.hconcat([frame, concat_v])

    cv2.putText(concat, 'Video Streaming', (10,20), 1, 1.5, (0,255,0), 2)
    cv2.putText(concat, 'Escala de grises', (650,20), 1, 1.5, (0,255,0), 2)
    cv2.putText(concat, 'Binarizada', (650,260), 1, 1.5, (0,255,0), 2)

    #cv2.imshow('Frame', frame)
    #cv2.imshow('Gray', gray)
    #cv2.imshow('Th', th)
    cv2.imshow('Concat', concat)

    k = cv2.waitKey(1)
    if k == ord('q'): break

cap.release()
cv2.destroyAllWindows()
