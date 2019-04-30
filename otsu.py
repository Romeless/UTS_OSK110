import numpy as np
from PIL import Image

def otsu_method(im):
    im = np.array(im)
    im = normalize(im).astype('int32')
    total_pixel = im.shape[0] * im.shape[1]
    mean_denom = 1.0 / total_pixel
    hist, bins = np.histogram(im, np.arange(0,257))
    final_thresh = -1
    final_value = -1
    intensity_arr = np.arange(256)
    for t in bins[1:-1]:
        pcb = np.sum(hist[:t])
        pcf = np.sum(hist[t:])
        Wb = pcb * mean_denom
        Wf = pcf * mean_denom

        mub = np.sum(intensity_arr[:t]*hist[:t]) / float(pcb)
        muf = np.sum(intensity_arr[t:]*hist[t:]) / float(pcf)
        #print mub, muf
        value = Wb * Wf * (mub - muf) ** 2

        if value > final_value:
            final_thresh = t
            final_value = value
    return np.round(255 / (final_thresh / 2)).astype('int32')
    
if __name__ == "__main__":
    from toolbox import *
else:
    from lib.toolbox import *