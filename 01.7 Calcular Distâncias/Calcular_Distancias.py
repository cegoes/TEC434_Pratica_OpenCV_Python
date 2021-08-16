import scipy.spatial.distance as dist
import numpy

if __name__== "__main__":
    a = numpy.array((10 , 5))
    b = numpy.array((20, 6))

    euclidiana = dist.euclidean(a, b)
    cityblock  = dist.cityblock(a, b)
    chessboard = dist.chebyshev(a, b)

    print ('Distância Euclidiana: ' + str(euclidiana) + ' pixels')
    print ('Distância City Block: ' + str(cityblock) + ' pixels')
    print ('Distância Chessboard: ' + str(chessboard) + ' pixels')