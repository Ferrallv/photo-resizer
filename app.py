import fnmatch
import numpy as np
import os
import cv2


def resize_it(filename):
    img = cv2.imread(filename, -1)
    ddname = 'dd_'+filename
    ubername = 'uber_'+filename
    uber_crop = cropper(img, 5/4) 
    dd_crop = cropper(img, 16/9) 
    cv2.imwrite(ubername, uber_crop)
    cv2.imwrite(ddname, dd_crop)

def cropper(img, aspect_ratio):
    height, width, channels = img.shape
    # crop height
    if (width/height)<(aspect_ratio):
        des_height = int(width/(aspect_ratio))
        crop = int((height-des_height)/2)
        crop_img = img[crop:crop+des_height,:,:]
        # cv2.imwrite('test.JPEG',crop_img)
        return crop_img

    elif (width/height)>(aspect_ratio):
        des_width = int(height*aspect_ratio)
        crop = int((width-des_width)/2)
        crop_img = img[:,crop:crop+des_width, :]
        # cv2.imwrite('test.JPEG', crop_img)
        return crop_img
    
    else:
        return img
    
    
for root, dirs, files in os.walk('.'):
    for filename in files:
        if filename.endswith(('.jpg', '.jpeg', '.png', '.JPEG')):
            resize_it(filename)
