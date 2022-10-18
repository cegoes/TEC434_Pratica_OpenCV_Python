import cv2 as cv
import dlib
import numpy as np
from pathlib import Path

DETECTOR = dlib.get_frontal_face_detector()
PREDICTOR = dlib.shape_predictor('11.03 FaceMorph/shape_predictor_68_face_landmarks.dat')

def get_landmarks(im):
	rects = DETECTOR(im, 1)
	if len(rects) > 1:
		raise Exception('Too many faces')
	if len(rects) == 0:
		raise Exception('Not enough faces')

	return np.array([[p.x, p.y] for p in PREDICTOR(im,rects[0]).parts()])

def transformation_from_points(points1, points2):
	"""Return a transformation that maps points1 into points2."""
	points1 = points1.astype(np.float64)
	points2 = points2.astype(np.float64)

	c1 = np.mean(points1, axis=0)
	c2 = np.mean(points2, axis=0)
	points1 -= c1
	points2 -= c2

	s1 = np.std(points1)
	s2 = np.std(points2)
	points1 /= s1
	points2 /= s2

	U,S,Vt=np.linalg.svd(points1.T @ points2)

	R= (U @ Vt).T

	return np.hstack([(s2/s1) * R, 
		(c2.T - (s2/s1) * R @ c1.T)[:,None]])

def create_mask(points, shape, face_scale):

	groups = [
		[17,18,19,20,21,22,23,24,25,26,36,37,38,39,40,41,42,43,44,45,46,47],
		[27,28,29,30,31,32,33,34,48,49,50,51,52,53,54,55,56,57,58,59,60]]
	mask_im = np.zeros(shape,dtype=np.float64)
	for group in groups:
		cv.fillConvexPoly(mask_im,
			cv.convexHull(body_points[group]),
			color=(1,1,1))

	feather_amount = int(0.2*face_scale*0.5)*2+1
	kernel_size=(feather_amount,feather_amount)
	mask_im = (cv.GaussianBlur(mask_im,kernel_size,0)>0)*1.0
	mask_im = cv.GaussianBlur(mask_im,kernel_size,0)

	return mask_im

def correct_colours(warped_face_im, body_im,face_scale):
	blur_amount = int(3*0.5*face_scale)*2+1
	kernel_size = (blur_amount,blur_amount)
	
	face_im_blur = cv.GaussianBlur(warped_face_im,kernel_size,0)
	body_im_blur = cv.GaussianBlur(body_im,kernel_size,0)
	
	return np.clip(0. + body_im_blur + warped_face_im - face_im_blur,0,255)

face_im = cv.imread(str(Path('11.03 FaceMorph/bush.jpg')))
body_im = cv.imread(str(Path('11.03 FaceMorph/obama.jpg')))

face_points = get_landmarks(face_im)
body_points = get_landmarks(body_im)

M = transformation_from_points(face_points,body_points)
warped_face_im = cv.warpAffine(face_im,M,(body_im.shape[1],body_im.shape[0]))

face_scale = np.std(body_points)
corrected_face_im = correct_colours(warped_face_im, body_im, face_scale)

mask_im = create_mask(body_points, body_im.shape, face_scale)
combined_im = (corrected_face_im * mask_im + body_im * (1-mask_im))

cv.imshow('Imagem 1', face_im)
cv.imshow('Imagem 2', body_im)


cv.imshow('Final', np.uint8(combined_im))
cv.waitKey()