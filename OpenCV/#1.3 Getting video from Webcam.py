import cv2

cap = cv2.VideoCapture(0) # using default camera, if more than 1, add ID
cap.set(3,640) # width is id no 3
cap.set(4,480) # height is id no 4
cap.set(10,100) # Brightness id is 10
while True:
    success, img = cap.read()
    cv2.imshow("Output",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
