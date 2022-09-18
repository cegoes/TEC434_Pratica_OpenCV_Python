import cv2
from pathlib import Path

diretorioVideo = Path('Anexos, Imagens e Videos/')

video = cv2.VideoCapture(str(diretorioVideo / 'Megamind.avi'))

if not video.isOpened():
    print('O vídeo não foi encontrado...')
    exit()

# Armazena os frames por segundo do vídeo
fps          = video.get(cv2.CAP_PROP_FPS)
# Armazena as colunas do vídeo
frame_width  = video.get(cv2.CAP_PROP_FRAME_WIDTH)
# Armazena as linhas do vídeo
frame_height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)

print('FPS   :' + str(fps))
print('WIDTH :' + str(frame_width))
print('HEIGHT:' + str(frame_height))

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
videoGravar = cv2.VideoWriter(str(diretorioVideo / 'Megamind_Gravado.avi'), fourcc, fps, (int(frame_width),  int(frame_height)), True)
#VideoWriter video ("MyVideo.avi", -1, 30, frameSize, true); //initialize the VideoWriter object

while video.isOpened():
    sucess, frame = video.read()  
    # if video finished or no Video Input
    if not sucess:
        print("Terminado o recebimento dos frames! Saindo...")
        break
    # write the flipped frame
    videoGravar.write(frame)

print('Vídeo gravado!')

# Release everything if job is finished
video.release()
videoGravar.release()