# imports
from PIL import Image, ImageEnhance
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Tucker\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# assigning an image from the source path
img = Image.open('''image_test\\test.png''')

# converts the image to result and saves it into result variable
result = pytesseract.image_to_string(img)

with open('text_result2.txt', mode ='w') as file:
 file.write(result)
 print("ready!")

