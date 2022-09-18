import cv2 as cv
from pathlib import Path

caminhoImagem = Path('Anexos, Imagens e Videos')

src = cv.imread(str(caminhoImagem / "shape.jpg"))
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
_, gray = cv.threshold(gray,200, 255, cv.THRESH_BINARY_INV) #Threshold the gray
cv.imshow("gray", gray)
largest_area=0
largest_contour_index=0

contours, hierarchy = cv.findContours( gray, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE )
bounding_rect = None

# Interage com cada contorno.
for i in range(len(contours)):
    #  Descobre a área do contorno
    a = cv.contourArea(contours[i],False)
    if(a > largest_area):
        largest_area = a
        print(  str(i) + " area  " + str(a) )
        # Armazena o índice do contorno
        largest_contour_index = i
        # Descobre o retângulo delimitador de cada contorno
        bounding_rect = cv.boundingRect(contours[i])

color = (255,0,255)

# Desenha o contorno e retângulo
cv.drawContours( src, contours, largest_contour_index, color, cv.FILLED, 8)
cv.rectangle(src, bounding_rect,  (0,0,255), 2, 8, 0)
cv.namedWindow( "Display window", cv.WINDOW_AUTOSIZE )
cv.imshow("Display window", src)
cv.waitKey()
