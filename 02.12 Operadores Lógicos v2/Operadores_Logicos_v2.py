import cv2
import numpy
import sys
from pathlib import Path

path = Path(sys.path[0])
caminhoImagem = str(path.parent.absolute()) + '\\Anexos, Imagens e Videos\\'

#Carrega a imagem
original = cv2.imread(caminhoImagem + 'len_std.png')
cv2.namedWindow('Imagem original', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Imagem original', original)

#mascara
mascara = cv2.imread(caminhoImagem + 'len_mascara.png')
cv2.namedWindow('Imagem máscara', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Imagem máscara', mascara)

resultado = cv2.bitwise_and(original, mascara)
cv2.namedWindow('Máscara aplicada', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Máscara aplicada', resultado)

cv2.waitKey(0)
cv2.destroyAllWindows()