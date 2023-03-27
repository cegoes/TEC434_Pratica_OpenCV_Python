import cv2

cameraCapture = cv2.VideoCapture(0)
cv2.namedWindow('Mostra webCam')

while cameraCapture.isOpened() and cv2.waitKey(1) == -1:
    sucess, frame = cameraCapture.read()    
    cv2.imshow('Mostra webCam', frame)
    
cv2.destroyAllWindows()

cameraCapture.release()
