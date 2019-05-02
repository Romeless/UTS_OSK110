import numpy as np
from toolbox import *
from PIL import Image
from segmentation import *
import cv2


def process(directory_name):
    import os
    
    path = directory_name
    
    i = 0
    #root, directory, files
    for root, d, f in os.walk(path):
        for file in f:
            filename = os.path.join(root, file)
            ext = sys.argv[2] if len(sys.argv) >= 3 else ".jpg"
            print(filename)
            
            image = Image.open(filename)
            image = np.uint8(image)
            
            ext = ".jpg"
            
            spatial = 3
            range = 1.4
            density = 100
            
            segm = Segmenter(spatial_radius=spatial, range_radius=range,
                        min_density = density)
               
            (image, labels, nb_regions) = segm.segmentate(normalize(np.array(image)).astype('uint8'))
            
            
            image = Image.fromarray(image).convert("RGB")
            
            image = resize2(np.array(image))
            
            image = cv2.Canny(image, 100, 200)
            
            image = padding(image, color=(0,0,0))
            
            image = Image.fromarray(image).convert("RGB")
            image = np.array(image)
            
            save_image((normalize(image).astype('uint8')), f"{filename}", \
                dir_name="algoritma_3",\
                info="[2]", ext=ext)
                
if __name__ == "__main__":
    import sys
    
    dir = sys.argv[1]
    
    process(dir)