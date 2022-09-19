import cv2
import numpy as np
from pathlib import Path

caminho = Path('VUwzK.jpg')
img = cv2.imread(str(caminho), -1)

rgb_planes = cv2.split(img)

result_planes = []
result_norm_planes = []
for plane in rgb_planes:
    dilated_img = cv2.dilate(plane, np.ones((7,7), np.uint8))
    bg_img = cv2.medianBlur(dilated_img, 21)
    diff_img = 255 - cv2.absdiff(plane, bg_img)
    norm_img = cv2.normalize(diff_img, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
    result_planes.append(diff_img)
    result_norm_planes.append(norm_img)

result = cv2.merge(result_planes)
result_norm = cv2.merge(result_norm_planes)

cv2.imshow('Original', img)
cv2.imshow('Remoção Sombra', result)
cv2.imshow('Remoção Sombra Normalizada', result_norm)
cv2.waitKey()