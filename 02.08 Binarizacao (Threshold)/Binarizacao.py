import cv2
from pathlib import Path

caminhoImagem = Path('Anexos, Imagens e Videos/len_std.png')

imagem = cv2.imread(str(caminhoImagem), cv2.IMREAD_GRAYSCALE)
ret, binarizada = cv2.threshold(imagem, 128, 255, cv2.THRESH_BINARY)

cv2.imshow('Imagem orignal', imagem)
cv2.imshow('Imagem binarizada', binarizada)

cv2.waitKey(0)
cv2.destroyAllWindows()