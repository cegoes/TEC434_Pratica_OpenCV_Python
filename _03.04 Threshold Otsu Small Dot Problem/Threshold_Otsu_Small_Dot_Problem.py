import cv2 as cv
from matplotlib import pyplot as plt
import sys
from pathlib import Path



path = Path(sys.path[0])
caminhoImagem = str(path.parent.absolute()) + '\\Anexos, Imagens e Videos\\Fig1041(a)(septagon_small_noisy_mean_0_stdv_10).tif'

img = cv.imread(caminhoImagem, 0)
# Otsu's thresholding
ret2,th1 = cv.threshold(img, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
# Otsu's thresholding after Gaussian filtering
blur = cv.blur(img,(5,5))
ret2,th2 = cv.threshold(blur, 0, 255,cv.THRESH_BINARY+cv.THRESH_OTSU)
# plot all the images and their histograms

lblur = cv.Laplacian(blur, cv.CV_8U, ksize=5)

images = [img,  0, th1,
          blur, 0, th2,
          lblur, 0, th2,
          blur, 0, th2]
titles = ['Original Noisy Image','Histogram',"Otsu's Thresholding",
          'Blured Noisy Image','Histogram',"Otsu's Thresholding",
          'Original Noisy Image','Histogram',"Otsu's Thresholding",
          'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]
for i in range(4):
    plt.subplot(4,3,i*3+1),plt.imshow(images[i*3],'gray')
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
    plt.subplot(4,3,i*3+2),plt.hist(images[i*3].ravel(),256)
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
    plt.subplot(4,3,i*3+3),plt.imshow(images[i*3+2],'gray')
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
plt.show()