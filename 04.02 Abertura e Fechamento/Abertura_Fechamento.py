import cv2
from pathlib import Path

caminhoImagem = Path('Anexos, Imagens e Videos')

# Carrega a imagem
image1 = cv2.imread(str(caminhoImagem / 'exmorfologia1.png'))
image2 = cv2.imread(str(caminhoImagem / 'exmorfologia2.png'))

cv2.namedWindow("Imagem 1",cv2.WINDOW_GUI_EXPANDED)
cv2.imshow("Imagem 1",image1)

cv2.namedWindow("Imagem 2",cv2.WINDOW_GUI_EXPANDED)
cv2.imshow("Imagem 2",image2)

elem1 = cv2.getStructuringElement( cv2.MORPH_CROSS, ( 3, 3 ) ) # Elemento estruturante
elem2 = cv2.getStructuringElement( cv2.MORPH_RECT, ( 3, 1 ) ) # Elemento estruturante

abertura1 = cv2.morphologyEx(image1,cv2.MORPH_OPEN ,elem1)
fechamento1 = cv2.morphologyEx(image1,cv2.MORPH_CLOSE,elem2)

abertura2 = cv2.morphologyEx(image2,cv2.MORPH_OPEN ,elem1)
fechamento2 = cv2.morphologyEx(image2,cv2.MORPH_CLOSE,elem2)

cv2.namedWindow("Abertura imagem 1",cv2.WINDOW_GUI_EXPANDED)
cv2.imshow("Abertura imagem 1",abertura1)

cv2.namedWindow("Fechamento imagem 1",cv2.WINDOW_GUI_EXPANDED)
cv2.imshow("Fechamento imagem 1",fechamento1)

cv2.namedWindow("Abertura imagem 2",cv2.WINDOW_GUI_EXPANDED)
cv2.imshow("Abertura imagem 2",abertura2)

cv2.namedWindow("Fechamento imagem 2",cv2.WINDOW_GUI_EXPANDED)
cv2.imshow("Fechamento imagem 2",fechamento2)

cv2.waitKey(0)