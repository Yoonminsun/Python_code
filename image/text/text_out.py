import cv2
import numpy as np
import pytesseract
from PIL import Image


def hangulFilePathImageRead(filePath):
    stream = open(filePath.encode("utf-8"), "rb")
    bytes = bytearray(stream.read())
    numpyArray = np.asarray(bytes, dtype=np.uint8)

    return cv2.imdecode(numpyArray, cv2.IMREAD_UNCHANGED)

# filepath = '공부하기싫다.jpg'
# filepath = hangulFilePathImageRead(filepath)

# filepath = cv2.cvtColor(filepath,cv2.COLOR_BGR2GRAY)
# ret, file_result = cv2.threshold(filepath,127,255,cv2.THRESH_BINARY)

# cv2.imshow('imageshow',filepath)
# cv2.imshow('imageshow',file_result)
# cv2.waitKey(0) # 이미지가 show 된 상태로 wait
# cv2.destroyAllWindows()
img = cv2.imread('toon3.jpg',cv2.THRESH_BINARY)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# img = Image.open('test.png')
# re_img = img.resize((1024,1024))
# re_img.save('toon2.jpg')
# re_img
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

print(pytesseract.image_to_string(img,lang='kor'))

