import cv2
from pathlib import Path

caminhoImagem = Path('Anexos, Imagens e Videos/pecas_lego.jpg')

imagem = cv2.imread(str(caminhoImagem), cv2.IMREAD_GRAYSCALE)

cv2.imshow('Imagem carregada', imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()