import cv2
import numpy as np
from pathlib import Path

caminhoImagem = Path('Anexos, Imagens e Videos/len_std.png')
# Read image from file
# Make sure that the image is in grayscale
img = cv2.imread(str(caminhoImagem), 0)

# Aplica a DFT
dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)    # Applying DFT

# Devolve novamente a imagem para o domínio do espaço
img_back = cv2.idft(dft, cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT )
#img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

# Converte a matrix novamente para o tipo unsigned 8bits e ajusta a escala dos pixels
img_back = np.uint8(img_back/255)

# Mostra a imagem original
cv2.imshow("Original Image", img)

# show the image
cv2.imshow("Resultado Image", (img_back))

cv2.waitKey()
cv2.destroyAllWindows()