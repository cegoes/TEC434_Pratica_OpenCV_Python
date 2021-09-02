import cv2

# Carrega a imagem
image = cv2.imread('.\\Anexos, Imagens e Videos\\exmorfologia0.png')

cv2.namedWindow("Imagem original",cv2.WINDOW_GUI_EXPANDED)
cv2.imshow("Imagem original",image)

elem1 = cv2.getStructuringElement( cv2.MORPH_CROSS, ( 3, 3 ) ) # Elemento estruturante

dilatacao = cv2.morphologyEx(image,cv2.MORPH_DILATE ,elem1)

erosao = cv2.morphologyEx(image,cv2.MORPH_ERODE,elem1)

abertura = cv2.morphologyEx(image,cv2.MORPH_OPEN ,elem1)

fechamento = cv2.morphologyEx(image,cv2.MORPH_CLOSE,elem1)

cv2.namedWindow("Dilatação imagem",cv2.WINDOW_GUI_EXPANDED)
cv2.imshow("Dilatação imagem",dilatacao)

cv2.namedWindow("Erosão imagem",cv2.WINDOW_GUI_EXPANDED)
cv2.imshow("Erosão imagem",erosao)

cv2.namedWindow("Abertura imagem",cv2.WINDOW_GUI_EXPANDED)
cv2.imshow("Abertura imagem",abertura)

cv2.namedWindow("Fechamento imagem",cv2.WINDOW_GUI_EXPANDED)
cv2.imshow("Fechamento imagem",fechamento)

cv2.waitKey(0)