from PIL import Image
import numpy as np

def preprocess(directory):
    import os
    
    path = diretory
    for r, d, f in os.walk(path):
        for file in f:
            if '.jpg' in file:
                size = 100
                filename = os.path.join(r,file)
                print(filename)
                
                old_image = Image.open(filename).convert("RGB")
                h, w = old_image.size
                
                
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
                new_im.paste((255, 255, 255), [0,0, new_size[0], new_size[1]])
                new_im.paste(old_image, (int((new_size[0]-old_size[0])/2),
                                      int((new_size[1]-old_size[1])/2)))
                
                new_im.save(filename)