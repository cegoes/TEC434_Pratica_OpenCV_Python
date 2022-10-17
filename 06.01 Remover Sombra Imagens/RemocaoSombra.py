import cv2 as cv
import numpy as np
from pathlib import Path

caminho = Path('Anexos, Imagens e Videos/VUwzK.jpg')

img = cv.imread(str(caminho), -1)

rgb_planes = cv.split(img)

result_planes = []
result_norm_planes = []
for plane in rgb_planes:
    dilated_img = cv.dilate(plane, np.ones((7,7), np.uint8))
    bg_img = cv.medianBlur(dilated_img, 21)
    diff_img = 255 - cv.absdiff(plane, bg_img)
    norm_img = cv.normalize(diff_img, None, alpha=0, beta=255, norm_type=cv.NORM_MINMAX, dtype=cv.CV_8UC1)
    result_planes.append(diff_img)
    result_norm_planes.append(norm_img)

result = cv.merge(result_planes)
result_norm = cv.merge(result_norm_planes)

cv.imshow('Original', img)
cv.imshow('Remocao Sombra', result)
cv.imshow('Remocao Sombra Normalizada', result_norm)
cv.waitKey()