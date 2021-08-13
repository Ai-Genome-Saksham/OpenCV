import cv2

# Loading the images
img1 = cv2.imread("Resources/pic3.jpg")
img2 = cv2.imread("Resources/pic4.jpg")

# -----------------Addition of Image------------------------
# Method 1:
#  Add two images by using function cv2.add().
#  This directly adds up image pixels in the two images.
# Not appropriate.

imgFinal = cv2.add(img1, img2)
cv2.imshow("Output", imgFinal)
cv2.waitKey(0)

# Method 2:
'''
Syntax: cv2.addWeighted(img1, wt1, img2, wt2, gammaValue)

Parameters:
img1: First Input Image array(Single-channel, 8-bit or floating-point)
wt1: Weight of the first input image elements to be applied to the final image
img2: Second Input Image array(Single-channel, 8-bit or floating-point)
wt2: Weight of the second input image elements to be applied to the final image
gammaValue: Measurement of light
'''

# cv2.addWeighted is applied over the
# image inputs with applied parameters
weightedSum = cv2.addWeighted(img1, 0.5, img2, 0.4, 0)
cv2.imshow("Output", weightedSum)
cv2.waitKey(0)

# -----------------Subtraction of Image------------------------
'''
Just like addition, we can subtract the pixel values in two images and merge them with the help of cv2.subtract().
The images should be of equal size and depth.
Syntax: cv2.subtract(src1, src2)
'''
#  cv2.subtract is applied over the
#  image inputs with applied parameters
sub = cv2.subtract(img1, img2)
cv2.imshow('Subtracted Image', sub)
cv2.waitKey(0)


