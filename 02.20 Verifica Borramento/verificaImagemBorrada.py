import cv2
from pathlib import Path
from matplotlib import pyplot as plt

# Verifica a variância do Lalaciano da Imagem,
# Se a variância for baixa, significa que os valores dos dados 
# estão agrupados em torno da média, indicando uma distribuição 
# mais uniforme dos dados. Se a variância for alta, significa 
# que os valores dos dados estão mais espalhados em torno 
# da média, indicando uma distribuição mais ampla dos dados.
def verificaBorramento(imagem):
    img = imagem.copy()
    borrada = bool
    varianceLaplacian = cv2.Laplacian(img,cv2.CV_64F).var()
    print(varianceLaplacian)
    # Limiar 100 definido para a variância
    if varianceLaplacian < 100:
        return True
    else:
        return False

caminhoImagem = Path('Anexos, Imagens e Videos')
# Carrega a imagem
imageA = cv2.imread(str(caminhoImagem / 'len_gray_blured.png'))
imageB = cv2.imread(str(caminhoImagem / 'len_gray.png'))
print('Imagem A está borrada? ' + str(verificaBorramento(imageA)))
print('Imagem B está borrada? ' + str(verificaBorramento(imageB)))

# Mostra as imagens e seus histogramas
plt.subplot(121, title = 'Imagem A'), plt.imshow(imageA)
plt.subplot(122, title = 'Imagem B'), plt.imshow(imageB)
plt.show()