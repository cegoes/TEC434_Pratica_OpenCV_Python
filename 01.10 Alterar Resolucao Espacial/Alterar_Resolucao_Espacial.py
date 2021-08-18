import cv2
import sys
from pathlib import Path

path = Path(sys.path[0])
caminhoImagem = str(path.parent.absolute()) + '\\Anexos, Imagens e Videos\\len_std.png'

imgEntrada = cv2.imread(caminhoImagem)

cv2.namedWindow('Imagem Entrada',cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Imagem Entrada', imgEntrada)

imgSaida = cv2.resize(imgEntrada, [64,64])

cv2.namedWindow('Imagem Saída',cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Imagem Saída', imgSaida)

cv2.waitKey(0)