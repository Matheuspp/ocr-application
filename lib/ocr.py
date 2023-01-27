import pytesseract
from PIL import Image
import re
import numpy as np

# read the image
#img = cv2.imread('img.png')
img = np.array(Image.open("images.jpeg"))

# run tesseract OCR on image
text = pytesseract.image_to_string(img, lang='eng', 
                                   config='--psm 11')
text = re.sub(r'\s+', '', text)
print(text)
