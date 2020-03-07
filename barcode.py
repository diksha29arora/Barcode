import numpy as np
import cv2 as cv

img = np.random.randint(0,2,(1,256))*255.
img = cv.resize(img, (256,50))

cv.imwrite("BarCode.png",img)