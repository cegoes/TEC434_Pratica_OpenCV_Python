import numpy as np
import cv2 as cv
from pathlib import Path

caminhoImagem = Path('Anexos, Imagens e Videos/windmill_noise.png')

def shift(magI):
    return np.fft.fftshift(magI)

def updateMag(complex):
    magI = np.ndarray
    planes = [
        np.zeros(complex.shape[:2], np.float32),
        np.zeros(complex.shape[:2], np.float32)]
    cv.split(complex, planes); # planes[0] = Re(DFT(I)), planes[1] = Im(DFT(I))
    magI = cv.magnitude(planes[0], planes[1]); # sqrt(Re(DFT(I))^2 + Im(DFT(I))^2)
    # switch to logarithmic scale: log(1 + magnitude)
    magI += 1
    cv.log(magI, magI)
    magI = shift(magI.copy()); # rearrage quadrants
    # Transform the magnitude matrix into a viewable image (float values 0-1)
    cv.normalize(magI, magI, 1, 0, cv.NORM_INF)
    return magI

# Step 1 read in the picture
img = cv.imread(str(caminhoImagem),0)

img_float = np.float32(img)
# Step 3: Fourier transform with cv.dft
dft = cv.dft(img_float, flags=cv.DFT_COMPLEX_OUTPUT)
# Step 4: use np.fft.fftshift to transfer the low frequency to the image center
dft_center = np.fft.fftshift(dft)
# Step 5: define mask: the generated mask is 1 in the middle and 0 around

crow1, ccol1 = (225,286)
crow2, ccol2 = (225,316)
dft_center[crow1-3:crow1+3,ccol1-3:ccol1+3]=0
dft_center[crow2-3:crow2+3,ccol2-3:ccol2+3]=0
mask_img = dft_center

mask_img = shift(mask_img)
magnitude_spectrum = updateMag(mask_img)

cv.imshow('Spectro',magnitude_spectrum)
#cv.imwrite('a.tif',magnitude_spectrum)

# Step 8: inverse Fourier transform using cv.idft
img_idf = cv.idft(mask_img)

# Step 9: use cv.magnitude to convert into space domain
img_idf = cv.magnitude(img_idf[:, :, 0], img_idf[:, :, 1])

# Converte a matrix novamente para o tipo unsigned 8bits e ajusta a escala dos pixels
img_idf = np.uint8(cv.normalize(img_idf, None, 0, 255, cv.NORM_MINMAX))

cv.imshow('Input Image',img)
cv.imshow('OutPut Image',img_idf)

cv.waitKey()