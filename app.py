import fnmatch
import numpy as np
import os
import cv2
import argparse


def resize_it(filename):
    img = cv2.imread(filename, -1)
    ddname = 'dd_'+filename
    ubername = 'uber_'+filename
    if args.pad:
        uber_pad = padder(img, 5/4)
        dd_pad = padder(img, 16/9)
        if 'reduce' in args:
            uber_pad, dd_pad = reducer(uber_pad, dd_pad)
        cv2.imwrite(ubername, uber_pad)
        cv2.imwrite(ddname, dd_pad)
    else: 
        uber_crop = cropper(img, 5/4) 
        dd_crop = cropper(img, 16/9) 
        if 'reduce' in args:
            uber_crop, dd_crop = reducer(uber_crop, dd_crop)
        cv2.imwrite(ubername, uber_crop)
        cv2.imwrite(ddname, dd_crop)

def reducer(uber_img, dd_img):
        uh, uw = (int(uber_img.shape[0]*(args.reduce/100)),int(uber_img.shape[1]*(args.reduce/100)))
        dh, dw = (int(dd_img.shape[0]*(args.reduce/100)),int(dd_img.shape[1]*(args.reduce/100)))
        udim = (uw, uh)
        ddim = (dw, dh)
        resized_uber_img = cv2.resize(uber_img, udim, interpolation= cv2.INTER_AREA)
        resized_dd_img = cv2.resize(dd_img, ddim, interpolation=cv2.INTER_AREA)
        return resized_uber_img, resized_dd_img
                  
def cropper(img, aspect_ratio):
    height, width, channels = img.shape
    # crop height
    if (width/height)<(aspect_ratio):
        des_height = int(width/(aspect_ratio))
        crop = int((height-des_height)/2)
        crop_img = img[crop:crop+des_height,:,:]
        return crop_img
    # crop width
    elif (width/height)>(aspect_ratio):
        des_width = int(height*aspect_ratio)
        crop = int((width-des_width)/2)
        crop_img = img[:,crop:crop+des_width, :]
        return crop_img
    
    else:
        return img
    
def padder(img, aspect_ratio):
    height, width, channels = img.shape
    color = [255,255,255]
    if (width/height)<(aspect_ratio):
        des_width = int(height*aspect_ratio)
        pad = int((des_width - width)/2)
        top, bottom = (0, 0)
        left, right = (pad, pad)
        padded_image = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)
        return padded_image

    if (width/height)>(aspect_ratio):
        des_height = int((width/aspect_ratio))
        pad = int((des_height - height)/2)
        top, bottom = (pad, pad)
        left, right = (0, 0)
        padded_image = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)
        return padded_image

    else:
        return img
        

parser = argparse.ArgumentParser(description="To quickly format multiple images for listings on UberEats and DoorDash")
parser.add_argument("-p", "--pad", action="store_true", default=False, help="Change the functionality from cropping images to padding with whitespace")
parser.add_argument("-r", "--reduce", type=int, help="Scales the image down by the input percentage.")
args = parser.parse_args()

for root, dirs, files in os.walk('.'):
    for filename in files:
        if filename.endswith(('.jpg', '.jpeg', '.png', '.JPEG')):
            resize_it(filename)
