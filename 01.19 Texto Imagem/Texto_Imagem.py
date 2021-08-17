import cv2
import sys
from pathlib import Path

path = Path(sys.path[0])
caminhoImagem = str(path.parent.absolute()) + '\\Anexos, Imagens e Videos\\len_std.png'

imagem = cv2.imread(caminhoImagem)

imagemtexto = imagem.copy()
# desenha um texto na imagem
cv2.putText(imagemtexto, "Foto da Lena", (10, 25), 
	cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

cv2.imshow('Imagem carregada', imagem)
cv2.imshow('Imagem texto', imagemtexto)

cv2.waitKey(0)
cv2.destroyAllWindows()