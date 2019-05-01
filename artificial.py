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
            
            