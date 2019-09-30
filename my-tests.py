import numpy as np
import random
from skimage.io import imread, imsave
from skimage import img_as_float, img_as_ubyte
import graylib as grl
import colorsystem.bt709 as bt


seed_1 = 'hello'

random.seed(seed_1)
key_mask = [[random.getrandbits(1) for i in range(4)] for j in range(4)]
print(key_mask)

key_mask = [[random.getrandbits(1) for i in range(4)] for j in range(4)]
print(key_mask)

random.seed(seed_1)
key_mask = [[random.getrandbits(1) for i in range(4)] for j in range(4)]
print(key_mask)
