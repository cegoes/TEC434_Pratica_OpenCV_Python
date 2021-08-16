import cv2
import numpy
import sys
from pathlib import Path

path = Path(sys.path[0])
caminhoImagem = str(path.parent.absolute()) + '\\Anexos, Imagens e Videos\\Fig0305(a)(DFT_no_log).tif'

#Carrega a imagem
image = cv2.imread(caminhoImagem)
cv2.imshow('Imagem original', image)

fg = numpy.float32(image)
fg = fg + 1

cv2.log(fg,fg)
cv2.normalize(fg,fg,0,255,cv2.NORM_MINMAX)

cv2.imshow('Transformação Log', fg)
cv2.convertScaleAbs(fg,fg)

cv2.waitKey(0)