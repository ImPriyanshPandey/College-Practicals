import cv2
import numpy as np

# Load the image
image_path = r'C:\\Users\\Dell\\OneDrive\\Desktop\\DIP Practicals\\pract6\\img.jpg'
img = cv2.imread(image_path)  
(h, w) = img.shape[:2]

# a. Translation (shift image right and down)
tx, ty = 50, 30  # Translation offsets
translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
translated_img = cv2.warpAffine(img, translation_matrix, (w, h))

# b. Scaling (resize image)
scale_x, scale_y = 1.5, 1.5
scaled_img = cv2.resize(img, None, fx=scale_x, fy=scale_y, interpolation=cv2.INTER_LINEAR)

# c. Rotation (rotate image around center)
angle = 45
rotation_center = (w // 2, h // 2)
rotation_matrix = cv2.getRotationMatrix2D(rotation_center, angle, 1.0)
rotated_img = cv2.warpAffine(img, rotation_matrix, (w, h))

# d. Shrinking (reduce size)
shrink_img = cv2.resize(img, (w // 2, h // 2), interpolation=cv2.INTER_AREA)

# e. Zooming (zoom into center part of image)
# Crop center and resize back
zoom_crop = img[h//4:3*h//4, w//4:3*w//4]  # Crop center region
zoom_img = cv2.resize(zoom_crop, (w, h), interpolation=cv2.INTER_LINEAR)

# Display results
cv2.imshow("Original", img)
cv2.imshow("Translated", translated_img)
cv2.imshow("Scaled (1.5x)", scaled_img)
cv2.imshow("Rotated (45 deg)", rotated_img)
cv2.imshow("Shrunken (0.5x)", shrink_img)
cv2.imshow("Zoomed (center)", zoom_img)

# Save outputs (optional)
cv2.imwrite("translated.jpg", translated_img)
cv2.imwrite("scaled.jpg", scaled_img)
cv2.imwrite("rotated.jpg", rotated_img)
cv2.imwrite("shrunken.jpg", shrink_img)
cv2.imwrite("zoomed.jpg", zoom_img)

cv2.waitKey(0)
cv2.destroyAllWindows()