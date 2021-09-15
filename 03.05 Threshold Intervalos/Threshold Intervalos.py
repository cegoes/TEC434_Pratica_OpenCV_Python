import cv2 as cv
import sys
from pathlib import Path

path = Path(sys.path[0])
caminhoImagem = str(path.parent.absolute()) + '\\Anexos, Imagens e Videos\\1280px-Hereditary_elliptocytosis.jpg'

print(caminhoImagem)
imagem = cv.imread(caminhoImagem,cv.IMREAD_GRAYSCALE)

cv.namedWindow('Imagem carregada',cv.WINDOW_GUI_EXPANDED)
cv.imshow('Imagem carregada', imagem)

t_intervalo = cv.inRange(imagem,150,200)

cv.namedWindow('Threshold intervalo',cv.WINDOW_GUI_EXPANDED)
cv.imshow('Threshold intervalo', t_intervalo)

cv.waitKey(0)