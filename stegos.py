import numpy as np
import colorsystem.bt709 as bt
from skimage.io import imread, imsave, imshow
from skimage import img_as_float, img_as_ubyte
import matplotlib.pyplot as plt


def btb(bool_con):
    return 1 if bool_con else 0


def nzb_insert_fast(container, watermark):

    new_cont = container.copy()
    st_i = len(watermark)
    st_j = len(watermark[0])

    for i in range(len(container) // st_i):
        for j in range(len(container[0]) // st_j):

            new_cont[i*st_i:(i+1)*st_i, j*st_j:(j+1)*st_j] -= \
                new_cont[i*st_i:(i+1)*st_i, j*st_j:(j+1)*st_j] % 2\
                - (new_cont[i*st_i:(i+1)*st_i, j*st_j:(j+1)*st_j] % 2 + watermark[:, :] + j + i) % 2

    return new_cont


def nzb_extract(container):
    plot = container.copy()
    plot[:, :] = container[:, :] % 2 * 255
    return plot


image, dwm = imread('cont.png'), imread('dwm.bmp')
image_fl = img_as_float(image)
imshow(image)
plt.show()

# здесь щас будет метод встраивания знака в яркость с преобразованием

cont_yuv = bt.to_yuv(image_fl)
imshow(cont_yuv)
plt.show()

cont_yuv[:, :, 0] = img_as_float(nzb_insert_fast(img_as_ubyte(cont_yuv[:, :, 0]), dwm))

image_restored = img_as_ubyte(np.clip(bt.to_rgb(cont_yuv), 0.0, 1.0))

img_sub = np.absolute(image_restored - image)
imshow(nzb_extract(img_sub))
plt.show()

imsave('exploit.png', img_sub)
imsave('cont-with-dwm.png', image_restored)
imshow(image_restored)
plt.show()

again_img = imread('cont-with-dwm.png')
again_yuv = np.clip(bt.to_yuv(img_as_float(again_img)), -1.0, 1.0)
img_y = nzb_extract(img_as_ubyte(again_yuv[:, :, 0]))

imshow(img_y)
plt.show()

img_y_etalon = img_as_ubyte(bt.to_yuv(image_fl)[:, :, 0])
img_y_check = nzb_extract(img_y_etalon - img_y)
imshow(img_y_check)
plt.show()
