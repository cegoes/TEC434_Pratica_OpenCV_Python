# Baseado na implementação desse trabalho:
# https://www.researchgate.net/publication/261340038_Global_thresholding_algorithm_based_on_boundary_selection

import cv2
from pathlib import Path

caminhoImagem = str(Path('Anexos, Imagens e Videos/Fig1041.tif'))

# carrega a imagem em escala de cinza
img = cv2.imread(caminhoImagem, 0)

# calcula o histograma da imagem
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

# determina o limite inicial
limiar = 128

# itera até que o limiar seja convergido
while True:
    # calcula as médias das intensidades dos pixels acima e abaixo do limite
    media_acima = sum([i * hist[i] for i in range(limiar, 256)]) / sum([hist[i] for i in range(limiar, 256)])
    media_abaixo = sum([i * hist[i] for i in range(0, limiar)]) / sum([hist[i] for i in range(0, limiar)])
    
    # calcula o novo limite como a média das médias acima e abaixo
    novo_limiar = int((media_acima + media_abaixo) / 2)
    
    # verifica se o limite convergiu
    if novo_limiar == limiar:
        break
    
    # atualiza o limite
    limiar = novo_limiar

# aplica a limiarização na imagem
thGTABBS = cv2.threshold(img, limiar, 255, cv2.THRESH_BINARY)[1]
thOTSU = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]

# exibe a imagem original e a imagem limiarizada
cv2.imshow('Imagem Original', img)
cv2.imshow('Imagem Limiarizada por OTSU', thOTSU)
cv2.imshow('Imagem Limiarizada por GTABBS', thGTABBS)

cv2.waitKey(0)
cv2.destroyAllWindows()
