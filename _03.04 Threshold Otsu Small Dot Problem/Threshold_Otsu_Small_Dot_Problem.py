import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import sys
from pathlib import Path

path = Path(sys.path[0])
caminhoImagem = str(path.parent.absolute()) + '\\Anexos, Imagens e Videos\\Fig1041(a)(septagon_small_noisy_mean_0_stdv_10).tif'

img = cv.imread(caminhoImagem, 0)

# Otsu's thresholding no filtering 
ret,th1 = cv.threshold(img, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)

# Otsu's thresholding after Blur filtering
blur = cv.blur(img,(5,5))
ret,th2 = cv.threshold(blur, 0, 255,cv.THRESH_BINARY+cv.THRESH_OTSU)

# teste ...
sobelx = cv.Sobel(src=img, ddepth=cv.CV_64F, dx=1, dy=0) 
sobely = cv.Sobel(src=img, ddepth=cv.CV_64F, dx=0, dy=1)
# compute the gradient magnitude and orientation
magnitude = np.sqrt((sobelx ** 2) + (sobely ** 2))
#filtered_image = np.where(magnitude > np.percentile(magnitude, 99.7), magnitude, 0)
limiar_percentil = np.percentile(magnitude, 99.7)
ret,mascara = cv.threshold(magnitude,limiar_percentil,255,cv.THRESH_BINARY)

print(mascara.shape)

#produto = img * np.uint8(mascara)
produto = cv.multiply(img, np.uint8(mascara))

cv.imwrite('teste.png',produto)

ret,th3 = cv.threshold(produto, 0, 255,cv.THRESH_BINARY+cv.THRESH_OTSU)

# plot all the images and their histograms
images = [img,  0, th1,
          blur, 0, th2,
          produto, 0, th3]

titles = ['Original Noisy Image(a)','Histogram(b)',"Otsu's Thresholding(c)",
          'Blured Noisy Image(d)','Histogram(e)',"Otsu's Thresholding(f)",
          'Magnitude Gradiente(g)','Histogram(h)',"Otsu's Thresholding(i)"]

plt.rcParams.update({'axes.titlesize': 6})

for i in range(3):
    plt.subplot(4,3,i*3+1),plt.imshow(images[i*3],'gray')
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
    plt.subplot(4,3,i*3+2),plt.hist(images[i*3].ravel(),256)
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
    plt.subplot(4,3,i*3+3),plt.imshow(images[i*3+2],'gray')
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
plt.show()