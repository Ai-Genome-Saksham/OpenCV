import cv2

faceCascade = cv2.CascadeClassifier("E:\my Computer Vision\OpenCV\haarcascades/haarcascade_frontalface_default.xml")

img = cv2.imread("Resources/smiling_face.jpg")

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect faces
faces = faceCascade.detectMultiScale(imgGray,1.1 , 4)
# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Image", img)
cv2.waitKey(0)