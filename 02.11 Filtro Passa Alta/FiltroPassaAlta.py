import cv2
import numpy as np
from pathlib import Path

caminhoImagem = Path('Anexos, Imagens e Videos/len_std.png')

#Carrega a imagem
image = cv2.imread(str(caminhoImagem))
cv2.namedWindow('Imagem original', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Imagem original', image)

# Apply identity kernel
kernel1 = np.array([[-1, -1, -1],
                    [-1,  8, -1],
                    [-1, -1, -1]])

passaalta = cv2.filter2D(image,ddepth=None,kernel=kernel1)

cv2.namedWindow('Imagem filtro passa-alta', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Imagem filtro passa-alta', passaalta)

cv2.waitKey(0)
cv2.destroyAllWindows()