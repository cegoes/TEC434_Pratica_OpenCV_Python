import cv2
import numpy as np
from pathlib import Path

caminhoImagem = Path('Anexos, Imagens e Videos')

def onTrackbarChange(max_slider):
	global img
	global dst
	global gray

	dst = np.copy(img)

	th1 = max_slider 
	th2 = th1 * 0.4
	edges = cv2.Canny(img, th1, th2)

	# image	8-bit, single-channel binary source image. The image may be modified by the function.
	# lines	Output vector of lines. Each line is represented by a 4-element vector (x1,y1,x2,y2) , where (x1,y1) and (x2,y2) are the ending points of each detected line segment.
	# rho	Distance resolution of the accumulator in pixels.
	# theta	Angle resolution of the accumulator in radians.
	# threshold	Accumulator threshold parameter. Only those lines are returned that get enough votes ( >threshold ).
	# minLineLength	Minimum line length. Line segments shorter than that are rejected.
	# maxLineGap	Maximum allowed gap between points on the same line to link them.

	# Aplicando a Transformada de Hough Probabilistica
	lines = cv2.HoughLinesP(image=edges, rho=2, theta=np.pi/180.0, threshold=50, 
		minLineLength=10, maxLineGap=100)

	# Draw lines on the detected points
	for line in lines:
		x1, y1, x2, y2 = line[0]
		cv2.line(dst, (x1, y1), (x2, y2), (0,0,255), 1)

	cv2.imshow("Result Image", dst)	
	cv2.imshow("Edges",edges)

if __name__ == "__main__":
	
	# Read image
	img = cv2.imread(str(caminhoImagem / 'lanes.jpg'))
	
	# Create a copy for later usage
	dst = np.copy(img)

	# Convert image to gray
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	# Create display windows
	cv2.namedWindow("Edges")
	cv2.namedWindow("Result Image")
	  
	# Initialize threshold value
	initThresh = 500

	# Maximum threshold value
	maxThresh = 1000

	cv2.createTrackbar("threshold", "Result Image", initThresh, maxThresh, onTrackbarChange)
	onTrackbarChange(initThresh)

	while True:
		key = cv2.waitKey(1)
		if key == 27:
			break

	cv2.destroyAllWindows()