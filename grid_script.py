import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Cretaing the Pixel array 

from PIL import Image
from PIL import Image, ImageOps
import numpy as np

import os
path = '/Volumes/MY_PASSPORT/JRF/cancer_genome/gopal_gen_copy/png_files'

image_list = []
for entry in os.listdir():
    if entry.endswith('.png'):
        image_list.append(entry)

print(image_list)
def get_concat_h_multi_resize(im_list, resample=Image.BICUBIC):
    max_height = max(im.height for im in im_list)
    #print(max_height)
    im_list_resize = [im.resize((int(im.width * max_height / im.height), max_height),resample=resample) for im in im_list]
    #print(im_list)
    #im_list_resize = im_list
    total_width = sum(im.width for im in im_list_resize)
    #print(total_width)
    dst = Image.new('RGB', (total_width, max_height))
    pos_x = 0
    for im in im_list_resize:
        dst.paste(im, (pos_x, 0))
        pos_x += im.width
    return dst

def get_concat_v_multi_resize(im_list, resample=Image.BICUBIC):
    max_width = max(im.width for im in im_list)
    #im_list_resize = [im.resize((min_width, int(im.height * max_width / im.width)),resample=resample) for im in im_list]
    im_list_resize = im_list
    total_height = sum(im.height for im in im_list_resize)
    dst = Image.new('RGB', (max_width, total_height))
    pos_y = 0
    for im in im_list_resize:
        dst.paste(im, (0, pos_y))
        pos_y += im.height
    return dst

def get_concat_tile_resize(im_list_2d, resample=Image.BICUBIC):
    im_list_v = [get_concat_h_multi_resize(im_list_h, resample=resample) for im_list_h in im_list_2d]
    return get_concat_v_multi_resize(im_list_v, resample=resample)

im = [Image.open(x) for x in image_list]

for entry in os.listdir(path):
    if entry.endswith('.png'):
        get_concat_tile_resize([[im[0], im[1]],
                        [im[2], im[3],im[4]],
                        [im[5]],
                        [im[6], im[7]],
                        [im[8], im[9]], 
                        [im[10],im[11]],
                        [im[12]],
                        [im[13]],
                        [im[14], im[15]],
                        [im[16]]
                        ]).save('pillow_concat_tile_resize.tiff')

