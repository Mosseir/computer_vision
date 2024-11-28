import cv2

# Initialize the video capture object (default camera is 0)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Unable to access the camera.")
else:
    print("Press 'q' to quit the camera feed.")

# Capture frames in a loop
while True:
    ret, frame = cap.read()  # Read a frame from the camera
    if not ret:
        print("Error: Unable to read from camera.")
        break

    # Display the frame in a window
    cv2.imshow('Real-Time Camera Feed', frame)

    # Wait for 'q' key to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
