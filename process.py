import numpy as np
from maskcolor import *
from toolbox import *
from PIL import Image
from thresholding import *
from corner_hyst import *

if __name__ == "__main__":
    import os
    import sys
    
    path = sys.argv[1]
    
    #root, directory, files
    for root, d, f in os.walk(path):
        for file in f:
            filename = os.path.join(root, file)
            im = Image.open(filename).convert("RGB")
            im = np.uint(im)
            
            ext = sys.argv[2] if len(sys.argv) >= 3 else ".jpg"
            im2 = im.copy()
            
            #get the colors from color.txt
            file = open("colors.txt", "r")
            i = 0
            for colors in file.readlines():
                split_color = colors.split()
                
                #split the line, R G B Low_Saturation High_Saturation Low_V High_V
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
                
                #save_image((normalize(im2).astype('uint8')), filename,info=\
                #"[0][{}]-[{},{},{}][{}-{}][{}-{}][{}]"\
                #.format(i, r, g, b, l_s, h_s, l_v, h_s, ran), ext=ext)
                
                i+=1
            
            #threshold twice
            #once to smooth the pic, another to completely split between 2 and 3
            
            threshold = 4
            im2 = level_thresh(im2, threshold)
            
            im2 = level_thresh(im2, 2)
            
            im2 = np.uint8(im2)
            
            #save_image((normalize(im2).astype('uint8')), filename,info=\
            #    "[1][thresholding]", ext=ext)
                
            #hysteresis the corner, open corner_hyst, good luck understanding that huehue
            im3 = np.array(im2)
            im3[im3 < im3.max()] = 0
            im3 = hysteresis_corner(im3, int(min(im3.shape) // 10))
            
            save_image((normalize(im3).astype('uint8')), filename,info=\
                "[2][corner hysteresis]", ext=ext)
        