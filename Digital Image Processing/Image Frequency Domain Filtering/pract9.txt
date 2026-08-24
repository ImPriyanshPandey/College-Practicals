import cv2
import numpy as np
import matplotlib.pyplot as plt

# ---- Read grayscale image ----
img = cv2.imread(r"img.jpg", 0)
if img is None: raise FileNotFoundError("Check the image path")
fimg = img.astype(np.float32)

# ---- (a) FFT ----
F = np.fft.fft2(fimg)
Fshift = np.fft.fftshift(F)                 # center low frequencies
mag = 20*np.log10(np.abs(Fshift)+1)         # magnitude spectrum (for view)

# ---- Make Gaussian LPF & HPF masks ----
rows, cols = img.shape
u = np.arange(rows) - rows//2
v = np.arange(cols) - cols//2
V, U = np.meshgrid(v, u)
D = np.sqrt(U**2 + V**2)

D0 = 40                                     # cutoff (tune this)
H_low = np.exp(-(D**2)/(2*(D0**2)))         # Gaussian LPF
H_high = 1 - H_low                          # Gaussian HPF

# ---- (b) Apply frequency-domain filters ----
F_low = Fshift * H_low
F_high = Fshift * H_high

# ---- (c) IFFT to reconstruct ----
low_img = np.fft.ifft2(np.fft.ifftshift(F_low))
high_img = np.fft.ifft2(np.fft.ifftshift(F_high))

low_img = np.abs(low_img)
high_img = np.abs(high_img)

# Normalize to 8-bit for display
low_disp = np.clip(low_img, 0, 255).astype(np.uint8)
high_disp = np.clip(high_img, 0, 255).astype(np.uint8)

# ---- Show results ----
titles = [
    "Original", "FFT Magnitude",
    "Gaussian LPF (recon)", "Gaussian HPF (recon)"
]
images = [img, mag, low_disp, high_disp]

plt.figure(figsize=(12,7))
for i,(t,im) in enumerate(zip(titles, images), 1):
    plt.subplot(2,2,i)
    cmap = "gray" if i != 2 else "gray"
    plt.imshow(im, cmap=cmap)
    plt.title(t); plt.axis("off")
plt.tight_layout(); plt.show()

# (optional) save outputs
cv2.imwrite("freq_mag.png", (255*mag/mag.max()).astype(np.uint8))
cv2.imwrite("lowpass_recon.png", low_disp)
cv2.imwrite("highpass_recon.png", high_disp)