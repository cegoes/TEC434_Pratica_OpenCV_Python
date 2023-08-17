# sudo apt-get install tesseract-ocr libtesseract-dev
# sudo pip install pytesseract

import cv2
import numpy as np
import pytesseract
from pathlib import Path

def rgb2cmyk(src):  
    cmyk = []
    for i in range(4):
        cmyk.append(np.zeros(src.shape[:2], dtype=np.float32))

    r = src[:,:,2] / 255.
    g = src[:,:,1] / 255.
    b = src[:,:,0] / 255.
    k = 1 - np.max([r,g,b], axis=0)

    cmyk[0] = np.divide((1 - r - k), (1 - k), out=np.zeros_like(r), where=(1-k)!=0)
    cmyk[1] = np.divide((1 - g - k), (1 - k), out=np.zeros_like(r), where=(1-k)!=0)
    cmyk[2] = np.divide((1 - b - k), (1 - k), out=np.zeros_like(r), where=(1-k)!=0)
    cmyk[3] = k

    return cmyk

def main():
    caminho = Path('Anexos, Imagens e Videos/scratchcard.png')
    im0 = cv2.imread(str(caminho))
    if im0 is None:
        return -1

    cmyk = rgb2cmyk(im0)

    im1 = (cmyk[3] * (1 - cmyk[1])) > 0.25
    im2 = np.uint8(im1)

    contours, _ = cv2.findContours(im2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    max_area = 0
    max_idx = 0
    for i in range(len(contours)):
        area = cv2.contourArea(contours[i])
        max_idx = i if area > max_area else max_idx
        max_area = area if area > max_area else max_area

    im2.fill(0)
    cv2.drawContours(im2, contours, max_idx, 255, -1)

    im3 = cv2.cvtColor(im0, cv2.COLOR_BGR2GRAY) 
    im3 = (255 - im3)
    im3 = np.bitwise_and(im3,im2)
    im3 = cv2.threshold(im3,200,255,cv2.THRESH_BINARY)[1]
  
    dst = im3.copy()

    contours, _ = cv2.findContours(dst, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for i in range(len(contours)):
        if cv2.contourArea(contours[i]) < 100:
            cv2.drawContours(dst, contours, i, 0, -1)
    dst = ~dst
    out = pytesseract.image_to_string(dst, config='--psm 11 digits --oem 3')

    print("Texto detectado: " + out)

    cv2.imshow("src", im0)
    cv2.imshow("dst", dst)
    cv2.waitKey()
    return 0

if __name__ == "__main__":
    main()