import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image (grayscale for simplicity)
image_path = r'C:\\Users\\Dell\\OneDrive\\Desktop\\DIP Practicals\\pract2\\lenna.png'
# Replace with your own image path
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)


# a. Negative Image
negative_img = 255 - img
cv2.imshow("Negative Image", negative_img)

# b. Flip Image (Horizontal and Vertical)
flip_h = cv2.flip(img, 1)   # Horizontal flip
flip_v = cv2.flip(img, 0)   # Vertical flip
cv2.imshow("Flip Horizontal", flip_h)
cv2.imshow("Flip Vertical", flip_v)

# c. Thresholding (Simple binary thresholding)
_, thresh_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("Thresholding", thresh_img)

# d. Contrast Stretching
# Formula: s = (r - rmin) * 255 / (rmax - rmin)
r_min = np.min(img)
r_max = np.max(img)
contrast_stretched = ((img - r_min) * 255 / (r_max - r_min)).astype(np.uint8)
cv2.imshow("Contrast Stretched", contrast_stretched)

# Save outputs if needed
cv2.imwrite('negative_image.png', negative_img)
cv2.imwrite('flip_horizontal.png', flip_h)
cv2.imwrite('flip_vertical.png', flip_v)
cv2.imwrite('threshold_image.png', thresh_img)
cv2.imwrite('contrast_stretched.png', contrast_stretched)

cv2.waitKey(0)
cv2.destroyAllWindows()