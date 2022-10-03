import cv2
import numpy as np
from pathlib import Path

caminhoImagem = Path('Anexos, Imagens e Videos/len_std.png')

#Carrega a imagem
image = cv2.imread(str(caminhoImagem), cv2.IMREAD_GRAYSCALE)
cv2.namedWindow('Imagem original', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Imagem original', image)

# Apply identity kernel
kernelX = np.array([[-1,-1,-1],
                    [ 0, 0, 0],
                    [ 1, 1, 1]])

kernelY = np.array([[-1, 0, 1],
                    [-1, 0, 1],
                    [-1, 0, 1]])

prewittX = cv2.filter2D(image,ddepth=None,kernel=kernelX)
prewittY = cv2.filter2D(image,ddepth=None,kernel=kernelY)

prewittXY = cv2.add(prewittX, prewittX)

cv2.namedWindow('Imagem filtro Prewitt X', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Imagem filtro Prewitt X', prewittX)

cv2.namedWindow('Imagem filtro Prewitt Y', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Imagem filtro Prewitt Y', prewittY)

cv2.namedWindow('Imagem filtro Prewitt XY', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Imagem filtro Prewitt XY', prewittXY)

cv2.waitKey()
cv2.destroyAllWindows()