from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

caminhoImagem = Path('Anexos, Imagens e Videos/len_std.png')
imagem = mpimg.imread(str(caminhoImagem))

# origin='upper' (Muda a legenda do eixo y com a origem no canto superior esquerdo)
plt.imshow(imagem, origin='upper')
plt.show()