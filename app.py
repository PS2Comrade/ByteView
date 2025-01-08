import cv2

# URL of the video
video_url = 'https://bitview.net/videos/22XAsGKsHZsJ9WL58wHb.mp4'

# Create a VideoCapture object
cap = cv2.VideoCapture(video_url)

# Check if the video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Read and display the video frames
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Display the frame
    cv2.imshow('Video', frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close the display window
cap.release()
cv2.destroyAllWindows()
