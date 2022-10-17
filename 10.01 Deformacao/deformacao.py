import cv2 as cv
import numpy as np
from pathlib import Path

img = cv.imread(str(Path('Deformacao/9ksVJ.jpg')))

right_eye = (215,105)
radius = 30
power = 1.6 # >1.0 for expansion, <1.0 for shrinkage

height, width, _ = img.shape
map_y = np.zeros((height,width),dtype=np.float32)
map_x = np.zeros((height,width),dtype=np.float32)

# create index map
for i in range(height):
    for j in range(width):
        map_y[i][j]=i
        map_x[i][j]=j

# deform around the right eye
for i in range (-radius, radius):
    for j in range(-radius, radius):
        if (i**2 + j**2 > radius ** 2):
            continue

        if i > 0:
            map_y[right_eye[1] + i][right_eye[0] + j] = right_eye[1] + (i/radius)**power * radius
        if i < 0:
            map_y[right_eye[1] + i][right_eye[0] + j] = right_eye[1] - (-i/radius)**power * radius
        if j > 0:
            map_x[right_eye[1] + i][right_eye[0] + j] = right_eye[0] + (j/radius)**power * radius
        if j < 0:
            map_x[right_eye[1] + i][right_eye[0] + j] = right_eye[0] - (-j/radius)**power * radius

warped=cv.remap(img,map_x,map_y,cv.INTER_LINEAR)
cv.imshow('Imagem Original', img)
cv.imshow('Imagem deformada', warped)
cv.waitKey()
