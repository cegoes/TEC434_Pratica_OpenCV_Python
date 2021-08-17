import cv2
import sys
from pathlib import Path

path = Path(sys.path[0])
caminhoImagem = str(path.parent.absolute()) + '\\Anexos, Imagens e Videos\\pecas_lego.jpg'

imagem = cv2.imread(caminhoImagem)

imagemtexto = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

cv2.imshow('Imagem carregada', imagem)
cv2.imshow('Imagem em tons de cinza', imagemtexto)

cv2.waitKey(0)
cv2.destroyAllWindows()