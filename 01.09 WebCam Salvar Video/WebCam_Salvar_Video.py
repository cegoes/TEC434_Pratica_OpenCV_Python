import cv2
from pathlib import Path


caminhoVideo = Path('Anexos, Imagens e Videos/')

cameraCapture = cv2.VideoCapture(0)

if not cameraCapture.isOpened():
    print('Problema na inicialização da WebCam...')
    exit()

frame_width  =   cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height =   cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps          =   cameraCapture.get(cv2.CAP_PROP_FPS)

print('WIDTH : ' + str(frame_width))
print('HEIGHT: ' + str(frame_height))
print('FPS   : ' + str(fps))

tamanho = (frame_width, frame_height)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
videoGravar = cv2.VideoWriter(str(caminhoVideo / 'GravarWebCam.avi'), fourcc, fps, (int(frame_width),  int(frame_height)), True)

while cameraCapture.isOpened() and cv2.waitKey(1) == -1:
    sucess, frame = cameraCapture.read()    
    videoGravar.write(frame)
    cv2.imshow('Mostra webCam', frame)

videoGravar.release()
cameraCapture.release()
cv2.destroyAllWindows()
