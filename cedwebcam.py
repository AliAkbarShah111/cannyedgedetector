import cv2
import numpy as np

def main():
    # Open the default camera (usually the built-in webcam)
    cap = cv2.VideoCapture(0)

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error opening the camera.")
        return

    while True:
        # Capture a frame from the camera
        ret, frame = cap.read()

        # Check if the frame is captured successfully
        if not ret:
            print("Error capturing the frame.")
            break

        # Convert the frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply Canny Edge Detection
        edges = cv2.Canny(gray_frame, 50, 150)

        # Display the original frame and the edges side-by-side
        combined = np.hstack((frame, cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)))
        cv2.imshow("Canny Edge Detection", combined)

        # Exit the loop when the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
