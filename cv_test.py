import time
import picamera
import numpy as np
import cv2

# Initialize the camera
with picamera.PiCamera() as camera:
    # Set camera resolution (adjust as needed)
    camera.resolution = (640, 480)
    camera.framerate = 30

    # Create a stream for capturing images
    stream = np.empty((camera.resolution[1], camera.resolution[0], 3), dtype=np.uint8)

    # Capture frames continuously
    while True:
        # Capture a frame into the stream
        camera.capture(stream, 'rgb')

        # Process the frame (example: convert to grayscale)
        processed_frame = cv2.cvtColor(stream, cv2.COLOR_RGB2GRAY)

        # Display the processed frame (you may want to use a GUI library or write to a file)
        cv2.imshow('Processed Frame', processed_frame)
        cv2.waitKey(1)  # Add a small delay to avoid high CPU usage

cv2.destroyAllWindows()
