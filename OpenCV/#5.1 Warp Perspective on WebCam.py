import cv2
import numpy as np

# Turn on Laptop's webcam
cap = cv2.VideoCapture(0)

while True:

    success, frame = cap.read()

    # Step 1: Define 4 corner points
    pts1 = np.float32([[0, 260], [640, 260], [0, 400], [640, 400]])

    # Step 2: Define location of the points
    width, height = 450, 330  # getting required size by taking care of height & width ratio of Output video
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

    # Step 3: Make matrix
    matrix = cv2.getPerspectiveTransform(pts1, pts2)

    # Step 4: Get Output image based on the above matrix
    vidOutput = cv2.warpPerspective(frame, matrix, (width, height))

    cv2.imshow('frame', frame)  # Inital Capture
    cv2.imshow('frame1', vidOutput)  # Transformed Capture

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
