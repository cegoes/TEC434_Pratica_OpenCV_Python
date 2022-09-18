import cv2
from pathlib import Path

caminhoImagem = Path('Anexos, Imagens e Videos/Fig0326(a)(embedded_square_noisy_512).tif')

# Carrega a imagem
image = cv2.imread(str(caminhoImagem),0)
cv2.namedWindow('Imagem original', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Imagem original', image)

# Equalização Global
equaGlobal = cv2.equalizeHist(image)
cv2.namedWindow('Equalização Global', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Equalização Global', equaGlobal)

# CLAHE (Contrast Limited Adaptive Histogram Equalization)
# Cria um objeto CLAHE (Argumentos são opcionais).
clahe = cv2.createCLAHE()
cl1 = clahe.apply(image)
cv2.namedWindow('Equalização Adaptativa', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Equalização Adaptativa', cl1)

cv2.waitKey(0)
cv2.destroyAllWindows()