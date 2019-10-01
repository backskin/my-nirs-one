from skimage.io import imread, imsave, imshow
import matplotlib.pyplot as plt
import numpy as np

from filters import rng_filter_rgb, rng_filter_yuv, median, erosion, dilatation, \
    convolution_rgb, convolution_yuv, noising_yuv, noising_rgb, similarity
from stegos import insert_dwm, extract_dwm, insert_dwm_wkey, extract_dwm_wkey, dwm_guess
from colorsystem.bt709 import check_restoration

# Test 0 - зашумить - встроить ЦВЗ - восстановить медианой - извлечь ЦВЗ
# График зависимости для шума (его дисперсии)
values = []
steps = 20
k = 0.5


for i in range(steps):
    image, dwm = imread('red-flower.png'), imread('dwm3.bmp')
    im_with_dwm = insert_dwm(image, dwm)
    im_with_dwm = noising_yuv(im_with_dwm, i * k)
    im_with_dwm = rng_filter_yuv(median, im_with_dwm)
    dwm_layer = extract_dwm(im_with_dwm)
    dwm_g = dwm_guess(dwm_layer, dwm.shape[0], dwm.shape[1])
    imsave('dwm_red_flower-'+str(i)+'.png', dwm_g)
    values += [similarity(dwm, dwm_g) * 100]
    print('Got ', (i+1), 'Similarity = %.2f prc' % values[i])

plt.plot(np.array(range(steps)) * k, values)
plt.xlabel('отн-я дисперсия шума')
plt.ylabel('восстановление ЦВЗ, в %')
plt.savefig('fig-1-from-0-to-10.png')
