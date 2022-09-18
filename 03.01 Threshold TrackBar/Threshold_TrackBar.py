import cv2 as cv
import numpy as np
from pathlib import Path

# Global variables
src = np.array
src_gray  = np.array
dst = np.array
threshold_value = 0
threshold_type = 3
MAX_VALUE = 255
MAX_TYPE = 4
MAX_BINARY_VALUE = 255

window_name = "Threshold Demo"

trackbar_type = "Tipo: \n 0: Binary \n 1: Binary Inverted \n 2: Truncate \n 3: To Zero \n 4: To Zero Inverted"
trackbar_value = "Valor"

def Threshold_Demo(val):
  ''' 
  0: Binary
  1: Binary Inverted
  2: Threshold Truncated
  3: Threshold to Zero
  4: Threshold to Zero Inverted
  '''
  threshold_type = cv.getTrackbarPos(trackbar_type, window_name)
  threshold_value = cv.getTrackbarPos(trackbar_value, window_name)
  _, dst = cv.threshold( src_gray, threshold_value, MAX_BINARY_VALUE, threshold_type )
  cv.imshow( window_name, dst )

if __name__ == '__main__':
  caminhoImagem = Path('Anexos, Imagens e Videos/len_std.png')

  # Carrega a imagem
  src = cv.imread( str(caminhoImagem) )

   # Converte para Cinza
  src_gray = cv.cvtColor( src, cv.COLOR_BGR2GRAY)

  # Cria uma janela para mostrar os resultados
  cv.namedWindow( window_name, cv.WINDOW_GUI_EXPANDED )

  # Cria um Trackbar para escolher o tipo do Threshold
  cv.createTrackbar( trackbar_type,
                window_name, 3,
                MAX_TYPE, Threshold_Demo )

  # Cria um Trackbar para escolher o valor do Threshold
  cv.createTrackbar( trackbar_value,
                window_name, 0,
                MAX_VALUE, Threshold_Demo )

  # Chama a função para inicializar
  Threshold_Demo(0)

  cv.waitKey(0)



