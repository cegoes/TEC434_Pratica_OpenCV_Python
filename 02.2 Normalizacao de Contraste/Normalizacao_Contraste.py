import cv2
import sys
import numpy
from pathlib import Path

path = Path(sys.path[0])
caminhoImagem = str(path.parent.absolute()) + '\\Anexos, Imagens e Videos\\Fig0310(b).tif'

imagem = cv2.imread(caminhoImagem)

cv2.namedWindow('Imagem Original', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Imagem Original', imagem)

normalizado = cv2.normalize(imagem, None, 0, 255, cv2.NORM_MINMAX)

cv2.namedWindow('Contraste normalizado', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Contraste normalizado', normalizado)

cv2.waitKey(0)


