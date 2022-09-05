import cv2 as cv
import sys
from pathlib import Path
import numpy as np

from cv2 import blur

path = Path(sys.path[0])
caminhoImagem = str(path.parent.absolute()) + '\\Anexos, Imagens e Videos\\'

mostraVideo = cv.VideoCapture(caminhoImagem + 'frutas.mp4')

#Guarda os frames por segundo do vídeo
fps = int(1000 / mostraVideo.get(cv.CAP_PROP_FPS))
cv.namedWindow('Abrir Vídeo', cv.WINDOW_GUI_EXPANDED )
cv.namedWindow('Vídeo Processado', cv.WINDOW_GUI_EXPANDED )
cv.namedWindow('Vídeo Threshold', cv.WINDOW_GUI_EXPANDED )

# HSV color thresholds for YELLOW
THRESHOLD_LOW = (20, 72, 80)
THRESHOLD_HIGH = (44, 255, 255)

while mostraVideo.isOpened():
    sucess, frame = mostraVideo.read()  

    # Se não tiver vídeo, interrompe
    if not sucess:
        break  

    frame = cv.GaussianBlur(frame.copy(), (3, 3), 0)

    hsv_imagem = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    hsv_threshold = cv.inRange(hsv_imagem, THRESHOLD_LOW, THRESHOLD_HIGH)

    elem = cv.getStructuringElement( cv.MORPH_ELLIPSE, ( 55, 55 ) ) # Elemento estruturante
    hsv_threshold = cv.morphologyEx(hsv_threshold.copy(),cv.MORPH_CLOSE ,elem)

    largest_area=0
    largest_contour_index=0
    a = 0

    contours, hierarchy = cv.findContours( hsv_threshold, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE )
    bounding_rect = None

    # Interage com cada contorno.
    for i in range(len(contours)):
        #  Descobre a área do contorno
        a = cv.contourArea(contours[i],False)
        if(a > largest_area):
            largest_area = a
            # Armazena o índice do contorno
            largest_contour_index1 = i
            # Descobre o retângulo delimitador de cada contorno
            bounding_rect = cv.boundingRect(contours[i])

    cv.imshow('Abrir Vídeo', frame)
    cv.imshow("Vídeo Threshold", hsv_threshold)
    cv.rectangle(frame, bounding_rect,  (0,0,255), 2, 8, 0)
    cv.imshow( "Vídeo Processado", frame )

    # press 'Q' if you want to exit
    if cv.waitKey(fps) == ord('q'):
        break

mostraVideo.release()
cv.destroyAllWindows()
cv.waitKey(0)