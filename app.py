import opencv as cv2
import numpy as np
import urllib.request

# Set up the IP address and port for the video stream
url = "http://127.0.0.1:8080/shot.jpg"

# Open the EpocCam app on the iPhone and make sure it's connected to the same WiFi network as the computer

# Start capturing video from the iPhone camera
cap = cv2.VideoCapture(url)

# Loop through the video frames and display them
while True:
    # Read the frame from the video stream
    ret, frame = cap.read()

    # If the frame is not available, break out of the loop
    if not ret:
        break

    # Display the frame in a window
    cv2.imshow("iPhone Camera", frame)

    # Wait for a key press and exit if the 'q' key is pressed
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

# Release the video capture object and destroy the window
cap.release()
cv2.destroyAllWindows()

