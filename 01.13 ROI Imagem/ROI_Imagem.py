import cv2
from pathlib import Path

caminhoImagem = Path('Anexos, Imagens e Videos/len_std.png')

imagem = cv2.imread(str(caminhoImagem))

#[Yinicio:Yfinal, Xinicio:Xfinal]
imagemROI = imagem[98:194, 106:185]

cv2.imshow('Imagem carregada', imagem)

cv2.imshow('Imagem ROI', imagemROI)

cv2.waitKey(0)
cv2.destroyAllWindows()