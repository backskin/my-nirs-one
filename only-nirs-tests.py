from skimage.io import imread, imsave, imshow
import matplotlib.pyplot as plt
import numpy as np

from filters import rng_filter_rgb, rng_filter_yuv, median, erosion, dilatation, \
    convolution_rgb, convolution_yuv, noising_yuv, noising_rgb, similarity
from stegos import insert_dwm, extract_dwm, insert_dwm_wkey, extract_dwm_wkey, dwm_guess

# Test 0 - зашумить - встроить ЦВЗ - восстановить медианой - извлечь ЦВЗ

image, dwm = imread('palm-tree.jpg'), imread('dwm3.bmp')
# # imshow(image)
# # plt.show()
#
im_with_dwm = insert_dwm(image, dwm)
# imsave('palm-noise-0.5.png', im_with_dwm)
im_with_dwm = noising_yuv(im_with_dwm, 1)
# imshow(im_with_dwm)
# plt.show()
im_with_dwm = rng_filter_yuv(erosion, im_with_dwm)
imsave('palm-noise-ex-0.2.png', im_with_dwm)
imshow(im_with_dwm)
plt.show()
dwm_layer = extract_dwm(im_with_dwm)
# imshow(dwm_layer)
# plt.show()
dwm_g = dwm_guess(dwm_layer, dwm.shape[0], dwm.shape[1])
print('Similarity = %.3f' % similarity(dwm_g, dwm))
imsave('dwm-guess1.png', dwm_g)
#
#
# image = noising_yuv(image, 10)
im_with_dwm = insert_dwm(image, dwm)
im_with_dwm = noising_yuv(im_with_dwm, 1)
# imshow(im_with_dwm)
# plt.show()
im_with_dwm = rng_filter_yuv(dilatation, im_with_dwm)
imsave('palm-noise-ex-2.png', im_with_dwm)
imshow(im_with_dwm)
plt.show()
dwm_layer = extract_dwm(im_with_dwm)
# imshow(dwm_layer)
# plt.show()
dwm_g = dwm_guess(dwm_layer, dwm.shape[0], dwm.shape[1])
print('Similarity = %.3f' % similarity(dwm_g, dwm))
imsave('dwm-guess2.png', dwm_g)
#
# image = noising_yuv(image, 50)
im_with_dwm = insert_dwm(image, dwm)
im_with_dwm = noising_yuv(im_with_dwm, 1)


mask = 1 / 9 * np.array([[1, 1, 1],
                               [1, 1, 1],
                               [1, 1, 1]])[:, :]

im_with_dwm = convolution_yuv(im_with_dwm, mask)
imsave('palm-noise-ex-3.png', im_with_dwm)
imshow(im_with_dwm)
plt.show()
dwm_layer = extract_dwm(im_with_dwm)
# imshow(dwm_layer)
# plt.show()
dwm_g = dwm_guess(dwm_layer, dwm.shape[0], dwm.shape[1])
print('Similarity = %.3f' % similarity(dwm_g, dwm))
imsave('dwm-guess3.png', dwm_g)

# график зависимости для шума (его дисперсии) перед встраиванием
# values = []
# steps = 50
# k = 0.2

# for i in range(steps):
#     image, dwm = imread('palm-tree.jpg'), imread('dwm3.bmp')
#     # image = noising_yuv(image, i * k)
#     im_with_dwm = insert_dwm(image, dwm)
#     im_with_dwm = noising_yuv(im_with_dwm, i*k)
#     im_with_dwm = rng_filter_yuv(median, im_with_dwm)
#     dwm_layer = extract_dwm(im_with_dwm)
#     dwm_g = dwm_guess(dwm_layer, dwm.shape[0], dwm.shape[1])
#     values += [similarity(dwm, dwm_g) * 100]
#     print('Got ', i, 'Similarity = %.2f prc' % values[i])
#
# plt.plot(np.array(range(steps)) * k, values)
# plt.xlabel('отн-я дисперсия шума')
# plt.ylabel('восстановление ЦВЗ, в %')
# plt.savefig('fig-1-from-0-to-10.png')
