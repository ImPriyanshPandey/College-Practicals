import cv2
import numpy as np

# Load two images (ensure they are the same size)
img1 = cv2.imread( r"C:\\Users\\Dell\\OneDrive\\Desktop\\DIP Practicals\\pract3\\then.jpeg")  
img2 = cv2.imread(r"C:\\Users\\Dell\\OneDrive\\Desktop\\DIP Practicals\\pract3\\img2.png")  

# Resize second image to match first (if needed)
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
print(" Resize successful")

# a. Addition of two images
added_img = cv2.add(img1, img2)
cv2.imshow('Image Addition', added_img)

# b. Subtraction of one image from another
subtracted_img = cv2.subtract(img1, img2)
cv2.imshow('Image Subtraction', subtracted_img)

# c. Mean value of image
mean_val = cv2.mean(img1)[:3]  # Only B, G, R values
print(f"Mean Value of Image1 (B, G, R): {mean_val}")

# d. Adjust brightness by changing mean value
# Convert to float for precise scaling
img1_float = img1.astype(np.float32)
mean_target = 150  # Example target mean brightness

current_mean = np.mean(img1_float)
scale = mean_target / current_mean

brightness_adjusted = np.clip(img1_float * scale, 0, 255).astype(np.uint8)
cv2.imshow('Brightness Adjusted', brightness_adjusted)

# Save outputs (optional)
cv2.imwrite('added_image.jpg', added_img)
cv2.imwrite('subtracted_image.jpg', subtracted_img)
cv2.imwrite('brightness_adjusted.jpg', brightness_adjusted)

cv2.waitKey(0)
cv2.destroyAllWindows()