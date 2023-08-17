import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from pathlib import Path

caminho = Path('Anexos, Imagens e Videos/coins.png')

# Load the image
img = cv.imread(str(caminho))
plt.imshow(img)
plt.show()

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold(gray,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
plt.imshow(thresh, cmap='gray')
plt.show()

kernel = np.ones((3,3),np.uint8)
closing = cv.morphologyEx(thresh,cv.MORPH_CLOSE, kernel, iterations = 1)

plt.imshow(closing, cmap='gray')
plt.show()

dist = cv.distanceTransform(closing, cv.DIST_L2, 3)

plt.imshow(dist, cmap='gray')   
plt.show()

ret, dist1 = cv.threshold(dist, 0.6*dist.max(), 255, 0)

markers = np.zeros(dist.shape, dtype=np.int32)
dist_8u = dist1.astype('uint8')
contours, _ = cv.findContours(dist_8u, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
for i in range(len(contours)):
    cv.drawContours(markers, contours, i, (i+1), -1)

markers = cv.circle(markers, (15,15), 5, len(contours)+1, -1)

markers = cv.watershed(img, markers)
img[markers == -1] = [0,0,255]

plt.imshow(markers)
plt.show()

cv.waitKey(0)



