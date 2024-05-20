import cv2 as cv
from scipy import ndimage as ndi
import numpy as np
from matplotlib import pyplot as plt

def invert_map(F: np.ndarray):
    I = np.zeros_like(F)
    I[:,:,1], I[:,:,0] = np.indices(sh)
    P = np.copy(I)
    for i in range(10):
        P += I - cv.remap(F, P, None, interpolation=cv.INTER_LINEAR)
    return P

# Simulate deformation field
N = 500
sh = (N, N)
t = np.random.normal(size=sh)
dx = ndi.gaussian_filter(t, 40, order=(0,1))
dy = ndi.gaussian_filter(t, 40, order=(1,0))
dx *= 10/dx.max()
dy *= 10/dy.max()

# Test image
img = np.zeros(sh)
img[::10, :] = 1
img[:, ::10] = 1
img = ndi.gaussian_filter(img, 0.5)

# Apply forward mapping
yy, xx = np.indices(sh)
xmap = (xx-dx).astype(np.float32)
ymap = (yy-dy).astype(np.float32)
warped = cv.remap(img, xmap, ymap ,cv.INTER_LINEAR)
plt.imshow(warped,cmap='gray')
plt.title('warped')
plt.show()

# F: The function to invert
F = np.zeros((sh[0], sh[1], 2), dtype=np.float32)
F[:,:,0], F[:,:,1] = (xmap, ymap)

# Test the prediction
unwarped = cv.remap(warped, invert_map(F), None, cv.INTER_LINEAR)
plt.imshow(unwarped, cmap='gray')
plt.show()