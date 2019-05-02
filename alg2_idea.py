import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

def proc(image):
    
    im2 = mpimg.imread(image)
    
    gray_im2 = rgb2gray(im2)
    gray_im2 = gray_im2 * 255
    
    hi,lo = ntah(gray_im2)
    
    s,w = threshold(gray_im2,lo,hi)
    
    new_s = s / 2
    new_w = w + new_s
    
    m,n = gray_im2.shape
    result = np.zeros((m,n,3))
    result[:,:,0] = new_s
    result[:,:,1] = (new_s + new_w) > 0
    result[:,:,2] = new_w
    
    return result

def enhance(image, clip_limit=3):
    
    # convert image to LAB color model
    image_lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

    # split the image into L, A, and B channels
    l_channel, a_channel, b_channel = cv2.split(image_lab)

    # apply CLAHE to lightness channel
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=(8, 8))
    cl = clahe.apply(l_channel)

    # merge the CLAHE enhanced L channel with the original A and B channel
    merged_channels = cv2.merge((cl, a_channel, b_channel))

    # convert iamge from LAB color model back to RGB color model
    final_image = cv2.cvtColor(merged_channels, cv2.COLOR_LAB2BGR)
    
    return final_image

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])
    
def otsu(gray):
    pixel_number = gray.shape[0] * gray.shape[1]
    mean_weigth = 1/pixel_number
    his, bins = np.histogram(gray, np.array(range(0, 256)))
    final_thresh = 0
    final_value = 0
    for t in bins[1:-1]: # This goes from 1 to 254 uint8 range (Pretty sure wont be those values)
        Wb = np.sum(his[:t]) * mean_weigth
        Wf = np.sum(his[t:]) * mean_weigth

        mub = np.mean(his[:t])
        muf = np.mean(his[t:])

        value = Wb * Wf * (mub - muf) ** 2
        print (value)

        #print("Wb", Wb, "Wf", Wf)
        #print("t", t, "value", value)
        
    if value > final_value:
        final_thresh = t
        final_value = value
    
    return final_value,final_value*0.2
            #for hi    for lo

def threshold(img, lo = 30, hi=130):
    strong = img > hi
    weak = img< lo
    return strong, weak


def ntah (img):
    count = 0
    for x in img:
        for y in x:
            count = count + y
    m,n = img.shape
    hi = count /(m*n)
    return hi,hi*0.2

def resize(img):
    old_image = Image.fromarray(img).convert("RGB")
    
    h, w = old_image.size
    size = 100
    
    denum_h = h / size
    denum_w = w / size
    denum = 0
    if denum_h > denum_w:
        denum = denum_h
    else:
        denum = denum_w

    old_image = old_image.resize((int(h // denum), int(w//denum)))
    old_size = old_image.size
        
    mx = np.array(old_image).max()
        
    new_size = (size,size)
    new_im = Image.new("RGB", new_size)
    new_im.paste((129, 253, 133), [0,0, new_size[0], new_size[1]])
    new_im.paste(old_image, (int((new_size[0]-old_size[0])/2),
                          int((new_size[1]-old_size[1])/2)))
        
    return(np.array(new_im))
