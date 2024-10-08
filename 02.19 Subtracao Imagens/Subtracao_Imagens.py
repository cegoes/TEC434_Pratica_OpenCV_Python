import cv2
from pathlib import Path

caminhoImagem = Path('Anexos, Imagens e Videos')

#Carrega a imagem
frame1 = cv2.imread(str(caminhoImagem / 'Frame1.png'), cv2.IMREAD_GRAYSCALE)
cv2.namedWindow('Frame 1', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Frame 1', frame1)

#mascara
frame2 = cv2.imread(str(caminhoImagem / 'Frame2.png'), cv2.IMREAD_GRAYSCALE)
cv2.namedWindow('Frame 2', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Frame 2', frame2)

resultado = cv2.absdiff(frame1, frame2)
cv2.namedWindow('Subtração aplicada', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Subtração aplicada', resultado)

cv2.waitKey(0)
cv2.destroyAllWindows()