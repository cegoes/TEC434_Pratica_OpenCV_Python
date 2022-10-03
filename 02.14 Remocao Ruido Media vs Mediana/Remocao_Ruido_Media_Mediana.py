import cv2
from pathlib import Path

caminhoImagem = Path('Anexos, Imagens e Videos')

#Carrega a imagem
imagem = cv2.imread(str(caminhoImagem / 'len_std_noise.png'))
cv2.namedWindow('Imagem original', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Imagem original', imagem)

#Filtro da mediana
filtromediana = cv2.medianBlur(imagem,3)
cv2.namedWindow('Imagem filtro mediana', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Imagem filtro mediana', filtromediana)

#Filtro da media
filtromedia = cv2.blur(imagem, (3,3))
cv2.namedWindow('Imagem filtro media', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Imagem filtro media', filtromedia)

cv2.waitKey(0)
cv2.destroyAllWindows()