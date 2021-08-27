import cv2
import sys
from pathlib import Path

path = Path(sys.path[0])
caminhoImagem = str(path.parent.absolute()) + '\\Anexos, Imagens e Videos\\pecas_lego.jpg'

imagem = cv2.imread(caminhoImagem, cv2.IMREAD_GRAYSCALE)

imagembordas = cv2.Canny(imagem, 30, 150)

cv2.imshow('Imagem carregada', imagem)
cv2.imshow('Imagem bordas detectadas', imagembordas)

cv2.waitKey(0)
cv2.destroyAllWindows()