import cv2
# Loading Images
img1 = cv2.imread("Resources/binary_pic1.png")
img2 = cv2.imread("Resources/binary_pic2.png")

# AND
# cv2.bitwise_and is applied over the
# image inputs with applied parameters
final_AND = cv2.bitwise_and(img2, img1, mask = None)

# OR
final_OR = cv2.bitwise_or(img2, img1, mask = None)

# XOR
final_XOR = cv2.bitwise_xor(img1, img2, mask = None)

# NOT
final_NOT1 = cv2.bitwise_not(img1, mask = None)
final_NOT2 = cv2.bitwise_not(img2, mask = None)

# Outputs
cv2.imshow('AND', final_AND)
cv2.imshow('OR', final_OR)
cv2.imshow('XOR', final_XOR)
cv2.imshow('NOT on Image 1', final_NOT1)
cv2.imshow('NOT on Image 2', final_NOT2)
cv2.waitKey(0)