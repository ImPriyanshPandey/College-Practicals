import cv2
import numpy as np
import matplotlib.pyplot as plt

# ---- Read grayscale image ----
img = cv2.imread(r"pepper.png", 0)


# ---- Add mild Gaussian noise (so low-pass denoises something) ----
sigma = 15.0
noise = np.random.normal(0, sigma, img.shape).astype(np.float32)
noisy = np.clip(img.astype(np.float32) + noise, 0, 255).astype(np.uint8)

# ---- 3x3 masks (kernels) ----
lowpass_box = np.ones((3,3), np.float32) / 9.0
lowpass_gauss = (1/16.0) * np.array([[1,2,1],[2,4,2],[1,2,1]], np.float32)
highpass = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]], np.float32)

# ---- 2-D convolution via filter2D ----
denoised_box = cv2.filter2D(noisy, -1, lowpass_box)     # Low-pass (average)
denoised_gauss = cv2.filter2D(noisy, -1, lowpass_gauss) # Low-pass (Gaussian)
edges = cv2.filter2D(img, -1, highpass)                 # High-pass (edges)

# ---- Show results ----
titles = ["Original", "Noisy", "Low-pass 3x3 (Box)", "Low-pass 3x3 (Gaussian)", "High-pass 3x3 (Edges)"]
images = [img, noisy, denoised_box, denoised_gauss, edges]

plt.figure(figsize=(12,6))
for i,(t,im) in enumerate(zip(titles, images), 1):
    plt.subplot(2,3,i)
    plt.imshow(im, cmap="gray")
    plt.title(t); plt.axis("off")
plt.tight_layout(); plt.show()

# (optional) save outputs
cv2.imwrite("noisy.png", noisy)
cv2.imwrite("lowpass_box.png", denoised_box)
cv2.imwrite("lowpass_gauss.png", denoised_gauss)
cv2.imwrite("highpass.png", edges)