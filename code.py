import cv2
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread('C:/Users/harsh/OneDrive/Pictures/manuscript/manuscript2.png', 0)

text = pytesseract.image_to_string(img)
print(text)
