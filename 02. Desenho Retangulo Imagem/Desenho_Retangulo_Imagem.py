import cv2
import sys
from pathlib import Path

path = Path(sys.path[0])
caminhoImagem = str(path.parent.absolute()) + '\\Anexos, Imagens e Videos\\len_std.png'

imagem = cv2.imread(caminhoImagem)

imagemdesenho = imagem.copy()
cv2.rectangle(imagemdesenho,(106,98),(185,194),(0,0,255),2)
cv2.imshow('Imagem carregada', imagem)
cv2.imshow('Imagem desenho', imagemdesenho)

cv2.waitKey(0)
cv2.destroyAllWindows()