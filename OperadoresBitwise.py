import cv2
import numpy as np

img1 = np.zeros((400,600), dtype=np.uint8)
img1[100:300, 200:400] = 255
img2 = np.zeros((400,600), dtype=np.uint8)
img2 = cv2.circle(img2, (300,200), 125, (255), -1)

AND = cv2.bitwise_and(img1, img2)

OR = cv2.bitwise_or(img1, img2)

XOR = cv2.bitwise_xor(img1, img2)

NOT = cv2.bitwise_not(img1)

cv2.imshow('Img1', img1)
cv2.imshow('Img2', img2)
cv2.imshow('AND', AND)
cv2.imshow('OR', OR)
cv2.imshow('XOR', XOR)
cv2.imshow('NOT', NOT)

cv2.waitKey(0)
cv2.destroyAllWindows()

#Ver ciertas regiones de la imagen
cap = cv2.VideoCapture(0)
mask = np.zeros((480,640), dtype=np.uint8)
mask = cv2.circle(mask, (320,248), 125, (255), -1)

while True:
    ret, frame = cap.read()
    if ret:
        imgMask = cv2.bitwise_and(frame, frame, mask=mask)
        cv2.imshow('Video', imgMask)

        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
    else: break

cap.release
cv2.destroyAllWindows()