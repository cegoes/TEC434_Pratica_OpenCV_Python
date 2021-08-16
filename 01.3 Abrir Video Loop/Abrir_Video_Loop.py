import cv2
import sys
from pathlib import Path

path = Path(sys.path[0])
caminhoImagem = str(path.parent.absolute()) + '\\Anexos, Imagens e Videos\\Megamind.avi'

mostraVideo = cv2.VideoCapture(caminhoImagem)

#Guarda os frames por segundo do vídeo
fps = int(1000 / mostraVideo.get(cv2.CAP_PROP_FPS))

cv2.namedWindow('Passar vídeo continuamente', cv2.WINDOW_KEEPRATIO)

frame_counter = 0

while mostraVideo.isOpened():
    sucess, frame = mostraVideo.read()  
    frame_counter += 1

    if (frame_counter == mostraVideo.get(cv2.CAP_PROP_FRAME_COUNT)):
        frame_counter = 0
        mostraVideo.set(cv2.CAP_PROP_POS_FRAMES, 0) # Set de video frame back to 0

    if (sucess):
        cv2.imshow('Passar vídeo continuamente', frame); # show the frame in "MyVideo" window

    # press 'Q' if you want to exit
    if cv2.waitKey(fps) == ord('q'):
        break

cv2.destroyAllWindows()
mostraVideo.release()
