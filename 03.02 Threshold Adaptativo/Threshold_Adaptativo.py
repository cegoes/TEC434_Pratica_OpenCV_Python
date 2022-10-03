import cv2 as cv
from pathlib import Path

if __name__ == '__main__':
    caminhoImagem = Path('Anexos, Imagens e Videos/FiguraSombra.png')

    image = cv.imread(str(caminhoImagem), 0)
    cv.namedWindow("Imagem original")
    cv.imshow("Imagem original", image)
    image = cv.blur(image,(3,3))
    '''
    @param src Source 8-bit single-channel image.
    @param dst Destination image of the same size and the same type as src.
    @param maxValue Non-zero value assigned to the pixels for which the condition is satisfied
    @param adaptiveMethod Adaptive thresholding algorithm to use, see #AdaptiveThresholdTypes. The #BORDER_REPLICATE | #BORDER_ISOLATED is used to process boundaries.
    @param thresholdType Thresholding type that must be either #THRESH_BINARY or #THRESH_BINARY_INV, see #ThresholdTypes.
    @param blockSize Size of a pixel neighborhood that is used to calculate a threshold value for the pixel: 3, 5, 7, and so on.
    @param C Constant subtracted from the mean or weighted mean (see the details below). Normally, it is positive but may be zero or negative as well.
    '''
    thresholdadap = cv.adaptiveThreshold(image, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 45, -3)
    cv.namedWindow('Resultado threshold adaptativo')
    cv.imshow('Resultado threshold adaptativo', thresholdadap)
    _, thresholdnormal = cv.threshold(image, 25, 255, cv.THRESH_BINARY)
    cv.namedWindow('Resultado threshold')
    cv.imshow('Resultado threshold', thresholdnormal)
    cv.waitKey(0)