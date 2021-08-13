import cv2
import numpy as np

#grayscale image
img = np.zeros((512,512))

print(img.shape)

# Adding color functionality and making above pic blue
img2 = np.zeros((512,512,3), np.uint8)
#img2[200:300,100:300] = 255,0,0 # taking a part of image
img2[:] = 255,0,0 # coloring whole of image

# Adding a line
img3 = np.zeros((512,512,3), np.uint8)
img3 = cv2.line(img3,(0,0),(300,300),(0,255,0), 3) # img, start pt, end pt, color, thickness
# Making the line complete
img4 = np.zeros((512,512,3), np.uint8)
img4 = cv2.line(img4,(0,0),(img4.shape[1],img4.shape[0]),(0,255,0),3) # width & height of img4

# Rectangle
img5 = cv2.line(img4,(0,0),(img4.shape[1],img4.shape[0]),(0,255,0),3)
img5 = cv2.rectangle(img5,(0,0),(250,350),(0,0,255),2)

# Circle
img6= cv2.circle(img,(400,60),35,(255,0,255),6)

# Putting Text
img7 = cv2.putText(img,"Hello World",(300,100),cv2.FONT_HERSHEY_COMPLEX,2,(250,200,100),3)

cv2.imshow("Image",img)
cv2.imshow("Image 2",img2)
cv2.imshow("Image 3",img3)
cv2.imshow("Image 4",img4)
cv2.imshow("Image 5",img5)
cv2.imshow("Image 6",img6)
cv2.imshow("Image 7",img7)

cv2.waitKey(0)