'''
 * Program to detect pupil, based on
 * http://www.codeproject.com/Articles/137623/Pupil-or-Eyeball-Detection-and-Extraction-by-C-fro
 * with some improvements.
'''

import cv2
import math
from pathlib import Path

caminhoImagem = Path('Anexos, Imagens e Videos/eye_image.jpg')

# Load image
src = cv2.imread(str(caminhoImagem))
if src.shape[0] == 0:
    exit()

# Invert the source image and convert to grayscale
gray = cv2.cvtColor(~src, cv2.COLOR_BGR2GRAY)

# Convert to binary image by thresholding it
_, gray = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY)

# Find all contours
contours, _ = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Fill holes in each contour
cv2.drawContours(gray, contours, -1, (255,255,255), -1)

for i in range(len(contours)):
    area = cv2.contourArea(contours[i])
    rect = cv2.boundingRect(contours[i])
    radius = rect[2] / 2

    # If contour is big enough and has round shape
    # Then it is the pupil
    if area >= 30 and abs(1 - (rect[2] / rect[3])) <= 0.2 and abs(1 - (area / (math.pi * math.pow(radius, 2)))) <= 0.2:
        centro = (int(rect[0] + radius), int(rect[1] + radius))

        cv2.circle(src, centro, int(radius), (255,0,0), 2)

cv2.imshow("image", src)
cv2.waitKey(0)