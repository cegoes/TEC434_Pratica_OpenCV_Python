import cv2
from pathlib import Path

caminhoImagem = Path('Anexos, Imagens e Videos/pecas_lego.jpg')

#Carrega a imagem
image = cv2.imread(str(caminhoImagem))
cv2.namedWindow('Imagem original', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Imagem original', image)

imagemcanais = cv2.split(image)

cv2.namedWindow('Imagem canal blue(azul)', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Imagem canal blue(azul)', imagemcanais[0])

cv2.namedWindow('Imagem canal green(verde)', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Imagem canal green(verde)', imagemcanais[1])

cv2.namedWindow('Imagem canal red(vermelho)', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Imagem canal red(vermelho)', imagemcanais[2])

cv2.waitKey(0)
cv2.destroyAllWindows()