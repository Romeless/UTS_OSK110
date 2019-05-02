import numpy as np
from toolbox import *
from PIL import Image
from luthfi import *

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
            
            res = proc(filename)
            res = Image.fromarray((normalize(res).astype('uint8'))).convert("RGB")
            
            res = np.array(res)
            
            res = Image.fromarray(res).convert("RGB")
            
            res = resize(np.array(res))
            
            save_image((normalize(res).astype('uint8')), f"{filename}", \
                dir_name="algoritma_2",\
                info="[1]", ext=ext)
                
if __name__ == "__main__":
    import sys
    
    dir = sys.argv[1]
    
    process(dir)