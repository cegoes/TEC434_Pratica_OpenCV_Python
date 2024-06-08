import cv2
import numpy as np
from pathlib import Path

# Define o tamanho do recorte
crop_size = 640
cropped_image = None
point = None

# Função de callback do mouse
def mouse_callback(event, x, y, flags, param):
    global point, image, cropped_image
    point = (x, y)
    cropped_image = crop_image(image, point, crop_size)

    if event == cv2.EVENT_LBUTTONDOWN:       
        # Salva o recorte em um arquivo
        cv2.imwrite('_Testes/croped.png', cropped_image)
        print("Recorte salvo como 'croped.jpg'")

    elif event == cv2.EVENT_MOUSEMOVE:
        if cropped_image is not None:
            # Exibe o recorte em tempo real
            cv2.imshow('Imagem Recorte', cropped_image)

# Função para recortar a imagem
def crop_image(image, point, crop_size):
    height, width = image.shape[:2]
    cx, cy = point

    # Calcula as coordenadas do canto superior esquerdo do recorte
    x1 = max(0, cx - crop_size // 2)
    y1 = max(0, cy - crop_size // 2)

    # Calcula as coordenadas do canto inferior direito do recorte
    x2 = min(width, x1 + crop_size)
    y2 = min(height, y1 + crop_size)

    # Ajusta as coordenadas do canto superior esquerdo caso o recorte ultrapasse os limites da imagem
    if x2 - x1 < crop_size:
        x1 = max(0, x2 - crop_size)
    if y2 - y1 < crop_size:
        y1 = max(0, y2 - crop_size)

    # Recorta a imagem
    cropped_image = image[y1:y2, x1:x2]
    return cropped_image

# Lê a imagem
image = cv2.imread(str(Path('Anexos, Imagens e Videos/a_vm1125.png')))

# Cria uma janela para exibir a imagem
cv2.namedWindow('Imagem',cv2.WINDOW_NORMAL)
cv2.setMouseCallback('Imagem', mouse_callback)
cv2.namedWindow('Imagem Recorte',cv2.WINDOW_NORMAL)

# Exibe a imagem
cv2.imshow('Imagem', image)

# Aguarda o usuário pressionar uma tecla
cv2.waitKey(0)

# Fecha todas as janelas
cv2.destroyAllWindows()