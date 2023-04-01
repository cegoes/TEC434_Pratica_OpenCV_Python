# TechVidvan Human pose estimator
# import necessary packages
# pip install mediapipe
# Se NÂO tiver gpu nvidia: pip install tensorflow-cpu
# Se tiver gpu nvidia: pip install tensorflow

import cv2
import mediapipe as mp
from pathlib import Path
import numpy as np

# initialize Pose estimator
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

pose = mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)

# create capture object
caminho = Path('Anexos, Imagens e Videos/dance.mp4')
cap = cv2.VideoCapture(str(caminho))

frame = np.ndarray

while cap.isOpened():
    # read frame from capture object
    _,frame = cap.read()    
    try:
        # convert the frame to RGB format
        RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # process the RGB frame to get the result
        results = pose.process(RGB)

        print(results.pose_landmarks)
        # draw detected skeleton on the frame
        mp_drawing.draw_landmarks(
            frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # show the final output
        cv2.imshow('Output', frame)
    except:
        break
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
