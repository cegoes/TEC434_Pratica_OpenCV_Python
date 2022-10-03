import cv2
from pathlib import Path

caminhoImagem = Path('Anexos, Imagens e Videos/len_std.png')

imagem = cv2.imread(str(caminhoImagem))

imagemtexto = imagem.copy()
# desenha um texto na imagem
cv2.putText(imagemtexto, "Foto da Lena", (10, 25), 
	cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

cv2.imshow('Imagem carregada', imagem)
cv2.imshow('Imagem texto', imagemtexto)

cv2.waitKey(0)
cv2.destroyAllWindows()