import cv2

# Opens the inbuilt camera of laptop to capture video.
webCam = cv2.VideoCapture(0)
currentframe = 0

while (True):
    success, frame = webCam.read()

    # Save Frame by Frame into disk using imwrite method
    cv2.imshow("Output", frame)
    cv2.imwrite('Frame' + str(currentframe) + '.jpg', frame)
    currentframe += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


webCam.release()
cv2.destroyAllWindows()
