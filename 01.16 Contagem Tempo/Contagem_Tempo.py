import cv2
from pathlib import Path

e1 = cv2.getTickCount()

caminhoImagem = Path('Anexos, Imagens e Videos/a_vm1125.png')
imagem = cv2.imread(str(caminhoImagem))

e2 = cv2.getTickCount()

time = (e2 - e1) / cv2.getTickFrequency()

cv2.namedWindow('Imagem carregada',cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Imagem carregada', imagem)

print('Tempo de carregamento: ' + str(time) + ' segundos')

cv2.waitKey(0)
cv2.destroyAllWindows()