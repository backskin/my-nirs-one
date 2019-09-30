import numpy as np
from skimage.io import imread, imsave, imshow
from skimage import img_as_float, img_as_ubyte
import graylib as grl
import matplotlib.pyplot as plt
import colorsystem.bt709 as bt


image = img_as_float(imread('tiger-color.png'))

image_yuv = bt.to_yuv(image)
image_restored = np.clip(bt.to_rgb(image_yuv), 0.0, 1.0)

image = img_as_ubyte(image)
image_restored = img_as_ubyte(image_restored)

print((image - image_restored).sum(), np.array_equal(image_restored, image))

image_yuv[:, :, 0] = grl.lin_con(image_yuv[:, :, 0], 0.05)

image_restored = np.clip(bt.to_rgb(image_yuv), 0.0, 1.0)
image_restored = img_as_ubyte(image_restored)

imsave('out_img.png', image_restored)
