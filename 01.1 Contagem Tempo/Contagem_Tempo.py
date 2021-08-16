import cv2
import sys
from pathlib import Path

e1 = cv2.getTickCount()

path = Path(sys.path[0])
caminhoImagem = str(path.parent.absolute()) + '\\Anexos, Imagens e Videos\\a_vm1125.png'
imagem = cv2.imread(caminhoImagem)

e2 = cv2.getTickCount()
time = (e2 - e1)/ cv2.getTickFrequency()

cv2.namedWindow('Imagem carregada',cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Imagem carregada', imagem)

print('Tempo de carregamento: ' + str(time) + ' segundos')

cv2.waitKey(0)
