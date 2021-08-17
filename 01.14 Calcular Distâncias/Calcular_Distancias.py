import scipy.spatial.distance as dist
import cv2
import sys
from pathlib import Path

path = Path(sys.path[0])
caminhoImagem = str(path.parent.absolute()) + '\\Anexos, Imagens e Videos\\brown-eyes.jpg'

a = (148 , 127)
b = (469, 126)

imagem = cv2.imread(caminhoImagem)

cv2.line(imagem, a, b, (0,255,2255), 2)

cv2.imshow('Imagem', imagem)

euclidiana = dist.euclidean(a, b)
cityblock  = dist.cityblock(a, b)
chessboard = dist.chebyshev(a, b)

print ('Distância Euclidiana: ' + str(euclidiana) + ' pixels')
print ('Distância City Block: ' + str(cityblock) + ' pixels')
print ('Distância Chessboard: ' + str(chessboard) + ' pixels')

cv2.waitKey(0)
cv2.destroyAllWindows()