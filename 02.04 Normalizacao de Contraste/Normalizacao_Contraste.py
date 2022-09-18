import cv2
from pathlib import Path

caminhoImagem = Path('Anexos, Imagens e Videos/Fig0310(b).tif')

imagem = cv2.imread(str(caminhoImagem))

cv2.namedWindow('Imagem Original', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Imagem Original', imagem)

normalizado = cv2.normalize(imagem, None, 0, 255, cv2.NORM_MINMAX)

cv2.namedWindow('Contraste normalizado', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Contraste normalizado', normalizado)

cv2.waitKey(0)


