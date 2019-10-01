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


image = imread('tiger-color.png')


img = noising_by_yuv(image.copy(), 32)
imsave('tiger-color-noise_yuv.png', img)
imshow(img)
plt.show()

img = noising_rgb(image.copy(), 32)
imsave('tiger-color-noise_rgb.png', img)
imshow(img)
plt.show()


sharp_mask = np.array([[-1, -1, -1],
                       [-1, 16, -1],
                       [-1, -1, -1]])

sharp_mask = sharp_mask[:, :] * 1/8

img = convolution_rgb(image.copy(), sharp_mask)
imsave('tiger-color-sharp.png', img)
imshow(img)
plt.show()

img = rng_filter_rgb(median, image.copy(), [[1] * 3] * 3)
imsave('tiger-color-median.png', img)
imshow(img)
plt.show()
