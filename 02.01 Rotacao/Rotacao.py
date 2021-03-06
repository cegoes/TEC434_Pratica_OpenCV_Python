import cv2
import sys
import numpy as np
from pathlib import Path

path = Path(sys.path[0])
caminhoImagem = str(path.parent.absolute()) + '\\Anexos, Imagens e Videos\\len_std.png'

imagem = cv2.imread(caminhoImagem)

rows,cols = imagem.shape[:2]
center = (rows/2, cols/2)

rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=45, scale=1)
translacao = cv2.warpAffine(imagem, rotate_matrix, (rows,cols))

cv2.imshow('Imagem original', imagem)
cv2.imshow('Imagem rotação', translacao)

cv2.waitKey(0)