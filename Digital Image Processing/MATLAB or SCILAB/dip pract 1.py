#Program 1
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Path to the image file
image_path = r'car.jfif'  # Replace with your image file

# a. Read and display image
image = cv2.imread(r'car.jfif')
cv2.imshow('Original Image', image)
cv2.waitKey(0)


# b. Resize a given image
resized_image = cv2.resize(image, (200, 200))  # Resize to 200x200
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)

# c. Convert color image to gray-scale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray Image', gray_image)
cv2.waitKey(0)

# d. Convert color/gray-scale image to black & white (binary)
_, bw_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('Black & White Image', bw_image)
cv2.waitKey(0)

# e. Draw the image profile (histogram of pixel intensities)
plt.figure()
plt.title("Gray Image Profile")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.hist(gray_image.ravel(), bins=256, range=[0, 256])
plt.show()

# f. Separate color image into R, G, and B channels
B, G, R = cv2.split(image)
cv2.imshow('Red Channel', R)
cv2.imshow('Green Channel', G)
cv2.imshow('Blue Channel', B)
cv2.waitKey(0)

# g. Create a color image using separated R, G, B planes
merged_image = cv2.merge([B, G, R])  # Merge back in BGR order
cv2.imshow('Merged Image', merged_image)
cv2.waitKey(0)

# h. Write 2D data (e.g., gray image) to image file
cv2.imwrite('output_gray.png', gray_image)
cv2.imwrite('output_bw.png', bw_image)
cv2.imwrite('output_resized.png', resized_image)

cv2.destroyAllWindows()
