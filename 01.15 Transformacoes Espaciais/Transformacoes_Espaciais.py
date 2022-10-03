import cv2
import numpy
from pathlib import Path

caminhoImagem = Path('Anexos, Imagens e Videos/X_Wing.png')

#Carrega a imagem
image = cv2.imread(str(caminhoImagem))

#Mostra a imagem na janela
cv2.namedWindow("Imagem Original") # define a janela
cv2.imshow("Imagem Original", image)

#Diminui o tamanho pela metade
scale_percent = 50
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
tamanho = (width, height)

escala = cv2.resize(image, tamanho, cv2.INTER_LINEAR)
cv2.namedWindow("Imagem com Escala")
cv2.imshow("Imagem com Escala", escala)

'''
Translação deve ser em forma de matriz linear
    |1 0 Tx|
M = |0 1 Ty|
'''
rows, cols = image.shape[:2]
M = numpy.float32([[1,0,100],[0,1,50]])
translacao = cv2.warpAffine(image, M, (rows, cols))

cv2.namedWindow("Imagem com Translação")
cv2.imshow("Imagem com Translação", translacao)

pontopivo = (232,248)
angulo = 45

# Rotate the image using cv2.warpAffine()
M = cv2.getRotationMatrix2D(pontopivo, angulo, 1)
rotacao = cv2.warpAffine(image, M, (cols, rows))

cv2.namedWindow("Imagem com Rotação")
cv2.imshow("Imagem com Rotação", rotacao)

cv2.waitKey(0)