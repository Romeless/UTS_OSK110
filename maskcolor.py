import numpy as np
import cv2
from PIL import Image

def mask_shadow(im, rgb_color):
    return mask_color(im, rgb_color, s=20, v=20, high_s=100, high_v=100)
    
def mask_color(im, rgb_color, s=100, v=100, high_s=255, high_v=255, range=15):
    # import matplotlib.pyplot as plt
    
    im = np.uint8(im)
    
    rgb_color = np.uint8(rgb_color)
    hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    
    hsv_color = cv2.cvtColor(cv2.UMat(rgb_color), cv2.COLOR_BGR2HSV)
    hsv_color = hsv_color.get()
    low = np.array([hsv_color[0][0][0] - range, s, v])
    high = np.array([hsv_color[0][0][0] + range, high_s, high_v])
    
    mask = cv2.inRange(hsv, low, high)
    
    res = cv2.bitwise_and(im, im, mask=mask)
    im2 = im.copy()
    im2[res != 0] = 255
    return im2
    
if __name__ == "__main__":  
    from toolbox import *
    import sys
    import matplotlib.pyplot as plt
    if len(sys.argv) >= 2:
        img = Image.open(sys.argv[1]).convert("RGB")
        red = sys.argv[2] if len(sys.argv) >= 5 else 255
        green = sys.argv[3] if len(sys.argv) >= 5 else 255
        blue = sys.argv[4] if len(sys.argv) >= 5 else 255
        s = int(sys.argv[5]) if len(sys.argv) >= 7 else 100
        v = int(sys.argv[6]) if len(sys.argv) >= 7 else 100
        high_s = int(sys.argv[7]) if len(sys.argv) >= 9 else 255
        high_v = int(sys.argv[8]) if len(sys.argv) >= 9 else 255
        
        rgb = np.uint8([[[red, green, blue]]])
        
        
        masked = mask_color(img, [[[255,0,0]]]) #, s, v, high_s, high_v)
        masked = mask_color(masked, [[[0,255,0]]])
        masked = mask_color(masked, [[[0,0,255]]])
        masked = mask_color(masked, [[[10,10,20]]], v=10, high_v=100)
        masked = mask_color(masked, [[[200,180,150]]], s=70, high_s=255)
        plt.show()
else:
    from toolbox import *