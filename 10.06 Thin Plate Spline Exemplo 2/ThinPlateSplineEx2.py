import cv2
import numpy as np
import random
from pathlib import Path

caminhoImagem = Path('Anexos, Imagens e Videos/liv.png')

# First read in img
img = cv2.imread(str(caminhoImagem),cv2.IMREAD_COLOR)
#img = cv2.resize(img,(180,32))

# N pair of reference control points
N=5
points=[]
dx=int(180/(N-1))
for i in range(2*N):
    points.append((dx*i,4))
    points.append((dx*i,36))

# Draw a green circle
for point in points:
    cv2.circle(img, point, 1, (0, 255, 0), 2)
    
cv2.imshow('Original',img)

# Widen a circle around
img = cv2.copyMakeBorder(img,4,4,0,0,cv2.BORDER_REPLICATE)


tps = cv2.createThinPlateSplineShapeTransformer()

sourceshape = np.array(points,np.int32)
sourceshape=sourceshape.reshape(1,-1,2)

matches =[]
for i in range(1,N+1):
    matches.append(cv2.DMatch(i,i,0))

# Start random changes
newpoints=[]
PADDINGSIZ=10
for i in range(N):
    nx=points[i][0]+random.randint(0,PADDINGSIZ)-PADDINGSIZ/2
    ny=points[i][1]+random.randint(0,PADDINGSIZ)-PADDINGSIZ/2
    newpoints.append((nx,ny))

#print(points,newpoints)
targetshape = np.array(newpoints,np.int32)
targetshape=targetshape.reshape(1,-1,2)
tps.estimateTransformation(sourceshape,targetshape,matches)
img=tps.warpImage(img)

cv2.imshow('Resultado',img)
#cv2.imwrite('tmp.png',img)
cv2.waitKey(0)