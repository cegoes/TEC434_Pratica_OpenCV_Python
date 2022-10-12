import cv2 as cv
from matplotlib import pyplot as plt
from pathlib import Path

img1 = cv.imread(str(Path('Feature Matching/box.png')),0)          # queryImage
img2 = cv.imread(str(Path('Feature Matching/box_in_scene.png')),0) # trainImage

# Initiate SIFT detector
sift = cv.SIFT_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)

# BFMatcher with default params
bf = cv.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)

# Apply ratio test
good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])

# cv.drawMatchesKnn expects list of lists as matches.
img3 = cv.drawMatchesKnn(img1,kp1,img2,kp2,good,outImg=None,flags=2)

plt.imshow(img3),plt.show()
