import cv2
import numpy as np

# Create two video capture objects for left and right cameras (adjust device IDs as needed)
left_camera = cv2.VideoCapture(0)
right_camera = cv2.VideoCapture(1)

# Set camera resolution (adjust as needed)
width = 640
height = 480
left_camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
left_camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
right_camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
right_camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

# Load stereo calibration data (you need to calibrate your stereo camera setup first)
stereo_calibration_file = "stereo_calibration.yml"
calibration_data = cv2.FileStorage(stereo_calibration_file, cv2.FILE_STORAGE_READ)

if not calibration_data.isOpened():
    print("Calibration file not found.")
    exit()

camera_matrix_left = calibration_data.getNode("cameraMatrixLeft").mat()
camera_matrix_right = calibration_data.getNode("cameraMatrixRight").mat()
distortion_coeff_left = calibration_data.getNode("distCoeffsLeft").mat()
distortion_coeff_right = calibration_data.getNode("distCoeffsRight").mat()
R = calibration_data.getNode("R").mat()
T = calibration_data.getNode("T").mat()

calibration_data.release()

# Create stereo rectification maps
R1, R2, P1, P2, Q, _, _ = cv2.stereoRectify(
    camera_matrix_left, distortion_coeff_left,
    camera_matrix_right, distortion_coeff_right,
    (width, height), R, T
    )

left_map1, left_map2 = cv2.initUndistortRectifyMap(
    camera_matrix_left, distortion_coeff_left, R1, P1, (width, height), cv2.CV_32FC1
    )
right_map1, right_map2 = cv2.initUndistortRectifyMap(
    camera_matrix_right, distortion_coeff_right, R2, P2, (width, height), cv2.CV_32FC1
    )

while True:
    # Capture frames from left and right cameras
    ret1, left_frame = left_camera.read()
    ret2, right_frame = right_camera.read()

    if not ret1 or not ret2:
        print("Failed to capture frames.")
        break

    # Undistort and rectify frames
    left_frame_rectified = cv2.remap(left_frame, left_map1, left_map2, interpolation=cv2.INTER_LINEAR)
    right_frame_rectified = cv2.remap(right_frame, right_map1, right_map2, interpolation=cv2.INTER_LINEAR)

    # Convert frames to grayscale
    left_gray = cv2.cvtColor(left_frame_rectified, cv2.COLOR_BGR2GRAY)
    right_gray = cv2.cvtColor(right_frame_rectified, cv2.COLOR_BGR2GRAY)

    # Perform stereo matching to calculate depth map (adjust parameters as needed)
    stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
    disparity = stereo.compute(left_gray, right_gray)

    # Normalize the disparity map for visualization
    disparity_normalized = cv2.normalize(disparity, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

    # Display the disparity map
    cv2.imshow("Disparity Map", disparity_normalized)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release resources
left_camera.release()
right_camera.release()
cv2.destroyAllWindows()