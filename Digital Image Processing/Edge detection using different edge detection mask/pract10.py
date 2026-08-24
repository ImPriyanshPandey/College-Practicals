import cv2
import numpy as np
import matplotlib.pyplot as plt

# ---- Read grayscale image ----
img = cv2.imread(r"img.jfif", 0)

# ===== Sobel (OpenCV) =====
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobel_mag = cv2.magnitude(sobel_x, sobel_y)

# ===== Prewitt =====
prewitt_kx = np.array([[-1,0,1],[-1,0,1],[-1,0,1]], np.float32)
prewitt_ky = np.array([[1,1,1],[0,0,0],[-1,-1,-1]], np.float32)
prewitt_x = cv2.filter2D(img, -1, prewitt_kx)
prewitt_y = cv2.filter2D(img, -1, prewitt_ky)
prewitt_mag = cv2.magnitude(prewitt_x.astype(np.float32), prewitt_y.astype(np.float32))

# ===== Roberts =====
roberts_kx = np.array([[1,0],[0,-1]], np.float32)
roberts_ky = np.array([[0,1],[-1,0]], np.float32)
roberts_x = cv2.filter2D(img, -1, roberts_kx)
roberts_y = cv2.filter2D(img, -1, roberts_ky)
roberts_mag = cv2.magnitude(roberts_x.astype(np.float32), roberts_y.astype(np.float32))

# ===== Laplacian =====
laplacian = cv2.Laplacian(img, cv2.CV_64F)

# ---- Display results ----
titles = [
    "Original",
    "Sobel Magnitude", "Prewitt Magnitude", "Roberts Magnitude",
    "Laplacian"
]
images = [
    img,
    sobel_mag, prewitt_mag, roberts_mag,
    laplacian
]

plt.figure(figsize=(12,6))
for i,(t,im) in enumerate(zip(titles, images), 1):
    plt.subplot(2,3,i)
    plt.imshow(im, cmap="gray")
    plt.title(t); plt.axis("off")
plt.tight_layout(); plt.show()