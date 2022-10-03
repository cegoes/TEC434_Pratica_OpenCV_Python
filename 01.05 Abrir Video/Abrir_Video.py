import cv2
from pathlib import Path

caminhoVideo = Path('Anexos, Imagens e Videos/Road traffic.mp4')

videoCarregado = cv2.VideoCapture(str(caminhoVideo))

#Guarda os frames por segundo do vídeo
fps = int(1000 / videoCarregado.get(cv2.CAP_PROP_FPS))

cv2.namedWindow('Abrir Vídeo', cv2.WINDOW_GUI_EXPANDED )

while videoCarregado.isOpened():
    sucess, frame = videoCarregado.read()  
    # if video finished or no Video Input
    if not sucess:
        break  
    cv2.imshow('Abrir Vídeo', frame)

    # press 'Q' if you want to exit
    if cv2.waitKey(fps) == ord('q'):
        break

cv2.destroyAllWindows()
videoCarregado.release()
