import cv2
import sys
from pathlib import Path

path = Path(sys.path[0])
caminhoImagem = str(path.parent.absolute()) + '\\Anexos, Imagens e Videos\\len_std.png'

print(caminhoImagem)
imagem = cv2.imread(caminhoImagem)

cv2.imshow('Imagem carregada', imagem)

cv2.waitKey(0)