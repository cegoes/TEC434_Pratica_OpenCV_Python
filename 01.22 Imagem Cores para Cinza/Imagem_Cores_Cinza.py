import cv2
from pathlib import Path

caminhoImagem = Path('Anexos, Imagens e Videos/pecas_lego.jpg')

imagem = cv2.imread(str(caminhoImagem))

imagemcinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

cv2.imshow('Imagem carregada', imagem)
cv2.imshow('Imagem em tons de cinza', imagemcinza)

cv2.waitKey(0)
cv2.destroyAllWindows()