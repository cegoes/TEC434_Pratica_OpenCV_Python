import cv2
from pathlib import Path

caminhoImagem = Path('Anexos, Imagens e Videos/len_std.png')

print(caminhoImagem)
imagem = cv2.imread(str(caminhoImagem))

cv2.namedWindow('Imagem carregadas', cv2.WINDOW_GUI_NORMAL)
cv2.imshow('Imagem carregadas', imagem)

cv2.waitKey(0)