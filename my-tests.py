from skimage.io import imread, imsave, imshow
import matplotlib.pyplot as plt
import numpy as np

from filters import rng_filter_rgb, median, erosion, dilatation, \
    convolution_rgb, noising_by_yuv, noising_rgb
from stegos import insert_dwm, extract_dwm, insert_dwm_wkey, extract_dwm_wkey

# TEST 1 : simple inception
#
# image, dwm = imread('cont.png'), imread('dwm2.bmp')
# im_with_dwm = insert_dwm(image, dwm)
# imsave('cont-with-dwm.png', im_with_dwm)
# again_img = imread('cont-with-dwm.png')
# dwm_layer = extract_dwm(again_img)
# imshow(dwm_layer)
# plt.show()


# TEST 2: inception with key
#
# image, dwm = imread('cont.png'), imread('dwm2.bmp')
# key = 'hello_world'
# wrong_key = 'bye_bye'
#
# im_with_dwm = insert_dwm_wkey(image, dwm, key)
# imsave('cont-with-dwm.png', im_with_dwm)
# again_img = imread('cont-with-dwm.png')
# dwm_layer = extract_dwm_wkey(again_img, key)
# imshow(dwm_layer)
# plt.show()
# wr_dwm_layer = extract_dwm_wkey(again_img, wrong_key)
# imshow(wr_dwm_layer)
# plt.show()

# TEST 3: check simple inception and extraction after noise
#
# image, dwm = imread('cont.png'), imread('dwm2.bmp')
# im_with_dwm = insert_dwm(image, dwm)
# imsave('cont-with-dwm.png', im_with_dwm)
# imshow(im_with_dwm)
# plt.show()
# dwm_layer = extract_dwm(im_with_dwm)
# imshow(dwm_layer)
# plt.show()
# im_with_dwm = noising_by_yuv(im_with_dwm.copy(), 0.5)
# imsave('cont-with-dwm-noised.png', im_with_dwm)
# again_img = imread('cont-with-dwm-noised.png')
# imshow(again_img)
# plt.show()
# dwm_layer = extract_dwm(again_img)
# imshow(dwm_layer)
# plt.show()

# TEST 4: check simple inc and ext after sharpen
#
# image, dwm = imread('tiger-color.png'), imread('dwm2.bmp')
#
# sharp_mask = 1 / 8 * np.array([[-1, -1, -1],
#                                [-1, 16, -1],
#                                [-1, -1, -1]])[:, :]
#
# im_with_dwm = insert_dwm(image, dwm)
# dwm_layer = extract_dwm(im_with_dwm)
# imshow(dwm_layer)
# plt.show()
# im_with_dwm = convolution_rgb(im_with_dwm.copy(), sharp_mask)
# imsave('cont-with-dwm-sharp.png', im_with_dwm)
# again_img = imread('cont-with-dwm-sharp.png')
# imshow(again_img)
# plt.show()
# dwm_layer = extract_dwm(again_img)
# imsave('dwm-layer-sharpen.png', dwm_layer)
# imshow(dwm_layer)
# plt.show()

# TEST 5: check simple inc and ext after median filter
image, dwm = imread('tiger-color.png'), imread('dwm2.bmp')
im_with_dwm = insert_dwm(image, dwm)
dwm_layer = extract_dwm(im_with_dwm)
imshow(dwm_layer)
plt.show()
im_with_dwm = rng_filter_rgb(median, im_with_dwm.copy(), [[1] * 3] * 3)
imsave('cont-with-dwm-median.png', im_with_dwm)
again_img = imread('cont-with-dwm-median.png')
imshow(again_img)
plt.show()
dwm_layer = extract_dwm(again_img)
imsave('dwm-layer-median.png', dwm_layer)
imshow(dwm_layer)
plt.show()

# TEST 6: check simple inc and ext after dilatation and erosion filters
