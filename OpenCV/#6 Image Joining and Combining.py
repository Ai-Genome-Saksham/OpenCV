import cv2
import numpy as np

img1 = cv2.imread("Resources/pic3.jpg")
img2 = cv2.imread("Resources/pic4.jpg")
img3 = cv2.imread("Resources/pic2.jpg")

# Concatenate images of same width vertically
""""cv2.vconcat() used"""
img_v = cv2.vconcat([img1, img2])

# Concatenate images of different widths vertically
"""" A function to resize the image """
def vconcat_resize_min(im_list, interpolation=cv2.INTER_CUBIC):
    w_min = min(im.shape[1] for im in im_list)
    im_list_resize = [cv2.resize(im, (w_min, int(im.shape[0] * w_min / im.shape[1])), interpolation=interpolation)
                      for im in im_list]
    return cv2.vconcat(im_list_resize)

img_v_resize = vconcat_resize_min([img1, img2, img3])

# Concatenate images of same height horizontally
img_h = cv2.hconcat([img1, img2])

# Concatenate images of different heights horizontally
def hconcat_resize_min(im_list, interpolation=cv2.INTER_CUBIC):
    h_min = min(im.shape[0] for im in im_list)
    im_list_resize = [cv2.resize(im, (int(im.shape[1] * h_min / im.shape[0]), h_min), interpolation=interpolation)
                      for im in im_list]
    return cv2.hconcat(im_list_resize)

img_h_resize = hconcat_resize_min([img1, img2, img3])

# Concatenate vertically and horizontally (like tiles)


#cv2.imshow("Vertical join same width ", img_v)
#cv2.imshow("Vertical join Different width", img_v_resize)
#cv2.imshow("Horizontal join same height ", img_h)
cv2.imshow("Horizontal join Different height", img_h_resize)
cv2.waitKey(0)