import numpy as np
import cv2
import matplotlib.pyplot as plt

# Step 1 read in the picture
img = cv2.imread('.\\Anexos, Imagens e Videos\\len_std.png',0)

img_float = np.float32(img)

# Step 3: Fourier transform with cv2.dft
dft = cv2.dft(img_float, flags=cv2.DFT_COMPLEX_OUTPUT)

# Step 4: use np.fft.fftshift to transfer the low frequency to the image center
dft_center = np.fft.fftshift(dft)

# Step 5: define mask: the generated mask is 1 in the middle and 0 around
crow, ccol = int(img.shape[0] / 2), int(img.shape[1] / 2) # Find the center of the image
mask = np.zeros((img.shape[0], img.shape[1], 2), np.uint8)
mask[crow-30:crow+30, ccol-30:ccol+30] = 1

# Step 6: multiply the mask with the image after Fourier transform, and keep the middle part
mask_img = dft_center * mask

# Step 7: use np.fft.ifftshift() to move the low frequency to the original position
img_idf = np.fft.ifftshift(mask_img)

# Step 8: inverse Fourier transform using cv2.idft
img_idf = cv2.idft(img_idf)

# Step 9: use cv2.magnitude to convert into space domain
img_idf = cv2.magnitude(img_idf[:, :, 0], img_idf[:, :, 1])

# Converte a matrix novamente para o tipo unsigned 8bits e ajusta a escala dos pixels
cv2.normalize(img_idf, img_idf, 0, 1, cv2.NORM_MINMAX)

cv2.imshow('Input Image',img)
cv2.imshow('Ringed Image',img_idf)

cv2.waitKey(0)