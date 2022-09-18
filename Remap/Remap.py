import cv2
from scipy.interpolate import griddata
import numpy as np
from pathlib import Path

caminhoImagem = Path('Anexos, Imagens e Videos/PJing.png')

grid_x, grid_y = np.mgrid[0:149:150j, 0:149:150j]
destination = np.array([[0,0], [0,49], [0,99], [0,149],
                  [49,0],[49,49],[49,99],[49,149],
                  [99,0],[99,49],[99,99],[99,149],
                  [149,0],[149,49],[149,99],[149,149]])
source = np.array([[22,22], [24,68], [26,116], [25,162],
                  [64,19],[65,64],[65,114],[64,159],
                  [107,16],[108,62],[108,111],[107,157],
                  [151,11],[151,58],[151,107],[151,156]])

grid_z = griddata(destination, source, (grid_x, grid_y), method='cubic')
map_x = np.append([], [ar[:,1] for ar in grid_z]).reshape(150,150)
map_y = np.append([], [ar[:,0] for ar in grid_z]).reshape(150,150)
map_x_32 = map_x.astype('float32')
map_y_32 = map_y.astype('float32')

orig = cv2.imread(str(caminhoImagem))
warped = cv2.remap(orig, map_x_32, map_y_32, cv2.INTER_CUBIC)

#Mostra a imagem original
cv2.namedWindow('Imagem original', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Imagem original', orig)

#Mostra a imagem remapeada
cv2.namedWindow('Imagem remapeada', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Imagem remapeada', warped)

cv2.waitKey(0)