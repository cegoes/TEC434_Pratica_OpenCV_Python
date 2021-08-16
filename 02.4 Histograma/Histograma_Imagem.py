import numpy as np
import cv2
from matplotlib import pyplot as plt
import sys
from pathlib import Path

path = Path(sys.path[0])
caminhoDiretorio = str(path.parent.absolute()) + '\\Anexos, Imagens e Videos\\'

nomeImagens = ['ImagemAltoContraste.tif','ImagemBaixoContraste.tif','ImagemClara.tif','ImagemEscura.tif']
nomeJanelas = ['Alto contraste','Baixo contraste','Imagem clara','Imagem escura']
imagem = []

for n in range(0,len(nomeJanelas)):
    imagem.append(cv2.imread(caminhoDiretorio + nomeImagens[n]))

# Calculate histogram with mask and without mask
# Check third argument for mask
histAlto =   cv2.calcHist(imagem[0],[0],None,[256],[0,256])
histBaixo =  cv2.calcHist(imagem[1],[0],None,[256],[0,256])
histClara =  cv2.calcHist(imagem[2],[0],None,[256],[0,256])
histEscura = cv2.calcHist(imagem[3],[0],None,[256],[0,256])
plt.subplot(241, title = 'Alto contraste'), plt.imshow(imagem[0], 'gray')
plt.subplot(242, title = 'Baixo contraste'), plt.imshow(imagem[1], 'gray')
plt.subplot(243, title = 'I. clara'), plt.imshow(imagem[2], 'gray')
plt.subplot(244, title = 'I. escura'), plt.imshow(imagem[3], 'gray')
plt.subplot(245, title = 'Histograma alto c.'), plt.plot(histAlto)
plt.subplot(246, title = 'Histograma baixo c.'), plt.plot(histBaixo)
plt.subplot(247, title = 'Histograma imagem c.'), plt.plot(histClara)
plt.subplot(248, title = 'Histograma imagem e.'), plt.plot(histEscura)
plt.xlim([0,256])
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()