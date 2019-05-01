import numpy as np
import cv2
from PIL import Image
from toolbox import *

def hysteresis_corner(img, ran=1):
    import sys
    sys.setrecursionlimit(1500)
    img = np.array(img).astype('uint8')
    nrow, ncol = img.shape
    print(img.max(), img.min())
    for j in range(ran):
        for i in range(1, nrow-2):
            rec = 0
            limit = False
            if img[i, 1+j] == 0:
                img[i, 1+j] = 255
                (img, rec, last_i, last_j, limit) = spreading(img, i, 1+j, rec, False)
            if img[i, ncol-2-j] == 0:
                img[i, ncol-2-j] = 255
                (img, rec, last_i, last_j, limit) = spreading(img, i, ncol-2-j, rec, False)
            while limit:
                print("limit bang?")
                rec = 0
                img[last_i, last_j] = 255
                (img, rec, last_i, last_j, limit) = spreading(img, last_i, last_j, rec, False)
    for i in range(ran):    
        for j in range(1, ncol-2):
            rec = 0
            limit = False
            if img[1+i, j] == 0:
                img[1+i, j] = 255
                (img, rec, last_i, last_j, limit) = spreading(img, 1+i, j, rec, False)
            if img[nrow-2-i, j] == 0:
                img[nrow-2-i, j] = 255
                (img, rec, last_i, last_j, limit) = spreading(img, nrow-2-i, j, rec, False)
            while limit:
                print("limit bang?")
                rec = 0
                img[last_i, last_j] = 255
                (img, rec, last_i, last_j, limit) = spreading(img, last_i, last_j, rec, False)
    return img
    
def spreading(img, loc_i, loc_j, rec, limit):
    try:
        for i in range(-1,2):
            for j in range(-1,2):
                try:
                    if rec >= 1400:
                        return (img, rec, loc_i, loc_j, True)
                    if img[loc_i + i,loc_j + j] == 0:
                        #print("[{}:{}]".format(loc_i + i, loc_j + j))
                        rec += 1
                        img[loc_i + i,loc_j + j] = 255
                        (img, rec, last_i, last_j, limit) = spreading(img, loc_i + i, loc_j + j, rec, False)
                except IndexError:
                    return (img, rec, loc_i, loc_j, limit)
    except RecursionError:
        print(rec)
        return (img, rec, loc_i, loc_j, True)
    return (img, rec, loc_i, loc_j, limit)