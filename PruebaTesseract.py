import cv2
import pytesseract

#pytesseract.pytesseract.tesseract_cmd = r'<>'

image = cv2.imread('/home/tavo/Imágenes/maxresdefault.jpg')

text = pytesseract.image_to_string(image)
print('Text', text)

cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()