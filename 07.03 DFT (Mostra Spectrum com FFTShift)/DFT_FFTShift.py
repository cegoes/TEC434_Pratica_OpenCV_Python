import numpy as np
import cv2
from matplotlib import pyplot as plt
from pathlib import Path

caminhoImagem = Path('Anexos, Imagens e Videos/len_std.png')

img = cv2.imread(str(caminhoImagem), cv2.IMREAD_GRAYSCALE)

img_float32 = np.float32(img)

dft = cv2.dft(img_float32, flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()   

plt.cla() # - Clear the current axes.
plt.clf() # - Clear the current figure.