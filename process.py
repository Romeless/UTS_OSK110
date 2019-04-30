import numpy as np
from maskcolor import *
from toolbox import *
from PIL import Image
from thresholding import *
from corner_hyst import *

if __name__ == "__main__":
    import sys
    import matplotlib.pyplot as plt
    
    im = Image.open(sys.argv[1]).convert("RGB")
    im = np.uint(im)
    ext = sys.argv[2] if len(sys.argv) >= 3 else ".jpg"
    im2 = im.copy()
    
    #get the colors from color.txt
    file = open("colors.txt", "r")
    i = 0
    for colors in file.readlines():
        split_color = colors.split()
        
        #split the line, R G B Low_Saturation High_Saturation Low_V High_V Range
        #i forgot what V is
        r = int(split_color[0])
        g = int(split_color[1])
        b = int(split_color[2])
        l_s = int(split_color[3])
        h_s = int(split_color[4])
        l_v = int(split_color[5])
        h_v = int(split_color[6])
        ran = int(split_color[7])
        
        rgb = np.uint8([[[r,g,b]]])
        
        im2 = mask_color(im2, rgb, s=l_s, v=l_v, high_s=h_s, high_v=h_v, range=ran)
        
        Image.fromarray(normalize(im2).astype('uint8'))\
        .save("output\{}[0][{}]-[{},{},{}][{}-{}][{}-{}][{}]{}"\
        .format(sys.argv[1], i, r, g, b, l_s, h_s, l_v, h_s, ran, ext))
        
        i+=1
    
    #threshold twice
    #once to smooth the pic, another to completely split between 0 and 255
    
    threshold = 4
    im2 = level_thresh(im2, threshold)
    
    im2 = level_thresh(im2, 2)
    
    im2 = np.uint8(im2)
    Image.fromarray(normalize(im2).astype('uint8'))\
        .save("output\{}[1][thresholding]{}"\
        .format(sys.argv[1], ext))
    
    #hysteresis the corner, open corner_hyst, good luck understanding that huehue
    im3 = np.array(im2)
    im3[im3 < im3.max()] = 0
    im3 = hysteresis_corner(im3)
    
    Image.fromarray(normalize(im3).astype('uint8'))\
        .save("output\{}[2][hysteresis]{}"\
        .format(sys.argv[1], ext))
