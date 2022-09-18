import cv2
import numpy as np
from pathlib import Path

caminhoImagem = Path('Anexos, Imagens e Videos/regionfilling.png')

#Carrega a imagem
src = cv2.imread(str(caminhoImagem), cv2.IMREAD_GRAYSCALE)

res = cv2.findContours(src, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
contours =  res[-2] # for cv2 v3 and v4+ compatibility

cv2.namedWindow('Imagem original',cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Imagem original',src)

# Option 1: Using fillPoly
img_pl = np.zeros(src.shape)
cv2.fillPoly(img_pl, pts=contours,color=255)
cv2.namedWindow('Imagem fillPoly',cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Imagem fillPoly',img_pl)

# Option 2: Using drawContours
img_c = np.zeros(src.shape)
cv2.drawContours(img_c, contours, contourIdx=-1, color=255,thickness=-1)
cv2.namedWindow('Imagem drawContours',cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Imagem drawContours',img_pl)

cv2.waitKey(0)