# %%
import cv2
import matplotlib.pyplot as plt

# %%
img = cv2.imread("page.png")
if img is not None:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (560, 900))

    cv2.imshow("title", img)
    cv2.waitKey(1000*5)
else:
    print("Error: Image not found or unable to load.")


# %%
# _, result = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
_, result = cv2.threshold(img, 20, 255, cv2.THRESH_BINARY)

adaptive_result = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 41, 5)



# %% [markdown]
# ![Enumerator](enumerator.png)
# 
# 
# The text in the image describes different thresholding techniques used in image processing. Each technique takes an input image and applies a threshold value to create a binary output image. The output image is based on whether the pixel values in the input image are above or below the threshold.
# 
# Here's a breakdown of each technique:
# 
# **THRESH_BINARY:**
# * If the pixel value is greater than the threshold, it is set to the maximum value (usually 255).
# * Otherwise, it is set to 0.
# 
# **THRESH_BINARY_INV:**
# * This is the inverse of THRESH_BINARY.
# * If the pixel value is greater than the threshold, it is set to 0.
# * Otherwise, it is set to the maximum value.
# 
# **THRESH_TRUNC:**
# * If the pixel value is greater than the threshold, it is set to the threshold value.
# * Otherwise, it remains unchanged.
# 
# **THRESH_TOZERO:**
# * If the pixel value is greater than the threshold, it remains unchanged.
# * Otherwise, it is set to 0.
# 
# **THRESH_TOZERO_INV:**
# * This is the inverse of THRESH_TOZERO.
# * If the pixel value is greater than the threshold, it is set to 0.
# * Otherwise, it remains unchanged.
# 
# The Python code for each technique is also provided, using the OpenCV library.
# 

# %%
cv2.imshow("original", img)
cv2.imshow("result", result)
cv2.imshow("adaptive", adaptive_result)

cv2.waitKey (10*1000)
cv2.destroyAllWindows()


# %%
plt.subplot(1, 3, 1)
plt.title("Original")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title("Result")
plt.imshow(result, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title("Adaptive Result")
plt.imshow(adaptive_result, cmap='gray')
plt.axis('off')

plt.show()

# %%



