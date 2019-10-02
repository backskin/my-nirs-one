from skimage.io import imread, imsave, imshow
import matplotlib.pyplot as plt
import numpy as np

from filters import rng_filter_rgb, rng_filter_yuv, median, erosion, dilatation, \
    convolution_rgb, convolution_yuv, noising_yuv, noising_rgb, similarity
from stegas import insert_dwm, extract_dwm, insert_dwm_wkey, extract_dwm_wkey, dwm_guess

# Test 0 - зашумить - встроить ЦВЗ - восстановить медианой - извлечь ЦВЗ

# image, dwm = imread('palm-tree.png'), imread('dwm3.bmp')
# imshow(image)
# plt.show()
# image = noising_rgb(image, 75)
# im_with_dwm = insert_dwm(image, dwm)
# # im_with_dwm = noising_yuv(im_with_dwm, 2)
# imshow(im_with_dwm)
# plt.show()
# im_with_dwm = rng_filter_yuv(median, im_with_dwm)
# imsave('palm-tree-noise-75.png', im_with_dwm)
# dwm_layer = extract_dwm(im_with_dwm)
# imshow(dwm_layer)
# plt.show()
# dwm_g = dwm_guess(dwm_layer, dwm.shape[0], dwm.shape[1])
# imsave('dwm-tree-noise-75.png', dwm_g)
#
# print('Similarity = ', similarity(dwm, dwm_g))
# imshow(dwm_g)
# plt.show()

# график зависимости для шума (его дисперсии) перед встраиванием
values = []
steps = 21
k = 0.5
image, dwm = imread('palm-tree.png'), imread('dwm3.bmp')
im_with_dwm = insert_dwm(image, dwm)
for i in range(steps):
    # image = noising_yuv(image, i * k)
    im_with_dwm_noised = noising_yuv(im_with_dwm, i*k)
    im_with_dwm = rng_filter_yuv(erosion, im_with_dwm_noised)
    dwm_layer = extract_dwm(im_with_dwm_noised)
    dwm_g = dwm_guess(dwm_layer, dwm.shape[0], dwm.shape[1])
    if i*k == 1:
        imsave('dwm-noise-2.png', dwm_g)
    values += [similarity(dwm, dwm_g) * 100]
    print('Got ', i, 'Similarity = %.2f prc' % values[i])

plt.plot(np.array(range(steps)) * k, values)
plt.xlabel('отн. дисперсия шума')
plt.ylabel('восстановление ЦВЗ, в %')
plt.savefig('fig-3-eros-before-from-0-to-10.png')
