import cv2
import sys
from pathlib import Path

path = Path(sys.path[0])
caminhoImagem = str(path.parent.absolute()) + '\\Anexos, Imagens e Videos\\len_std.png'

imagem = cv2.imread(caminhoImagem)

#[Yinicio:Yfinal, Xinicio:Xfinal]
imagemROI = imagem[98:194, 106:185]

cv2.imshow('Imagem carregada', imagem)

cv2.imshow('Imagem ROI', imagemROI)

cv2.waitKey(0)
cv2.destroyAllWindows()