# Import all essential libraries
import cv2
import numpy as np
import sys
from pathlib import Path

path = Path(sys.path[0])
caminhoImagem = str(path.parent.absolute()) + '\\Anexos, Imagens e Videos\\pessoas-racas.jpg'

# minRange for min skin color Rnage
# maxRange for maximum skin color Range
minRange = np.array([0,133,77],np.uint8)
maxRange = np.array([235,173,127],np.uint8)
image = cv2.imread(caminhoImagem)

# change our image bgr to ycr using cvtcolor() method 
YCRimage = cv2.cvtColor(image,cv2.COLOR_BGR2YCR_CB)

# apply min or max range on skin area in our image
skinArea = cv2.inRange(YCRimage,minRange,maxRange)
detectedSkin = cv2.bitwise_and(image, image, mask = skinArea)

cv2.namedWindow('Imagem entrada/saída', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Imagem entrada/saída', np.hstack([image,detectedSkin]))

cv2.waitKey(0)
cv2.destroyAllWindows()
