import cv2
import sys
from pathlib import Path

path = Path(sys.path[0])
caminhoImagem = str(path.parent.absolute()) + '\\Anexos, Imagens e Videos\\len_std.png'

#Carrega a imagem
image = cv2.imread(caminhoImagem)
cv2.namedWindow('Imagem original', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Imagem original', image)

passabaixa = cv2.blur(image,(9,9))

cv2.namedWindow('Imagem passa baixa', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Imagem passa baixa', passabaixa)

cv2.waitKey(0)
cv2.destroyAllWindows()