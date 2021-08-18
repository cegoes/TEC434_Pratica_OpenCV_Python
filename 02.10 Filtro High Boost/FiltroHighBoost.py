import cv2
import numpy as np
import sys
from pathlib import Path

path = Path(sys.path[0])
caminhoImagem = str(path.parent.absolute()) + '\\Anexos, Imagens e Videos\\len_std.png'

#Carrega a imagem
image = cv2.imread(caminhoImagem)
cv2.namedWindow('Imagem original', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Imagem original', image)

# Apply identity kernel
kernel1 = np.array([[-1, -1, -1], 
                    [-1,  8, -1], 
                    [-1, -1, -1]])
passaalta1 = cv2.filter2D(image,ddepth=None,kernel=kernel1)
highboost1 = cv2.add(image,passaalta1)

cv2.namedWindow('Imagem filtro high boost (a)', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Imagem filtro high boost (a)', highboost1)

# Apply identity kernel
kernel2 = np.array([[0, -1, 0],
                    [-1, 4, -1],
                    [0, -1, 0]])
passaalta2 = cv2.filter2D(image,ddepth=None,kernel=kernel2)
highboost2 = cv2.add(image,passaalta2)

cv2.namedWindow('Imagem filtro high boost (b)', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Imagem filtro high boost (b)', highboost2)

cv2.waitKey(0)
cv2.destroyAllWindows()