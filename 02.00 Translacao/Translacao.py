import cv2
import numpy as np
from pathlib import Path

caminhoImagem = Path('Anexos, Imagens e Videos/len_std.png')

imagem = cv2.imread(str(caminhoImagem))

rows,cols = imagem.shape[:2]

trans = np.float32([[1, 0, 15], [0, 1, 25]])
translacao = cv2.warpAffine(imagem, trans, (rows,cols))

cv2.imshow('Imagem original', imagem)
cv2.imshow('Imagem translacao', translacao)

cv2.waitKey(0)