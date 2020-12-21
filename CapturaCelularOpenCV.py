import urllib.request
import cv2
import numpy as np
import time

url = 'http://192.168.1.57:8080/shot.jpg'

while True:

    imgResp = urllib.request.urlopen(url)

    imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)

    img = cv2.imdecode(imgNp, -1)

    cv2.imshow('Beo el celuko', img)

    time.sleep(0.1)

    tecla = cv2.waitKey(25) & 0xFF

    if tecla == 27:
        break

cv2.destroyAllWindows()
