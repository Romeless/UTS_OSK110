import numpy as np
from PIL import Image
import cv2

def level_thresh(image, level=17):
    image = np.array(image)
    if len(image.shape) > 2:
        image = grayscale(image)
    high = 255
    diff = int(high // level)
    
    while(1):
        low = high - diff if (high - diff) >= 0 else 0
        to_low = np.array([low])
        to_high = np.array([high])
        mask = cv2.inRange(image, to_low, to_high)
        image[mask > 0] = high
        high -= diff
        
        if (low <= 0):
            break
            
    return Image.fromarray(normalize(image).astype('uint8'))
    
if __name__ == "__main__":
    from toolbox import *
else:
    from toolbox import *