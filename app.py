from fastapi import FastAPI, File, UploadFile, Request
import uvicorn
#from mangum import Mangum
import numpy as np
import pytesseract
from PIL import Image
import re


app = FastAPI()
#handler = Mangum(app)
@app.post("/home/")
def home():
    return {"Welcome": "this is an experimental test"}
    
@app.post('/')
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    nparr = np.fromstring(contents, np.uint8)
    img = Image.frombytes('L', (28, 28), nparr.tostring())
    #img = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)
    img = np.array(img)   
    text = pytesseract.image_to_string(img, lang='eng', 
                                   config='--psm 11')
    #text = re.sub(r'\s+', '', text)

    return {"ocr": text}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)

