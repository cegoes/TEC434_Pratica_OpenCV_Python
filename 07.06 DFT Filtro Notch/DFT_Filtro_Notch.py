import cv2 as cv
import numpy as np
import sys
from pathlib import Path

def computeDFT(image):
    planes = [np.float32(image), np.zeros(image.shape[:2], np.float32)]
    # create a complex matrix
    complex = cv.merge(planes)
    cv.dft(complex, complex, cv.DFT_COMPLEX_OUTPUT);  # fourier transform
    return complex

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

def shift(magI):
    return np.fft.fftshift(magI)

def filtroNotch(complex, caminho):
    mask = cv.imread(caminho + "\\DFT Filtros\\Clown FFT2.png", cv.IMREAD_GRAYSCALE)

    if mask is None:
        print('Falha ao abrir a imagem do filtro notch...')
        exit()

    cv.imshow('Filtro Notch', mask)

    mask = cv.resize(mask,complex.shape[:2])
    cv.normalize(mask, mask, 0, 1, cv.NORM_MINMAX)
    mask = np.float32(mask)
    mask = shift(mask.copy()) # rearrange quadrants of mask

    planes = [
        np.zeros(complex.shape[:2], np.float32),
        np.zeros(complex.shape[:2], np.float32)]

    planes[0] = mask; # real
    planes[1] = mask; # imaginar
    kernel_spec = cv.merge(planes)

    complex = cv.mulSpectrums(complex, kernel_spec, flags=cv.DFT_ROWS) #only DFT_ROWS flag is accepted    
    return complex

def updateResult(complex):
    result = cv.idft(complex)
    # equivalent to:
    # dft(complex, result, DFT_INVERSE + DFT_SCALE)
    planes = [
        np.zeros(complex.shape[:2], np.float32),
        np.zeros(complex.shape[:2], np.float32)]

    planes = cv.split(result); # planes[0] = Re(DFT(I)), planes[1] = Im(DFT(I))
    result = cv.magnitude(planes[0], planes[1]); # sqrt(Re(DFT(I))^2 + Im(DFT(I))^2)
    cv.normalize(result, result,0, 255, cv.NORM_MINMAX)
    result = np.uint8(result)
    return result

def main():
    path = Path(sys.path[0])
    caminhoImagem = str(path.parent.absolute()) + '\\Anexos, Imagens e Videos'

    imagem = cv.imread(caminhoImagem + '\\Clown.jpg', cv.IMREAD_GRAYSCALE)
    if( imagem is None):
        print('Falha ao abrir a imagem de entrada...')
        exit()

    cv.namedWindow("Imagem Original")
    cv.imshow("Imagem Original", imagem)
    cv.namedWindow("Filtro Notch")
    cv.namedWindow("Espectro")
    cv.namedWindow("Espectro Filtro Notch")
    cv.namedWindow("Resultado")

    dftImagem = computeDFT(imagem)
    cv.imshow('Espectro', updateMag(dftImagem))
    dftImagem = filtroNotch(dftImagem.copy(), caminhoImagem)
    cv.imshow('Espectro Filtro Notch', updateMag(dftImagem))
    cv.imshow('Resultado', updateResult(dftImagem))

    cv.waitKey(0)

if __name__ == "__main__":
    main()