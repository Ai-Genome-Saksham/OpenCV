import cv2


img = cv2.imread("E:\my Computer Vision\OpenCV\Resources\pic1.jpg")

cv2.imshow("output",img)
cv2.waitKey(0)

# height, width, number of channels in image
height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]

print('Image Height       : ', height)
print('Image Width        : ', width)
print('Number of Channels : ', channels)

print(img.shape)

cv2.imshow("Image", img)

cv2.waitKey(0)