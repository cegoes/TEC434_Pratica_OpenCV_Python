import cv2
from pathlib import Path

caminhoImagem = Path('Anexos, Imagens e Videos/len_std.png')

#Carrega a imagem
image = cv2.imread(str(caminhoImagem))
cv2.namedWindow('Imagem original', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Imagem original', image)

filtromediana = cv2.medianBlur(image,3)

cv2.namedWindow('Imagem filtro mediana', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Imagem filtro mediana', filtromediana)

cv2.waitKey(0)
cv2.destroyAllWindows()