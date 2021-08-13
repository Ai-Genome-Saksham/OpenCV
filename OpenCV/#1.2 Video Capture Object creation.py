import cv2

      # Use cv2. VideoCapture( ) to get a video capture object for the camera
vid = cv2.VideoCapture("Resources/vid1.mp4")

      # Video is just fast moving images
      # Success variable is a boolean: true or false... it will tell us whether it was successfull or not
while True:
    success, img = vid.read()
    cv2.imshow("Output",img)
    if cv2.waitKey(32) & 0xFF == ord('q'):
        break
             # cv2.waitkey(1) adds delay
             # 0xFF breaks video when 'q' pressed, any other button or pressing 'cross' symbol won't break

# When everything done, release the video capture object
vid.release()
# Closes all the frames
cv2.destroyAllWindows()

