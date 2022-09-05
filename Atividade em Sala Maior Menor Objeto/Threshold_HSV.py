import cv2 as cv
import sys
from pathlib import Path

path = Path(sys.path[0])
caminhoImagem = str(path.parent.absolute()) + '\\Anexos, Imagens e Videos\\'
frame_HSV = None

max_value = 255
max_value_H = 360 // 2
low_H = 0
low_S = 0
low_V = 0
high_H = max_value_H
high_S = max_value
high_V = max_value
window_imagem = 'Imagem original'
window_trackbars = 'Janela threshold HSV'
window_deteccao = 'Imagem segmentada'
low_H_name = 'Low H'
low_S_name = 'Low S'
low_V_name = 'Low V'
high_H_name = 'High H'
high_S_name = 'High S'
high_V_name = 'High V'

def on_low_H_thresh_trackbar(val):
    global low_H
    global high_H
    low_H = val
    low_H = min(high_H-1, low_H)
    mostra_resultado()

def on_high_H_thresh_trackbar(val):
    global low_H
    global high_H
    high_H = val
    high_H = max(high_H, low_H+1)
    mostra_resultado()

def on_low_S_thresh_trackbar(val):
    global low_S
    global high_S
    low_S = val
    low_S = min(high_S-1, low_S)
    mostra_resultado()

def on_high_S_thresh_trackbar(val):
    global low_S
    global high_S
    high_S = val
    high_S = max(high_S, low_S+1)
    mostra_resultado()

def on_low_V_thresh_trackbar(val):
    global low_V
    global high_V
    low_V = val
    low_V = min(high_V-1, low_V)
    mostra_resultado()

def on_high_V_thresh_trackbar(val):
    global low_V
    global high_V
    high_V = val
    high_V = max(high_V, low_V+1)
    mostra_resultado()

def mostra_resultado():
    global frame_HSV
    frame_threshold = cv.inRange(frame_HSV, (low_H, low_S, low_V), (high_H, high_S, high_V))
    cv.imshow(window_deteccao, frame_threshold)

def main():
    cv.namedWindow(window_imagem)
    cv.namedWindow(window_trackbars)
    cv.createTrackbar(low_H_name, window_trackbars , low_H, max_value_H, on_low_H_thresh_trackbar)
    cv.createTrackbar(high_H_name, window_trackbars , high_H, max_value_H, on_high_H_thresh_trackbar)
    cv.createTrackbar(low_S_name, window_trackbars , low_S, max_value, on_low_S_thresh_trackbar)
    cv.createTrackbar(high_S_name, window_trackbars , high_S, max_value, on_high_S_thresh_trackbar)
    cv.createTrackbar(low_V_name, window_trackbars , low_V, max_value, on_low_V_thresh_trackbar)
    cv.createTrackbar(high_V_name, window_trackbars , high_V, max_value, on_high_V_thresh_trackbar)

    imagem = cv.imread(caminhoImagem + 'h.png')
    if imagem is None:
        print('Imagem não encontrada! Finalizando o programa...')
        exit()

    cv.imshow(window_imagem, imagem)
    global frame_HSV
    frame_HSV = cv.cvtColor(imagem, cv.COLOR_BGR2HSV)
    mostra_resultado()
    
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    main()

