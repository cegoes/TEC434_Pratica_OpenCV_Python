import cv2
import sys
from pathlib import Path

path = Path(sys.path[0])
caminhoImagem = str(path.parent.absolute()) + '\\Anexos, Imagens e Videos\\len_std.png'

#Carrega a imagem
image = cv2.imread(caminhoImagem)
cv2.namedWindow('Imagem original', cv2.WINDOW_GUI_NORMAL)
cv2.imshow('Imagem original', image)

negativo = ~image

cv2.namedWindow('Imagem negativa', cv2.WINDOW_GUI_NORMAL)
cv2.imshow('Imagem negativa', negativo)

cv2.waitKey(0)
cv2.destroyAllWindows()