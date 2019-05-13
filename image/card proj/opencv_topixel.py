import numpy as np
import cv2
img = cv2.imread('zero.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('imageshow',img)
cv2.waitKey(0) # 이미지가 show 된 상태로 wait
cv2.destroyAllWindows()

# pixel = []

# h,w = img.shape
# for y in range(0,h):
#     for x in range(0,w):
#         # grayscale 인 경우
#         pixel.append(img.item(y,x))
#         # rgb 인 경우
#         # r = img.item(y,x,2)
#         # g = img.item(y,x,1)
#         # b = img.item(y,x,0)
#         # pixel.append([r,g,b])
#
# print(pixel)

orb = cv2.ORB_create()
