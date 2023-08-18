import cv2
import numpy as np
from pygame import mixer
from pathlib import Path

# Necessário ter instalado o pyglet. Instalar com:
#   pip install pyglet
# No Windows instalar: https://avbin.github.io/AVbin/Download.html
# No Linux instalar: sudo apt install gstreamer1.0-opencv

filename = Path("Anexos, Imagens e Videos/Harry_Potter_Theme_Song_Hedwigs_Theme.mp3")

# create a mixer and queue the song
mixer.init()
mixer.music.load(str(filename))
mixer.music.play()

#  Create a VideoCapture object and open the input file
print ('Tentando iniciar a camera...')
cameraCapture = cv2.VideoCapture(0)

if cameraCapture.isOpened()==False:
    print ('Falha na inicialização da camera...')
    exit(1)

background = np.ndarray
frame = np.ndarray
contador = 0

while (cv2.waitKey != 27) and (cameraCapture.isOpened()):

    sucess, frame = cameraCapture.read()
    if (frame is not(None)) and (sucess == True):
        if contador > 120:
            background = frame
            print ('Imagem do background capturada...')
            break
    contador = contador + 1

cv2.namedWindow("Capa da Invisibilidade.", cv2.WINDOW_FREERATIO)

kernel = np.ones((3,3),np.uint8)

#low_blue = np.array([94, 80, 2])
#high_blue = np.array([126, 255, 255])
#low_green = np.array([36, 45, 0])
#high_green = np.array([86, 250, 255])
low_red1 = np.array([0, 120, 70])
high_red1 = np.array([10, 255, 255])
low_red2 = np.array([170, 120, 70])
high_red2 = np.array([180, 255, 255])

sucess = True

while sucess and cv2.waitKey(1) != 27:
    sucess, frame = cameraCapture.read()    

    if (sucess == False):
        print('Falha na captura do frame...')
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Vermelho
    mask1 = cv2.inRange(hsv, low_red1, high_red1)
    mask2 = cv2.inRange(hsv, low_red2, high_red2)
    mask1 = mask1 + mask2

    # Azul
    # mask1 = cv2.inRange(hsv, low_blue, high_blue)

    # Verde
    #mask1 = cv2.inRange(hsv, low_green, high_green)

    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, kernel)
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, kernel)

    mascara = cv2.bitwise_not(mask1)

    res1 = cv2.bitwise_and(frame, frame, mask = mascara)

    res2 = cv2.bitwise_and(background, background, mask = mask1)

    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)

    cv2.imshow("Capa da Invisibilidade.",final_output)

# When everything done, release the video capture object
cameraCapture.release()

# Closes all the frames
cv2.destroyAllWindows()