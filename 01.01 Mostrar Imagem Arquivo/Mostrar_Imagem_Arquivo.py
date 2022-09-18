import cv2
from pathlib import Path

caminhoImagem = Path('Anexos, Imagens e Videos/len_std.png')
imagem = cv2.imread(str(caminhoImagem))

cv2.imshow('Imagem carregada', imagem)

cv2.waitKey(0)