import cv2
import sys
from pathlib import Path

path = Path(sys.path[0])
caminhoImagem = str(path.parent.absolute()) + '\\Anexos, Imagens e Videos\\len_std.png'

image = cv2.imread(caminhoImagem)

(h, w, d) = image.shape
tipo = image.dtype
print("width={}, height={}, depth={}, tipo={}".format(w, h, d, tipo))

# display the image to our screen -- we will need to click the window
# open by OpenCV and press a key on our keyboard to continue execution
cv2.imshow("Image", image)
cv2.waitKey(0)

