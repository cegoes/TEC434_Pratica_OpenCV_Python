import cv2
import sys
from pathlib import Path

path = Path(sys.path[0])
caminhoImagem = str(path.parent.absolute()) + '\\Anexos, Imagens e Videos\\Road traffic.mp4'

mostraVideo = cv2.VideoCapture(caminhoImagem)

#Guarda os frames por segundo do vídeo
fps = mostraVideo.get(cv2.CAP_PROP_FPS)

cv2.namedWindow('Abrir Vídeo', cv2.WINDOW_GUI_EXPANDED )

while mostraVideo.isOpened():
    sucess, frame = mostraVideo.read()  
    # if video finished or no Video Input
    if not sucess:
        break  
    cv2.imshow('Abrir Vídeo', frame)

    # press 'Q' if you want to exit
    if cv2.waitKey(int(fps)) & 0xFF == ord('q'):
        break

cv2.destroyWindow('Abrir Vídeo')
mostraVideo.release()
