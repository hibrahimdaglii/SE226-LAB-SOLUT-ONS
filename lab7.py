import cv2

import numpy as np

path=r'C:\Users\ibrahim\Desktop\aykut.jpg'

img=cv2.imread(path)

orig=np.copy(img)

(b, g, r) = cv2.split(img)

cv2.imshow('image',img)

cv2.imshow("Red", r)

cv2.imshow("Green", g)

cv2.imshow("Blue", b)

for x in range(0, 100):

    for y in range(0, 200):

        b[x*4,y*2]= b[x,3]

        r[x*4,y*2] = r[x,y]

cv2.waitKey(0)

merged = cv2.merge([b, g, r])

cv2.imshow("Merged", merged)

cv2.waitKey(0)