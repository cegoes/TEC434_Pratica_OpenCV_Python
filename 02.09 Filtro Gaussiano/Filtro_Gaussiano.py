import cv2
from pathlib import Path

caminhoImagem = Path('Anexos, Imagens e Videos/len_std.png')

#Carrega a imagem
image = cv2.imread(str(caminhoImagem))
cv2.namedWindow('Imagem original', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Imagem original', image)

imagemFiltrada = cv2.GaussianBlur(image,(9,9),0)

cv2.namedWindow('Imagem Filtro Gaussiano', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Imagem Filtro Gaussiano', imagemFiltrada)

cv2.waitKey(0)
cv2.destroyAllWindows()