import cv2
import os

or_path = '/home/tavo/Imágenes/Toonify/Images'

for path, _, files in os.walk(or_path):
    if path == '/home/tavo/Imágenes/Toonify/Images':
        for f in files:
            image = cv2.imread(or_path + '/' + f)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            inverted = 255- gray
            blurred = cv2.GaussianBlur(inverted, (21,21), 0)
            invertedBlurred = 255 - blurred
            finalImg = cv2.divide(gray, invertedBlurred, scale=256.0)

            final_path = '/home/tavo/Descargas/' + f
            cv2.imwrite(final_path, finalImg)
            cv2.imshow('File', finalImg)
            cv2.waitKey(0)
        
cv2.destroyAllWindows()