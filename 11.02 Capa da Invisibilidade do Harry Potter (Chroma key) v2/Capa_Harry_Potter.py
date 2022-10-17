import cv2
import numpy as np
import pyglet
from pathlib import Path

# Necessário ter instalado o pyglet. Instalar com:
#   pip install pyglet
# No Windows instalar: https://avbin.github.io/AVbin/Download.html
# No Linux instalar: sudo apt-get install libavbin-dev libavbin0

filename = Path("Anexos, Imagens e Videos/Harry_Potter_Theme_Song_Hedwigs_Theme.mp3")

# create a player and queue the song
player = pyglet.media.Player()
player.loop = True
sound = pyglet.media.load(str(filename))
player.queue(sound)
# keep playing for as long as the app is running (or you tell it to stop):
player.play()

#  Create a VideoCapture object and open the input file
cameraCapture = cv2.VideoCapture(0)

background = np.ndarray

while (cv2.waitKey != 27):
    sucess, frame = cameraCapture.read()
    if (sucess==True):
        print ('Camera inicializada...')
        print ('Capturando o background...')
        for i in range(120):
            sucess, frame = cameraCapture.read()
            background = frame
        print ('Imagem do background capturada...')
        break

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

while sucess and cv2.waitKey(1) != 27:
    sucess, frame = cameraCapture.read()    

    if (sucess == False):
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