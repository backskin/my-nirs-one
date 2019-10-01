from skimage.io import imread, imsave, imshow
import matplotlib.pyplot as plt
import numpy as np

from filters import rng_filter_rgb, rng_filter_yuv, median, erosion, dilatation, \
    convolution_rgb, convolution_yuv, noising_yuv, noising_rgb, similarity
from stegos import insert_dwm, extract_dwm, insert_dwm_wkey, extract_dwm_wkey, dwm_guess

# Test 0 - зашумить - встроить ЦВЗ - восстановить медианой - извлечь ЦВЗ

image, dwm = imread('palm-tree.jpg'), imread('dwm3e.bmp')
imshow(image)
plt.show()
# image = noising_yuv(image, 0.5)
im_with_dwm = insert_dwm(image, dwm)
# im_with_dwm = noising_yuv(im_with_dwm, 2)
imshow(im_with_dwm)
plt.show()
im_with_dwm = rng_filter_yuv(median, im_with_dwm)
imshow(im_with_dwm)
plt.show()
dwm_layer = extract_dwm(im_with_dwm)
imshow(dwm_layer)
plt.show()
dwm_g = dwm_guess(dwm_layer, dwm.shape[0], dwm.shape[1])

print('Similarity = ', similarity(dwm, dwm_g))
imshow(dwm_g)
plt.show()

# график зависимости для шума (его дисперсии)
image, dwm = imread('palm-tree.jpg'), imread('dwm3e.bmp')