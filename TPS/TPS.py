import cv2
import numpy as np
from pathlib import Path
import GridImagem

caminhoImagem = Path('Anexos, Imagens e Videos/len_std.png')

if __name__ == "__main__":

    img = cv2.imread(str(caminhoImagem))
    print(img.shape)
    tps = cv2.createThinPlateSplineShapeTransformer()
    rows, cols, _ = img.shape

    gd = GridImagem.GridImagem() 
    sourcePointsb = gd.calculaPontosImagem(img)
    targetPointsb = gd.calculaPontosImagem(img)

    # mudando as coordenadas de um dos pontos para distorcer
    targetPointsb[0] = (150,150)
    #targetPointsb[1] = (55,170)

    sourcePoints = np.array(sourcePointsb,
                            np.float32)
    targetPoints = np.array(targetPointsb,
                            np.float32)
   
    sourcePoints=sourcePoints.reshape(-1,len(sourcePoints),2)
    targetPoints=targetPoints.reshape(-1,len(targetPoints),2)

    matches = list()

    for i in range(0,len(sourcePoints[0])):
        matches.append(cv2.DMatch(i,i,0))

    tps.estimateTransformation(targetPoints, sourcePoints, matches)

    out_img = tps.warpImage(img)

    cv2.imshow("Original", img)

    gd.mostraPontosImagem(out_img,targetPointsb)

    cv2.imshow("Distorção", out_img)

    cv2.waitKey()