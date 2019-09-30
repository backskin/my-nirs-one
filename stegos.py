import numpy as np
import colorsystem.bt709 as bt
from skimage.io import imread, imsave, imshow
from skimage import img_as_float, img_as_ubyte
import matplotlib.pyplot as plt


def btb(bool_con):
    return 1 if bool_con else 0


def nzb_insert(contan, mark):

    new_cont = contan.copy()
    st_i = len(mark)
    st_j = len(mark[0])

    for i in range(len(contan) // st_i):
        for j in range(len(contan[0]) // st_j):
            old_bit = new_cont[i*st_i:(i+1)*st_i, j*st_j:(j+1)*st_j] % 2
            new_cont[i*st_i:(i+1)*st_i, j*st_j:(j+1)*st_j] -= \
                old_bit[:, :] - (old_bit[:, :] + mark[:, :] + j + i) % 2

    return new_cont


def nzb_extract(container):
    plot = container.copy()
    plot[:, :] = (container[:, :] % 2) * 255
    return plot


def nzb_insert_secured(contan, mark, key):

    import random
    random.seed(key)

    new_cont = contan.copy()
    st_i = len(mark)
    st_j = len(mark[0])

    for i in range(len(contan) // st_i):
        for j in range(len(contan[0]) // st_j):

            key_mask = [[random.getrandbits(1) for j in range(st_j)] for i in range(st_i)]

            old_bit = new_cont[i*st_i:(i+1)*st_i, j*st_j:(j+1)*st_j] % 2
            new_cont[i*st_i:(i+1)*st_i, j*st_j:(j+1)*st_j] -= \
                old_bit[:, :] - (old_bit[:, :] + mark[:, :] + key_mask + j + i) % 2

    return new_cont


def nzb_extract_secured(container, key):
    import random
    random.seed(key)
    plot = container.copy()
    for i in range(len(container)):
        for j in range(len(container[0])):
            sec_bit = random.getrandbits(1)
            plot[i, j] = ((container[i, j] + sec_bit) % 2) * 255

    return plot


image, dwm = imread('cont.png'), imread('dwm.bmp')
image_fl = img_as_float(image)
imshow(image)
plt.show()

# здесь щас будет метод встраивания знака в яркость с преобразованием

cont_yuv = bt.to_yuv(image_fl)
imshow(cont_yuv[:, :, 0])
plt.show()

cont_yuv[:, :, 0] = img_as_float(nzb_insert(img_as_ubyte(cont_yuv[:, :, 0]), dwm))

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
