import cv2
from pathlib import Path

caminhoImagem = Path('Anexos, Imagens e Videos/len_std.png')

imagem = cv2.imread(str(caminhoImagem))

cv2.namedWindow('Imagem Entrada',cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Imagem Entrada', imagem)

# Mostra o valor do pixel da posição (x,y) (20,30) da imagem
print(imagem[20,30])

# Insere um pixel verde na posição (x,y) (20,30) da imagem
imagem[20,30] = [255,255,255] # O opencv trabalha com a matriz de cores BGR(Blue,Green,Red) ao invés do RGB

# Mostra o novo valor do pixel da posição (x,y) (20,30) da imagem
print(imagem[20,30])

cv2.namedWindow('Imagem Pixel Manipulado',cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Imagem Pixel Manipulado', imagem)

cv2.waitKey(0)
