import cv2
import numpy as np
import matplotlib.pyplot as plt

# ---- Read grayscale image ----
img = cv2.imread(r"img.jpg", 0)

# ---- Convert to binary (thresholding) ----
_, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# ---- Create structuring element (kernel) ----
kernel = np.ones((5, 5), np.uint8)

# ---- Morphological operations ----
erosion = cv2.erode(binary, kernel, iterations=1)
dilation = cv2.dilate(binary, kernel, iterations=1)

# ---- Show results ----
titles = ["Original Grayscale", "Binary", "Erosion", "Dilation"]
images = [img, binary, erosion, dilation]

plt.figure(figsize=(10,6))
for i, (t, im) in enumerate(zip(titles, images), 1):
    plt.subplot(2, 2, i)
    plt.imshow(im, cmap='gray')
    plt.title(t)
    plt.axis('off')
plt.tight_layout()
plt.show()