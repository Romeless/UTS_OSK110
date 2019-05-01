from PIL import Image
import numpy as np
from toolbox import *

if __name__ == "__init__":
    import os
    import sys
    
    path = sys.argv[1]
    
    for r, d, f in os.walk(path):
        for file in f:
            filename = os.path.join(r,file)
            
            im = Image.open(filename)
            
            rot90 = im.transpose(Image.ROTATE_90)
            rot180 = im.transpose(Image.ROTATE_180)
            rot270 = im.transpose(Image.ROTATE_270)

            
            
            save_image(rot90, filename, info="rot90")
            save_image(rot180, filename, info="rot180")
            save_image(rot270, filename, info="rot270")
            