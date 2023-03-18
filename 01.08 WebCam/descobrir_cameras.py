import cv2

camera_index = 0
camera_list = []

while True:
    camera = cv2.VideoCapture(camera_index)
    if not camera.isOpened():
        break
    else:
        camera_list.append(camera.getBackendName())
        camera.release()
    camera_index += 1

print('Lista das Cameras...')
print(camera_list)