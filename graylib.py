import numpy as np

def nzb_insert(dwm, container):
    result = container.copy()
    lines = len(container) // len(dwm)
    cols = len(container[0]) // len(dwm[0])


def conv_no_border(gray_image, filter):
    width = len(gray_image) - len(filter) + 1
    length = len(gray_image[0]) - len(filter[0]) + 1
    new_image = np.array([[0 for i in range(length)] for j in range(width)])
    for i in range(width):
        for j in range(length):

            new_pixel = 0
            for k_i in range(len(filter[:])):
                for k_j in range(len(filter[k_i, :])):
                    new_pixel += gray_image[i + k_i, j + k_j] * filter[k_i, k_j]
            new_image[i, j] = new_pixel
    return new_image


def hist(img):
    histogram = [0] * 256
    for i in range(len(img)):
        for j in range(len(img[i])):
            histogram[img[i, j]] += 1
    return histogram


def lin_con_uint(img, precision):
    x_min, x_max = np.percentile(img, [100*precision, 100*(1 - precision)])
    img_out = 255 * (img - x_min) / (x_max - x_min)
    return np.clip(img_out, 0, 255).astype(np.uint8)


def lin_con(img, precision):
    x_min, x_max = np.percentile(img, [100*precision, 100*(1 - precision)])
    img_out = (img - x_min) / (x_max - x_min)
    return np.clip(img_out, 0.0, 1.0)
