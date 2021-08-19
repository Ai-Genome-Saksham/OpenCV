import cv2
import os
import glob

original = cv2.imread("E:\my Computer Vision\OpenCV\Resources/pic1.jpg")

b, g, r = cv2.split(original)

cv2.imshow("Blue Channel", b)

cv2.imshow("Green Channel", g)

cv2.imshow("Red Channel", r)


merged = cv2.merge((b,g,r))
cv2.imshow("Merged Image", merged)
cv2.waitKey(0)