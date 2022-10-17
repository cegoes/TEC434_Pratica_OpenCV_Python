import cv2 as cv
import numpy as np
from pathlib import Path

caminho = Path('Automatic Perspective Correction/kMNcG.jpg')
src = cv.imread(str(caminho))
thr = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
ret, thr = cv.threshold( thr, 70, 255, cv.THRESH_BINARY )

largest_contour_index: int = 0
largest_area: int = 0

rows, cols, _ = src.shape
dst = np.zeros((rows,cols), np.uint8) #create destination image
contours, hierarchy = cv.findContours( thr.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE ) # Find the contours in the image

for i in range(len(contours)):
    a = cv.contourArea(contours[i], False)
    if (a > largest_area):
        largest_area = a
        largest_contour_index = i;                #Store the index of largest contour

cv.drawContours( dst,contours, largest_contour_index, (255,255,255), cv.FILLED, 8, hierarchy )
contours_poly = cv.approxPolyDP( contours[largest_contour_index], 5, True )
(x,y,width,heigth) = cv.boundingRect(contours[largest_contour_index])

if(len(contours_poly)==4):
    quad_pts = np.float32(contours_poly)
    P1 = contours_poly[0]
    P2 = contours_poly[1]
    P3 = contours_poly[2]
    P4 = contours_poly[3]

    PA = [0,0]
    PB = [width,0]
    PC = [width,heigth]
    PD = [0,heigth]

    squre_pts = np.float32([PA, PD, PC, PB])

    transmtx = cv.getPerspectiveTransform(quad_pts,squre_pts)
    transformed = cv.warpPerspective(src, transmtx, (width, heigth))

    cv.line(src,P1[0],P2[0], (0,0,255), 1, cv.LINE_AA, 0)
    cv.line(src,P2[0],P3[0], (0,0,255), 1, cv.LINE_AA, 0)
    cv.line(src,P3[0],P4[0], (0,0,255), 1, cv.LINE_AA, 0)
    cv.line(src,P4[0],P1[0], (0,0,255), 1, cv.LINE_AA, 0)

    cv.imshow("Perspectiva corrigida", transformed)
    cv.imshow("Threshold", thr)
    cv.imshow("Contornos Preenchidos", dst)
    cv.imshow("Original", src)

    cv.waitKey()
else:
    print('Make sure that your are getting 4 corner using approxPolyDP...')