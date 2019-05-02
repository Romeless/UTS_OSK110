from PIL import Image
import numpy as np
from toolbox import *

def artificial(directory_name):
    import os
    
    path = sys.argv[1]
    
    for r, d, f in os.walk(path):
        for file in f:
            if '.jpg' in file:
                filename = os.path.join(r,file)
                print(filename)
                
                im = Image.open(filename)
                
                rot90 = np.array(im.transpose(Image.ROTATE_90))
                rot180 = np.array(im.transpose(Image.ROTATE_180))
                rot270 = np.array(im.transpose(Image.ROTATE_270))
                
                print(d)
                save_image(np.array(im), f"{filename}", dir_name=f"artificial", info="ori")
                save_image(rot90, f"{filename}", dir_name=f"artificial", info="rot90")
                save_image(rot180, f"{filename}", dir_name=f"artificial", info="rot180")
                save_image(rot270, f"{filename}", dir_name=f"artificial", info="rot270")

if __name__ == "__main__":
    
    import sys
    
    dir_name = sys.argv[1]
    
    artificial(dir_name)