import cv2
import numpy as np
from pathlib import Path

caminhoImagem = Path('Anexos, Imagens e Videos/20211029_105654.jpg')

def onTrackbarChange(max_slider):
    cimg = np.copy(img)

    p1 = max_slider
    p2 = max_slider * 0.4

    # Detect circles using HoughCircles transform
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, cimg.shape[0]/64, param1=p1, param2=p2, minRadius=65, maxRadius=100)
    imgMoedas = np.ndarray(gray.shape[:2],np.uint8)

    # If at least 1 circle is detected
    if circles is not None:
        cir_len = circles.shape[1] # store length of circles found
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            # Draw the outer circle
            cv2.circle(imgMoedas, (i[0], i[1]), i[2], 255, 2)
    else:
        cir_len = 0 # no circles detected
    
    # Display output image
    cv2.imshow('Image', cimg)    
    cv2.imshow('Imagem Moedas', imgMoedas)  

    #Detecta os contornos de uma imagem binarizada:
    contours, hierarchy = cv2.findContours( imgMoedas, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE )

    colunas,linhas = imgMoedas.shape[:2]

    imgTiposMoedas = np.zeros((colunas, linhas , 3), np.uint8)

    # Interage com cada contorno.
    for i in range(len(contours)):
        #  Descobre a área do contorno
        area = cv2.contourArea(contours[i], False)
        print(  str(i) + " area  " + str(area) )

        if (area>16000 and area<18000):
            color = (0,0,255)
        elif (area>27000):
            color = (0,255,0)
        elif (area>24000):
            color = (255,0,0)
        else:
            color = (255,255,255)            
        # Para desenhar todos os contornos é necessário fazer um iterator para cada um variando o índice do contorno.
        cv2.drawContours( imgTiposMoedas, contours, i, color, cv2.FILLED, 8)

    cv2.imshow("Moedas", imgTiposMoedas)

if __name__ == "__main__":
    # Read image
    img = cv2.imread(str(caminhoImagem), 1)

    # Convert to gray-scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    gray = cv2.blur(gray, (9,9))

    # Create display windows
    cv2.namedWindow("Moedas", cv2.WINDOW_GUI_NORMAL)
    cv2.namedWindow("Image", cv2.WINDOW_GUI_NORMAL)
    cv2.namedWindow("Imagem Moedas", cv2.WINDOW_GUI_NORMAL)

    # Trackbar will be used for changing threshold for edge 
    initThresh = 105 
    maxThresh = 200 

    # Create trackbar
    cv2.createTrackbar("Threshold", "Image", initThresh, maxThresh, onTrackbarChange)
    onTrackbarChange(initThresh)
    
    while True:
        key = cv2.waitKey(1)
        if key == 27:
            break

    cv2.destroyAllWindows()