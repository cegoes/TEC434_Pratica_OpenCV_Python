import cv2
import numpy as np
from pathlib import Path

caminhoImagem = Path('Anexos, Imagens e Videos/tennis.png')

imagem = cv2.imread(str(caminhoImagem))

cv2.namedWindow('Imagem Entrada',cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Imagem Entrada', imagem)


p = np.float32([(356,218),(930,216),(1112,548),(158,552)])
q = np.float32([(0,0),(954,0),(954,2067),(0,2067)])

rot = cv2.getPerspectiveTransform(p,q)

result = cv2.warpPerspective(imagem, rot, (954,2067))

cv2.namedWindow('Perspectiva Corrigida',cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Perspectiva Corrigida', result)

cv2.waitKey(0)
