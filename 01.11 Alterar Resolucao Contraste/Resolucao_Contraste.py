import cv2
from pathlib import Path

caminhoImagem = Path('Anexos, Imagens e Videos/len_std.png')
print (caminhoImagem)

imagem256 = cv2.imread(str(caminhoImagem), 0)

cv2.namedWindow("256 Tons", cv2.WINDOW_AUTOSIZE)
cv2.normalize(imagem256, imagem256, 0, 255, cv2.NORM_MINMAX )
cv2.imshow("256 Tons", imagem256)

imagem128 = imagem256 >> 1

cv2.namedWindow("128 Tons", cv2.WINDOW_AUTOSIZE)
cv2.normalize(imagem128, imagem128, 0, 255, cv2.NORM_MINMAX )
cv2.imshow("128 Tons", imagem128)

imagem64 = imagem256 >> 2

cv2.namedWindow("64 Tons", cv2.WINDOW_AUTOSIZE)
cv2.normalize(imagem64, imagem64, 0, 255, cv2.NORM_MINMAX )
cv2.imshow("64 Tons", imagem64)

imagem32 = imagem256 >> 3

cv2.namedWindow("32 Tons", cv2.WINDOW_AUTOSIZE)
cv2.normalize(imagem32, imagem32, 0, 255, cv2.NORM_MINMAX )
cv2.imshow("32 Tons", imagem32)

imagem16 = imagem256 >> 4

cv2.namedWindow("16 Tons", cv2.WINDOW_AUTOSIZE)
cv2.normalize(imagem16, imagem16, 0, 255, cv2.NORM_MINMAX )
cv2.imshow("16 Tons", imagem16)

imagem8 = imagem256 >> 5

cv2.namedWindow("8 Tons", cv2.WINDOW_AUTOSIZE)
cv2.normalize(imagem8, imagem8, 0, 255, cv2.NORM_MINMAX )
cv2.imshow("8 Tons", imagem8)

imagem4 = imagem256 >> 6

cv2.namedWindow("4 Tons", cv2.WINDOW_AUTOSIZE)
cv2.normalize(imagem4, imagem4, 0, 255, cv2.NORM_MINMAX )
cv2.imshow("4 Tons", imagem4)

imagem2 = imagem256 >> 7

cv2.namedWindow("2 Tons", cv2.WINDOW_AUTOSIZE)
cv2.normalize(imagem2, imagem2, 0, 255, cv2.NORM_MINMAX )
cv2.imshow("2 Tons", imagem2)

cv2.waitKey(0)
