import cv2
import sys
from pathlib import Path

path = Path(sys.path[0])
caminhoImagem = str(path.parent.absolute()) + '\\Anexos, Imagens e Videos\\'

#Carrega a imagem
image_a = cv2.imread(caminhoImagem + 'A.png')
cv2.namedWindow('Imagem original A', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Imagem original A', image_a)

#Carrega a imagem
image_b = cv2.imread(caminhoImagem + 'B.png')
cv2.namedWindow('Imagem original B', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Imagem original B', image_b)

res = cv2.bitwise_and(image_a,image_b)
cv2.imshow("A AND B",res)
res = cv2.bitwise_or(image_a,image_b)
cv2.imshow("A OR B",res)
res = cv2.bitwise_xor(image_a,image_b)
cv2.imshow("A XOR B",res)
res = cv2.bitwise_not(image_a)
cv2.imshow("NOT A",res)

cv2.waitKey(0)
cv2.destroyAllWindows()