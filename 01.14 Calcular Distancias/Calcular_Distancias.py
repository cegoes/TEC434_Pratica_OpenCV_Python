import scipy.spatial.distance as dist
import cv2
from pathlib import Path

caminhoImagem = Path('Anexos, Imagens e Videos/brown-eyes.jpg')
# Coordenadas em (colunas, linhas) a serem mensuradas
a = (148, 127)
b = (469, 126)

imagem = cv2.imread(str(caminhoImagem))

# Desenha uma linha entre as coordenadas
cv2.line(imagem, a, b, (0,255,255), 2)

cv2.imshow('Imagem', imagem)

# Calcula as distâncias
euclidiana = dist.euclidean(a, b)
cityblock  = dist.cityblock(a, b)
chessboard = dist.chebyshev(a, b)

print ('Distância Euclidiana: ' + str(euclidiana) + ' pixels')
print ('Distância City Block: ' + str(cityblock) + ' pixels')
print ('Distância Chessboard: ' + str(chessboard) + ' pixels')

cv2.waitKey(0)
cv2.destroyAllWindows()