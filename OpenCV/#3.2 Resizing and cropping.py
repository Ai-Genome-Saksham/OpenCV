import cv2
import numpy as np

# read image
img = cv2.imread("Resources/pic1.jpg")

# get dimensions of image
dimensions = img.shape

# height, width, number of channels in image
height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]

print('Image Dimension    : ', dimensions)
print('Image Height       : ', height)
print('Image Width        : ', width)
print('Number of Channels : ', channels)
print('Image Shape        :',  img.shape)

# Resizing
imgResize = cv2.resize(img,(300,200)) # width comes first

# Cropping
imgCropped = img[0:200, 200:500]  # height comes first

cv2.imshow("Image", img)
cv2.imshow("Resized Image", imgResize)
cv2.imshow("Cropped Image", imgCropped)
cv2.waitKey(0)