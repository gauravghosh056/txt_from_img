import pytesseract
from PIL import Image


img = Image.open("health.PNG")
text = pytesseract.image_to_string(img)
print(text)


