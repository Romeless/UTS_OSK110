import numpy as np
from maskcolor import *
from toolbox import *
from PIL import Image
from thresholding import *
from corner_hyst import *

def process(directory_name):
    import os
    
    path = directory_name
    
    #root, directory, files
    for root, d, f in os.walk(path):
        for file in f:
            import matplotlib.pyplot as plt
            filename = os.path.join(root, file)
            ext = sys.argv[2] if len(sys.argv) >= 3 else ".jpg"
            print(filename)
            
            im = Image.open(filename).convert("RGB")
            im = np.uint8(im)
            
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
                
            #threshold twice
            #once to smooth the pic, another to completely split between 2 and 3
            
            threshold = 4
            im2 = level_thresh(im2, threshold)
            
            im2 = np.uint8(im2)
            im2 = im2.copy()
          
            #hysteresis the corner, open corner_hyst, good luck understanding that huehue
            im3 = np.array(im2)
            im3[im3 < im3.max()] = 0
            im3 = hysteresis_corner(im3, int(min(im3.shape) // 10))
            
            im2[im3 == 255] = 255
            
            im2 = Image.fromarray(im2).convert("RGB")
            
            im2 = resize(np.array(im2))
            
            save_image((normalize(im2).astype('uint8')), f"{filename}", \
                dir_name="algoritma_1",\
                info="[0]", ext=ext)
                
if __name__ == "__main__":
    import sys
    
    dir = sys.argv[1]
    
    process(dir)