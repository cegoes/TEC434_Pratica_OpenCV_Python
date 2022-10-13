import numpy as np
import diplib as dip
import cv2
from pathlib import Path

caminhoImagem = Path('Anexos, Imagens e Videos/test_image.png')

img_grey = cv2.imread(str(caminhoImagem), cv2.IMREAD_GRAYSCALE)
afterMedian = cv2.medianBlur(img_grey, 3)
thresh = 140

bin = afterMedian > thresh

sk = dip.EuclideanSkeleton(bin, endPixelCondition='three neighbors')

cv2.imshow("Original Image",cv2.normalize(np.uint8(bin),None,0,255,cv2.NORM_MINMAX))
cv2.imshow("Thinning Skeletonization",cv2.normalize(np.uint8(sk),None,0,255,cv2.NORM_MINMAX))

cv2.waitKey()
cv2.destroyAllWindows()