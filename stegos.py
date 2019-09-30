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
                old_bit[:, :] - (mark[:, :] + j + i) % 2

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


def insert_dwm(rgb_container, dwm):
    from colorsystem.bt709 import to_yuv, to_rgb
    from skimage import img_as_float, img_as_ubyte
    import numpy as np

    cont_yuv = to_yuv(img_as_float(rgb_container))
    cont_yuv[:, :, 0] = img_as_float(nzb_insert(img_as_ubyte(cont_yuv[:, :, 0]), dwm))
    cont_rgb = img_as_ubyte(np.clip(to_rgb(cont_yuv), 0.0, 1.0))

    return cont_rgb


def extract_dwm(rgb_container):
    from colorsystem.bt709 import to_yuv
    from skimage import img_as_float, img_as_ubyte

    cont_yuv = to_yuv(img_as_float(rgb_container))
    dwm_e = nzb_extract(img_as_ubyte(cont_yuv[:, :, 0]))

    return dwm_e

def insert_dwm_wkey(rgb_container, dwm):
    from colorsystem.bt709 import to_yuv, to_rgb
    from skimage import img_as_float, img_as_ubyte
    import numpy as np

    cont_yuv = to_yuv(img_as_float(rgb_container))
    cont_yuv[:, :, 0] = img_as_float(nzb_insert(img_as_ubyte(cont_yuv[:, :, 0]), dwm))
    cont_rgb = img_as_ubyte(np.clip(to_rgb(cont_yuv), 0.0, 1.0))

    return cont_rgb