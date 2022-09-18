import cv2
from pathlib import Path

caminhoImagem = Path('Anexos, Imagens e Videos/pecas_lego.jpg')

imagem = cv2.imread(str(caminhoImagem), cv2.IMREAD_GRAYSCALE)

imagembordas = cv2.Canny(imagem, 30, 150)

cv2.imshow('Imagem carregada', imagem)
cv2.imshow('Imagem bordas detectadas', imagembordas)

cv2.waitKey(0)
cv2.destroyAllWindows()