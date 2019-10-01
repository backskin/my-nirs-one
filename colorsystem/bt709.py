from numpy import matmul, array, clip
from skimage.io import imread, imsave


def conversion(img, matrix):
    return array([[matmul(matrix, pixel) for pixel in col[:]] for col in img[:]])


def to_yuv(img_f):
    drc_matrix = array([[0.2126, 0.7152, 0.0722],
                        [-0.09991, -0.33609, 0.436],
                        [0.615, -0.55861, -0.05639]])

    return conversion(img_f, drc_matrix)


def to_rgb(yuv_f):
    inv_matrix = array([[1, 0, 1.28033],
                        [1, -0.21482, -0.38059],
                        [1, 2.12798, 0]])

    return conversion(yuv_f, inv_matrix)


def check_restoration(ubyte_image):

    from skimage import img_as_float, img_as_ubyte

    image_fl = img_as_float(ubyte_image)
    cont_yuv = to_yuv(image_fl)
    image_restored = img_as_ubyte(clip(to_rgb(cont_yuv), 0.0, 1.0))

    from numpy import array_equal
    return array_equal(image_restored, ubyte_image)
