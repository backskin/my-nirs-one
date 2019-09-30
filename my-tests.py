from skimage.io import imread, imsave, imshow
import matplotlib.pyplot as plt
import numpy as np

from filters import rng_filter_rgb, median, erosion, dilatation, \
    convolution_rgb, noising_by_yuv, noising_rgb
from stegos import insert_dwm, extract_dwm

# TEST 1 : simple inception
#
# image, dwm = imread('cont.png'), imread('dwm2.bmp')
# im_with_dwm = insert_dwm(image, dwm)
# imsave('cont-with-dwm.png', im_with_dwm)
# again_img = imread('cont-with-dwm.png')
# dwm_layer = extract_dwm(again_img)


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
