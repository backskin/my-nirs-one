import numpy as np
from skimage.io import imread, imshow, imsave
import matplotlib.pyplot as plt

def convolution(img, mask):

    img_w = img.shape[0]
    img_h = img.shape[1]
    m_w = len(mask)
    m_h = len(mask[0])
    new_img = img.copy()
    cast_img = np.array([[0] * (img_h + m_h - 1)] * (img_w + m_w - 1)).astype(np.uint8)

    cast_img[:1 - m_w, :m_h] = img[:, :m_h]
    cast_img[-m_w:, :1 - m_h] = img[-m_w:, :]
    cast_img[m_w - 1:, -m_h:] = img[:, -m_h:]
    cast_img[:m_w, m_h - 1:] = img[:m_w, :]

    cast_img[m_w // 2:-m_w + 2, m_h // 2:-m_h + 2] = img[:, :]

    for i in range(img_w):
        for j in range(img_h):

            cast_block = cast_img[i: i + m_w, j: j + m_h]
            new_img[i, j] = np.clip((cast_block * mask[:, :]).sum(), 0, 255)

    return new_img


def convolution_rgb(img, mask):

    img[:, :, 0] = convolution(image[:, :, 0], mask)
    img[:, :, 1] = convolution(image[:, :, 1], mask)
    img[:, :, 2] = convolution(image[:, :, 2], mask)

    return img


def dilatation(block, mask):
    mask = np.array(mask).flatten()
    block = np.array(block).flatten()
    array = []
    for i in range(len(mask)):
        for j in range(mask[i]):
            array += [block[i]]

    array.sort()

    return array[-1]


def erosion(block, mask):
    mask = np.array(mask).flatten()
    block = np.array(block).flatten()
    array = []
    for i in range(len(mask)):
        for j in range(mask[i]):
            array += [block[i]]

    array.sort()

    return array[0]


def median(block, mask):

    if len(block) != len(mask):
        raise Exception('Exception during filtering:', 'block.len %d != mask.len %d' % (len(block), len(mask)))

    if len(block) % 2 == 0:
        raise Exception('Exception during filtering:' 'block.len is even; must be odd number')
    mask = np.array(mask).flatten()
    block = np.array(block).flatten()
    array = []
    for i in range(len(mask)):
        for j in range(mask[i]):
            array += [block[i]]

    array.sort()

    return array[len(array) // 2 + 1]


def rng_filter(method, img, mask):
    img_w = img.shape[0]
    img_h = img.shape[1]
    m_w = len(mask)
    m_h = len(mask[0])
    new_img = img.copy()
    cast_img = np.array([[0] * (img_h + m_h - 1)] * (img_w + m_w - 1)).astype(np.uint8)

    cast_img[:1 - m_w, :m_h] = img[:, :m_h]
    cast_img[-m_w:, :1 - m_h] = img[-m_w:, :]
    cast_img[m_w - 1:, -m_h:] = img[:, -m_h:]
    cast_img[:m_w, m_h - 1:] = img[:m_w, :]

    cast_img[m_w // 2:-m_w + 2, m_h // 2:-m_h + 2] = img[:, :]

    for i in range(img_w):
        for j in range(img_h):
            cast_block = np.array(cast_img[i: i + m_w, j: j + m_h])
            new_img[i, j] = method(cast_block, mask)

    return new_img


def rng_filter_rgb(method, img, mask):

    if mask is None:
        mask = [[[1] * 3] * 3]
    img[:, :, 0] = rng_filter(method, img[:, :, 0], mask)
    img[:, :, 1] = rng_filter(method, img[:, :, 1], mask)
    img[:, :, 2] = rng_filter(method, img[:, :, 2], mask)

    return img


image = imread('tiger-color.png')
sharp_mask = np.array([[-1, -1, -1],
                       [-1, 9, -1],
                       [-1, -1, -1]])

sharp_mask = sharp_mask[:, :] * 1

imshow(image)
plt.show()

# img = convolution_rgb(image.copy(), sharp_mask)
# imsave('tiger-color-sharp.png', img)
# imshow(img)
# plt.show()

img = rng_filter_rgb(median, image.copy(), [[1] * 3] * 3)
imsave('tiger-color-median.png', img)
imshow(img)
plt.show()

img = rng_filter_rgb(erosion, image.copy(), [[1] * 3] * 3)
imsave('tiger-color-eros.png', img)
imshow(img)
plt.show()

img = rng_filter_rgb(dilatation, image.copy(), [[1] * 3] * 3)
imsave('tiger-color-dilat.png', img)
imshow(img)
plt.show()
