import cv2
import numpy as np
from pygame import mixer
from pathlib import Path

# Necessário ter instalado o pyglet. Instalar com:
#   pip install pyglet
# No Windows instalar: https://avbin.github.io/AVbin/Download.html
# No Linux instalar: sudo apt install gstreamer1.0-opencv

filename =  Path('Anexos, Imagens e Videos')

# create a mixer and queue the song
mixer.init()
mixer.music.load(str(filename / 'Harry_Potter_Theme_Song_Hedwigs_Theme.mp3'))
mixer.music.play()

#  Create a VideoCapture object and open the input file
videoPlayer = cv2.VideoCapture(str(filename / 'Input.mp4'))
if not videoPlayer.isOpened():
    print('Falha na abertura do vídeo...')

# Declarar as variáveis fora do looping faz a execução ser mais rápida!
background = np.array
mask1 = np.array
mask2 = np.array
hsv = np.array
res1 = np.array
res2 = np.array
mascara = np.array
final_output = np.array
kernel = np.ones((3,3),np.uint8)

sucess = True
frame = np.ndarray
print ('Capturando o background...')

while (sucess):
    sucess, frame = videoPlayer.read()
    if sucess == True:
        background = frame
        print ('Imagem do background capturada...')
        break

cv2.namedWindow("Capa da Invisibilidade.", cv2.WINDOW_FREERATIO)

#low_blue = np.array([94, 80, 2])
#high_blue = np.array([126, 255, 255])
# low_green = np.array([36, 45, 0])
# high_green = np.array([86, 250, 255])
low_red1 = np.array([0, 120, 70])
high_red1 = np.array([10, 255, 255])
low_red2 = np.array([170, 120, 70])
high_red2 = np.array([180, 255, 255])

# Segundo dividido pela quantidade de Frames
tempoFrame =  1 / (videoPlayer.get(cv2.CAP_PROP_FPS))

espera = 0
tecla = 0
tempoinicio = 0
final = 0 

while sucess and tecla != 27:
    tempoinicio = cv2.getTickCount()
    sucess, frame = videoPlayer.read()    

    if (sucess == False):
        print('Terminou o vídeo...')
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Vermelho
    mask1 = cv2.inRange(hsv, low_red1, high_red1)
    mask2 = cv2.inRange(hsv, low_red2, high_red2)
    mask1 = mask1 + mask2

    # Azul
    #mask1 = cv2.inRange(hsv, low_blue, high_blue)

    # Verde
    #mask1 = cv2.inRange(hsv, low_green, high_green)

    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, kernel)
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, kernel)

    mascara = cv2.bitwise_not(mask1)

    res1 = cv2.bitwise_and(frame, frame, mask = mascara)

    res2 = cv2.bitwise_and(background, background, mask = mask1)

    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)

    cv2.imshow("Capa da Invisibilidade.", final_output)
    e2 = cv2.getTickCount()
    final = ((e2 - tempoinicio) / cv2.getTickFrequency())

    espera = int((tempoFrame - final) * 1000)

    if espera <= 0:
        espera = 1
    
    tecla = cv2.waitKey(espera)

# When everything done, release the video capture object
videoPlayer.release()
mixer.quit()

# Closes all the frames
cv2.destroyAllWindows()