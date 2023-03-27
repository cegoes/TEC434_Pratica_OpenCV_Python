import cv2 as cv
import numpy as np
from pathlib import Path

caminhoImagens = Path("09.08 Mario Coin")
img = cv.imread(str(caminhoImagens / 'res_mario.jpg'))
img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
template = cv.imread(str(caminhoImagens / 'coin.jpg'),cv.IMREAD_GRAYSCALE)
w, h = template.shape[::-1]
res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
img_rgb = img.copy()

for pt in zip(*loc[::-1]):
    cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

cv.imshow('Mario',img)
cv.imshow('Mario Moedas',img_rgb)
cv.waitKey()