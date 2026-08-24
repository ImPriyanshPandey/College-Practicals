import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load two images (grayscale)
img1 = cv2.imread("then.jpeg", 0)
img2 = cv2.imread("img2.png", 0)

# Resize images if sizes differ
if img1.shape != img2.shape:
    img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

# a. AND operation
and_img = cv2.bitwise_and(img1, img2)

# b. OR operation
or_img = cv2.bitwise_or(img1, img2)

# c. Intersection (same as AND)
intersection_img = cv2.bitwise_and(img1, img2)

# d. XOR Watermarking
watermarked_img = cv2.bitwise_xor(img1, img2)

# e. NOT (Negative)
not_img1 = cv2.bitwise_not(img1)

# Titles & images
titles = [
    "Image 1",
    "Image 2",
    "AND Operation",
    "OR Operation",
    "Intersection",
    "Watermarked (XOR)",
    "NOT Operation (Negative)"
]

images = [
    img1, img2, and_img, or_img,
    intersection_img, watermarked_img, not_img1
]

# Display outputs
plt.figure(figsize=(14, 8))
for i, (title, image) in enumerate(zip(titles, images), 1):
    plt.subplot(2, 4, i)
    plt.imshow(image, cmap="gray")
    plt.title(title)
    plt.axis("off")

plt.tight_layout()
plt.show()

# Save output images
cv2.imwrite("and_operation.png", and_img)
cv2.imwrite("or_operation.png", or_img)
cv2.imwrite("intersection.png", intersection_img)
cv2.imwrite("watermarked_xor.png", watermarked_img)
cv2.imwrite("not_image1.png", not_img1)
