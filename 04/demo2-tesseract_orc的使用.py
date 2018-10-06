import pytesseract
from PIL import Image

img = Image.open('authCode.png')
str1 = pytesseract.image_to_string(img)
print(str1)