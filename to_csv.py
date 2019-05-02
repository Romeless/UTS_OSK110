from PIL import Image
import numpy as np
import os
import sys

def to_scv(directory_names):
    loc = os.getcwd()

    i = 0

    csv = open("data.csv", "w+")
    
    for folder in directory_names:
        for r, d, f in os.walk(os.path.join(loc,folder)):
            for file in f:
                if '.jpg' in file:
                    filename = os.path.join(r,file)
                    
                    img = Image.open(filename).convert("LA")
                    img = np.array(img)
                    
                    csv.write(f"{d},")
                    
                    img2 = img.flatten().tolist()
                    
                    csv.write(str(img2).strip('[]'))
                    csv.write("\n")
                    
                    Image.fromarray(img).convert("RGB").save("udang\\train\\{}\\{}{}".format(d, i, ".jpg"))
                    
                    i += 1