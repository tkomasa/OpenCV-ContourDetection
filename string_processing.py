# imports
from PIL import Image, ImageEnhance
import pytesseract

# assigning an image from the source path
img = Image.open('''image_test\\pytest.png''')

# adding some sharpness and contrast to the image
enhancer1 = ImageEnhance.Sharpness(img)
enhancer2 = ImageEnhance.Contrast(img)
img_edit = enhancer1.enhance(20.0)
img_edit = enhancer2.enhance(1.5)

# save the new image
img_edit.save("imeage_test\\edited_image.png")

# converts the image to result and saves it into result variable
result = pytesseract.image_to_string(img_edit)
with open('text_result2.txt', mode='w') as file:
    file.write(result)
    print("File ready.")
