import cv2 as cv
from pathlib import Path

caminhoImagem = Path('Anexos, Imagens e Videos/1280px-Hereditary_elliptocytosis.jpg')

imagem = cv.imread(str(caminhoImagem),cv.IMREAD_GRAYSCALE)

cv.namedWindow('Imagem carregada',cv.WINDOW_GUI_EXPANDED)
cv.imshow('Imagem carregada', imagem)

t_intervalo = cv.inRange(imagem,150,200)

cv.namedWindow('Threshold intervalo',cv.WINDOW_GUI_EXPANDED)
cv.imshow('Threshold intervalo', t_intervalo)

cv.waitKey()