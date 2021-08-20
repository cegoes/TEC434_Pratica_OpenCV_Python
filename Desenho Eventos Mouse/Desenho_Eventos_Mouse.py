import cv2
import sys
from pathlib import Path

path = Path(sys.path[0])
caminhoImagem = str(path.parent.absolute()) + '\\Anexos, Imagens e Videos\\len_std.png'

imagem = cv2.imread(caminhoImagem)

# This is the mouse callback function:
def draw_circle(event, x, y, flags, param):

    if event == cv2.EVENT_LBUTTONDBLCLK:
        print("event: EVENT_LBUTTONDBLCLK")
        cv2.circle(imagem, (x, y), 10, (0,0,255), 2)
    if event == cv2.EVENT_MOUSEMOVE:
        print("event: EVENT_MOUSEMOVE")
    if event == cv2.EVENT_LBUTTONUP:
        print("event: EVENT_LBUTTONUP")
    if event == cv2.EVENT_LBUTTONDOWN:
        print("event: EVENT_LBUTTONDOWN")
    cv2.imshow('Imagem carregada', imagem)
        


# We create a named window where the mouse callback will be established
cv2.namedWindow('Imagem carregada')

cv2.setMouseCallback('Imagem carregada', draw_circle)



cv2.waitKey(0)

