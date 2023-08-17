import cv2
import numpy as np
from pathlib import Path

im = cv2.imread(str(Path('10.15 Multiplo Corretor de Perspectiva/6b1u2.jpg')))
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (1, 1), 1000)
flag, thresh = cv2.threshold(blur, 120, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)

contourns_to_draw = []

# filter the cards contour
for i in range(len(contours)):
    card = contours[i]
    peri = cv2.arcLength(card, True)
    if peri > 800:
        contourns_to_draw.append(card)

img = cv2.drawContours(im, contourns_to_draw, -1, (0, 255, 0), 3)
cv2.imshow("Show Boxes", img)
key = cv2.waitKey(0) & 0xFF

# Should create a new image by the given card contour ( NOT WORK )
for i, contour in enumerate(contourns_to_draw):

    peri = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.02 * peri, True)
    rect = cv2.minAreaRect(contour)
    r = cv2.boxPoints(rect)

    h = np.array([[0, 0], [449, 0], [449, 449], [0, 449]], np.float32)
    #transform = cv2.getPerspectiveTransform(approx, h)
    transform = cv2.getPerspectiveTransform(approx.astype(np.float32), h)
    warp = cv2.warpPerspective(im, transform, (450, 450))


    cv2.imshow("Show Boxes", warp)
    key = cv2.waitKey(0) & 0xFF
    if key == 27:
        break
cv2.destroyAllWindows()
