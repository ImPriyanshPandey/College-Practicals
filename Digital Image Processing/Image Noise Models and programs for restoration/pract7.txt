import cv2
import numpy as np
import matplotlib.pyplot as plt

# --- Read image (grayscale) ---
image_path = r"cameraman.jfif"
img = cv2.imread(image_path, 0)

# ========== (b) Add & Remove Salt-and-Pepper Noise ==========
sp_noisy = img.copy()
prob = 0.05
n = int(prob * img.size // 2)
coords = [np.random.randint(0, s, n) for s in img.shape]
sp_noisy[coords] = 255
coords = [np.random.randint(0, s, n) for s in img.shape]
sp_noisy[coords] = 0

# Median filter (best for S&P)
sp_median = cv2.medianBlur(sp_noisy, 3)

# Local Wiener (no SciPy): estimate local mean/var and noise
k = 5
spf = sp_noisy.astype(np.float32)
mu  = cv2.boxFilter(spf, ddepth=-1, ksize=(k, k))
mu2 = cv2.boxFilter(spf*spf, ddepth=-1, ksize=(k, k))
var = np.maximum(mu2 - mu*mu, 0.0)
noise = np.mean(var)
w = var / (var + noise + 1e-8)
sp_wiener = mu + w * (spf - mu)
sp_wiener = np.clip(sp_wiener, 0, 255).astype(np.uint8)

# ========== (c) Add Gaussian Noise & Minimize ==========
sigma = 20.0
gauss = np.random.normal(0, sigma, img.shape).astype(np.float32)
gauss_noisy = np.clip(img.astype(np.float32) + gauss, 0, 255).astype(np.uint8)

# Non-Local Means (strong for Gaussian)  → (a) Image restoration as well
gauss_nlm = cv2.fastNlMeansDenoising(gauss_noisy, None, h=12, templateWindowSize=7, searchWindowSize=21)

# Median (for comparison; not ideal for Gaussian)
gauss_median = cv2.medianBlur(gauss_noisy, 3)

# Local Wiener on Gaussian noisy image
gf = gauss_noisy.astype(np.float32)
gmu  = cv2.boxFilter(gf, -1, (k, k))
gmu2 = cv2.boxFilter(gf*gf, -1, (k, k))
gvar = np.maximum(gmu2 - gmu*gmu, 0.0)
gnoise = np.mean(gvar)
gw = gvar / (gvar + gnoise + 1e-8)
gauss_wiener = gmu + gw * (gf - gmu)
gauss_wiener = np.clip(gauss_wiener, 0, 255).astype(np.uint8)

# (a) Optional general restoration (edge-preserving)
restored_bilateral = cv2.bilateralFilter(img, d=9, sigmaColor=75, sigmaSpace=75)

# ========== Show results ==========
titles = [
    "Original",
    "S&P Noisy", "Median (S&P)", "Wiener (S&P)",
    "Gaussian Noisy", "Median (Gauss)", "NLM (Gauss)", "Wiener (Gauss)",
    "Bilateral (restore)"
]
images = [
    img,
    sp_noisy, sp_median, sp_wiener,
    gauss_noisy, gauss_median, gauss_nlm, gauss_wiener,
    restored_bilateral
]

plt.figure(figsize=(14, 8))
for i, (t, im) in enumerate(zip(titles, images), 1):
    plt.subplot(3, 3, i)
    plt.imshow(im, cmap="gray")
    plt.title(t, fontsize=9)
    plt.axis("off")
plt.tight_layout()
plt.show()