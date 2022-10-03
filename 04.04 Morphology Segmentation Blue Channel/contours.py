#-*- coding: utf-8 -*-

import numpy as np
import cv2
from pathlib import Path

caminhoImagem = Path('Anexos, Imagens e Videos/HeLa-I.jpg')
image = cv2.imread(str(caminhoImagem))
cv2.namedWindow("Main", cv2.WINDOW_NORMAL)
cv2.imshow("Main", image)

# Extraction of Blue channel
b = image[:,:,0]
cv2.namedWindow("Only Blue Channel", cv2.WINDOW_NORMAL)
cv2.imshow("Only Blue Channel", b)

# Callback Function for Trackbar (but do not any work)
def nothing(x):
    pass

 # Generate trackbar Window Name
TrackbarName = "Trackbar"

 # Make Window and Trackbar
cv2.namedWindow("window", cv2.WINDOW_NORMAL)
cv2.createTrackbar(TrackbarName, "window", 0, 250, nothing)

img_threshed = np.zeros(b.shape, np.uint8)

while True:
   # Get kernel size in trackbar
   TrackbarPos = cv2.getTrackbarPos(TrackbarName, "window")
   # Apply dilation
   limit = TrackbarPos
   ret,img_threshed = cv2.threshold(b,limit,255,cv2.THRESH_BINARY)
   # Show in window
   cv2.imshow("window", img_threshed)


   # Expanding borders of the objects
   kernel = np.ones((9, 9),np.uint8)
   img_dilated = cv2.dilate(img_threshed, kernel)
   img_dilated = cv2.dilate(img_dilated, kernel)
   kernel = np.ones((11, 11),np.uint8)
   img_dilated = cv2.erode(img_dilated, kernel)
   cv2.namedWindow("Dilatedx2 and Eroded Blue Channel", cv2.WINDOW_NORMAL)
   cv2.imshow("Dilatedx2 and Eroded Blue Channel", img_dilated)

   # Retrieving contours by subtraction base objects from the expanded objects
   img_contours = img_dilated - img_threshed
   cv2.namedWindow("Contours", cv2.WINDOW_NORMAL)
   cv2.imshow("Contours", img_contours)

   ch = cv2.waitKey(27)
   if ch == 27 or ch == 0x10001b:
      break

cv2.destroyAllWindows()

# About photo (PL):
# HeLa - uma linha celular derivada de células de câncer cervical coletadas de Henrietta Lacks, de 31 anos.
# A linha celular HeLa é usada para estudar a biologia das células cancerosas. As células são significativamente diferentes das células epiteliais cervicais normais. Eles sofreram transformação neoplásica como resultado da infecção pelo vírus do papiloma HPV 18. A linha é caracterizada por um crescimento notavelmente rápido, excedendo outras linhas de células neoplásicas. Atualmente, a massa total das células HeLa excede significativamente o peso do paciente do qual a amostra foi retirada [1].
# De acordo com alguns cientistas, as células HeLa são uma espécie completamente nova e distinta de organismos unicelulares, desenvolvida pela diferenciação das células epiteliais cervicais femininas sob a influência do papilomavírus. Em 1991, esta espécie foi denominada Helacyton gartleri [2].
# Referência(ENG): https://en.wikipedia.org/wiki/HeLa