import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load grayscale image
img = cv2.imread("lenna.png", 0)

# --- A) Using OpenCV inbuilt functions ---

# Histogram using OpenCV
hist_inbuilt = cv2.calcHist([img], [0], None, [256], [0, 256])

# Histogram equalization (OpenCV)
equalized_inbuilt = cv2.equalizeHist(img)
equalized_hist_inbuilt = cv2.calcHist([equalized_inbuilt], [0], None, [256], [0, 256])

# --- B) Without using OpenCV inbuilt functions ---

# Manual histogram
hist_manual = np.zeros(256, dtype=int)
for pixel in img.ravel():
    hist_manual[pixel] += 1

# Normalize histogram
hist_norm = hist_manual / hist_manual.sum()

# CDF (Cumulative Distribution Function)
cdf = hist_norm.cumsum()

# Lookup table
lut = np.floor(255 * cdf).astype(np.uint8)

# Apply manual equalization
equalized_manual = lut[img]

# Manual histogram of equalized image
equalized_hist_manual = np.zeros(256, dtype=int)
for pixel in equalized_manual.ravel():
    equalized_hist_manual[pixel] += 1

# --- Display results ---
plt.figure(figsize=(14, 10))

# Original Image
plt.subplot(3, 2, 1)
plt.title('Original Image')
plt.imshow(img, cmap='gray')
plt.axis('off')

# Original Histogram (Inbuilt)
plt.subplot(3, 2, 2)
plt.title('Original Histogram (Inbuilt)')
plt.plot(hist_inbuilt)
plt.xlim([0, 256])

# Equalized Image (Inbuilt)
plt.subplot(3, 2, 3)
plt.title('Equalized Image (Inbuilt)')
plt.imshow(equalized_inbuilt, cmap='gray')
plt.axis('off')

# Equalized Histogram (Inbuilt)
plt.subplot(3, 2, 4)
plt.title('Equalized Histogram (Inbuilt)')
plt.plot(equalized_hist_inbuilt)
plt.xlim([0, 256])

# Manual Equalized Image
plt.subplot(3, 2, 5)
plt.title('Equalized Image (Manual)')
plt.imshow(equalized_manual, cmap='gray')
plt.axis('off')

# Manual Equalized Histogram
plt.subplot(3, 2, 6)
plt.title('Equalized Histogram (Manual)')
plt.plot(equalized_hist_manual)
plt.xlim([0, 256])

plt.tight_layout()
plt.show()
