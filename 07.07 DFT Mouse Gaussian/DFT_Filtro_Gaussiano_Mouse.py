import numpy as np
import cv2
from pathlib import Path

kernel_size: int = 0
complex = np.ndarray

def f(val):
    global kernel_size
    kernel_size = val

def updateResult(complex):    
    work = cv2.idft(complex)
    #dft(complex, work, DFT_INVERSE + DFT_SCALE)
    planes = [np.zeros(complex.shape[:2], np.float32), np.zeros(complex.shape[:2], np.float32)]
    cv2.split(work, planes)                # planes[0] = Re(DFT(I)), planes[1] = Im(DFT(I))

    work = cv2.magnitude(planes[0], planes[1])    # === sqrt(Re(DFT(I))^2 + Im(DFT(I))^2)
    cv2.normalize(work, work, 0, 1, cv2.NORM_MINMAX)
    cv2.imshow("result", work)

def updateMag(complex):    
    planes = [np.zeros(complex.shape[:2], np.float32), np.zeros(complex.shape[:2], np.float32)]
    planes = cv2.split(complex) # planes[0] = Re(DFT(I)), planes[1] = Im(DFT(I))

    magI = cv2.magnitude(planes[0], planes[1]) # sqrt(Re(DFT(I))^2 + Im(DFT(I))^2)

    # switch to logarithmic scale: log(1 + magnitude)
    magI += 1
    magI = cv2.log(magI)

    magI=shift(magI)
    cv2.normalize(magI, magI, 1, 0, cv2.NORM_INF) # Transform the matrix with float values into a
                                                  # viewable image form (float between values 0 and 1).
    cv2.imshow("spectrum", magI)

def computeDFT(image):
    padded = np.ndarray; # expand input image to optimal size
    rows, cols = image.shape[:2]
    m = cv2.getOptimalDFTSize( rows )
    n = cv2.getOptimalDFTSize( cols ); # on the border add zero values
    padded = cv2.copyMakeBorder(image, 0, m - rows, 0, n - cols, cv2.BORDER_CONSTANT, value=[0, 0, 0])
    planes = [np.float32(padded), np.zeros(padded.shape[:2], np.float32)]
    complex = cv2.merge(planes); # Add to the expanded another plane with zeros
    cv2.dft(complex, complex, cv2.DFT_COMPLEX_OUTPUT); # furier transform
    return complex

def createGausFilterMask(size, x: int, y: int, ksize: int, normalization: bool, invert: bool):
    width, height  = size[:2]
    # Some corrections if out of bounds
    if(x < (ksize / 2)):
        ksize = x * 2
    if(y < (ksize / 2)):
        ksize = y * 2
    if(width - x < ksize / 2 ):
        ksize = (width - x ) * 2
    if(height - y < ksize / 2 ):
        ksize = (height - y) * 2

    # call openCV gaussian kernel generator
    sigma = -1
    kernelX = cv2.getGaussianKernel(ksize, sigma, ktype=cv2.CV_32F)
    kernelY = cv2.getGaussianKernel(ksize, sigma, ktype=cv2.CV_32F)
    # create 2d gaus
    kernel = kernelX * np.transpose(kernelY)
    # create empty mask
    mask = np.zeros(size[:2], np.float32)
    maski = np.zeros(size[:2], np.float32)

    # copy kernel to mask on x,y
    xini = round(x - ksize / 2)
    xfim = xini + ksize
    yini = round(y - ksize / 2)
    yfim = yini + ksize
    mask[yini:yfim,xini:xfim] = kernel.copy()

    # create mirrored mask
    xini2 = round(( width - x) - ksize / 2)
    xfim2 = xini2 + ksize
    yini2 = round(( height - y) - ksize / 2)
    yfim2 = yini2 + ksize
    maski[yini2:yfim2,xini2:xfim2] = kernel.copy()

    # add mirrored to mask
    cv2.add(mask, maski, mask)

    # transform mask to range 0..1
    if(normalization): 
        cv2.normalize(mask, mask, 0, 1, cv2.NORM_MINMAX)
    # invert mask
    if(invert):
        mask = np.ones(mask.shape[:2], np.float32) - mask

    return mask

def shift(imgDFT):
    return np.fft.fftshift(imgDFT)

def onMouse(event, x, y, _, param):
    if( event != cv2.EVENT_LBUTTONDOWN ):
        return

    # cast *param to use it local
    global complex
        
    mask = createGausFilterMask(complex.shape, x, y, kernel_size, True, True)
    # show the kernel
    cv2.imshow("gaus-mask", mask)

    mask = shift(mask)

    planes = [np.zeros(complex.shape[:2], np.float32), np.zeros(complex.shape[:2], np.float32)]
    planes[0] = mask; # real
    planes[1] = mask; # imaginar
    kernel_spec = cv2.merge(planes)

    complex = cv2.mulSpectrums(complex, kernel_spec, flags=cv2.DFT_ROWS) # only DFT_ROWS accepted

    updateMag(complex)    # show spectrum
    updateResult(complex)      # do inverse transform

def main():
    # Step 1 read in the picture
    caminhoImagem = Path('Anexos, Imagens e Videos/Clown.jpg')
    image = cv2.imread(str(caminhoImagem), cv2.IMREAD_GRAYSCALE)    
    cv2.namedWindow('Original Image', cv2.WINDOW_GUI_EXPANDED)
    cv2.imshow('Original Image',image)
    global complex
    complex = computeDFT(image)

    cv2.namedWindow( "spectrum", cv2.WINDOW_AUTOSIZE )
    cv2.createTrackbar( "Gausian kernel size", "spectrum", 0, 255, f)
    cv2.setMouseCallback( "spectrum", onMouse)

    updateMag(complex)         # compute magnitude of complex, switch to logarithmic scale and display...
    updateResult(complex)      # do inverse transform and display the result image

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()