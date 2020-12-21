import cv2
import pytesseract

placa = []
image = cv2.imread('/home/tavo/Imágenes/auto001.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#Atenuando la imagen
gray = cv2.blur(gray, (3,3))
canny = cv2.Canny(image, 150, 200)
#Engrosando los contornos
canny = cv2.dilate(canny, None, iterations=1)

conts, _ = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

for c in conts:
    area = cv2.contourArea(c)
    epsilon = 0.09 * cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, epsilon, True)

    lados = len(approx)

    x,y,w,h = cv2.boundingRect(c)

    if lados == 4 and area > 1000: 
        #cv2.drawContours(image, [c], 0, (0,255,0), 2)
        aspect_ratio = float(w)/h
        
        if aspect_ratio > 3:
            placa = gray[y:y+h, x:x+w]
            text = pytesseract.image_to_string(placa, config='--psm 11')
            print('Text: ', text)
            cv2.imshow('Placa', placa)
            cv2.moveWindow('placa', 780, 10)
            cv2.rectangle(image, (x,y), (x+w,y+h), (0,255,0), 3)
            cv2.putText(image, text, (x-20,y-10), 1, 2.2, (0,255,0), 3)
            
cv2.imshow('Image', image)
cv2.moveWindow('Image', 45, 10)
cv2.waitKey(0)
cv2.destroyAllWindows()