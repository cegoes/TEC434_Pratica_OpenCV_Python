import cv2 as cv
from pathlib import Path

caminhoImagem = Path('Anexos, Imagens e Videos/bottom-shape-coloring-page.jpg')

src = cv.imread(str(caminhoImagem))
hsv_imagem = cv.cvtColor(src, cv.COLOR_BGR2HSV)

hsv_threshold = cv.inRange(hsv_imagem, (17,69,147), (32,189,221))
    
cv.imshow("HSV Binarizado", hsv_threshold)

largest_area=0
largest_area2=0
largest_contour_index1=0
largest_contour_index2=0
a = 0

contours, hierarchy = cv.findContours( hsv_threshold, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE )
bounding_rect1 = None
bounding_rect2 = None

print(  "Quantidade de Contornos: " + str(len(contours)) )

# Interage com cada contorno.
for i in range(len(contours)):
    print(  str(i) + " area  " + str(a) )
    #  Descobre a área do contorno
    a = cv.contourArea(contours[i],False)
    if(a > largest_area):
        largest_area = a
        # Armazena o índice do contorno
        largest_contour_index1 = i
        # Descobre o retângulo delimitador de cada contorno
        bounding_rect1 = cv.boundingRect(contours[i])

# Interage com cada contorno.
for i in range(len(contours)):

    #  Descobre a área do contorno
    a = cv.contourArea(contours[i],False)
    if(a > largest_area2 and a < largest_area):
        largest_area2 = a
        # Armazena o índice do contorno
        largest_contour_index2 = i
        # Descobre o retângulo delimitador de cada contorno
        bounding_rect2 = cv.boundingRect(contours[i])

cv.rectangle(src, bounding_rect1,  (0,255,255), 2, 8, 0)
cv.rectangle(src, bounding_rect2,  (0,0,255), 2, 8, 0)
cv.namedWindow( "Display window", cv.WINDOW_AUTOSIZE )
cv.imshow( "Display window", src )
cv.waitKey()
