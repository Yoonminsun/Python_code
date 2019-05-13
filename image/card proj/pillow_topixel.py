import PIL.Image as pilimg
from PIL import ImageFilter
import numpy as np

im = pilimg.open('card.png')
im.show()
cont_im = im.filter(ImageFilter.CONTOUR)
cont_im.show()
pix = np.array(im)
print(pix) # 437*626 >> pix[0]은 1열의 437행의 r,g,b 값들을 가진다

