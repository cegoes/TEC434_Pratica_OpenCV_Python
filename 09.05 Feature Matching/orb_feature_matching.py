import cv2 as cv
from matplotlib import pyplot as plt
from pathlib import Path

img1 = cv.imread(str(Path('Feature Matching/box.png')),0)          # queryImage
img2 = cv.imread(str(Path('Feature Matching/box_in_scene.png')),0) # trainImage

# Initiate SIFT detector
orb = cv.ORB_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

# create BFMatcher object
bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)

# Match descriptors.
matches = bf.match(des1,des2)

# Sort them in the order of their distance.
matches = sorted(matches, key = lambda x:x.distance)

# Draw first 10 matches.
img3 = cv.drawMatches(img1,kp1,img2,kp2,matches[:10], outImg=None,flags=2)

plt.imshow(img3),plt.show()