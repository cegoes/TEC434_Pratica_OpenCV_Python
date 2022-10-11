import cv2 as cv
import numpy as np
from pathlib import Path

if __name__ == '__main__' :

     # Read destination image.
     im_dst = cv.imread(str(Path('Perspective Homography/KkQ9B.jpg')))
     pts_dst = np.array([[314, 107], [693, 107], [903, 493],[311, 491]])

     # Read source image.
     im_src = cv.imread(str(Path('Perspective Homography/pitch.jpg')))
     pts_src = np.array([[487, 81],[575, 81],[575, 297],[487, 297]])

     # Calculate Homography
     h, status = cv.findHomography(pts_src, pts_dst)

     # Warp source image to destination based on homography
     im_out = cv.warpPerspective(im_src, h, (im_dst.shape[1],im_dst.shape[0]), borderValue=[255,255,255])
     mask = im_out[:,:,0] < 100
     cv.imshow("mask Image", np.uint8(mask))
     im_out_overlapped = im_dst.copy()
     im_out_overlapped[mask] = [0,0,255]
     # Display images
     cv.imshow("Source Image", im_src)
     cv.imshow("Destination Image", im_dst)
     cv.imshow("Warped Source Image", im_out)
     cv.imshow("Warped", im_out_overlapped)
     cv.waitKey(0)