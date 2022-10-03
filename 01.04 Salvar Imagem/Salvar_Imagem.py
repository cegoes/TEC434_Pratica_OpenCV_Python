import cv2
from pathlib import Path

caminhoImagem = Path('Anexos, Imagens e Videos')

imagem = cv2.imread(str(caminhoImagem / 'len_std.png'))

# Copia a imagem para outra matriz
imageCopiada = imagem.copy()

cv2.imshow('Imagem carregada', imagem)

cv2.imwrite(str(caminhoImagem / 'len_std_salva.png'), imageCopiada)

cv2.waitKey(0)