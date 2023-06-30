import numpy as np
from PIL import Image
img = np.zeros([1000,1000,3],dtype=np.uint8)

# do logic code
# for assigning color
img[xx][yy] = np.array([255, 255, 255])



# end
im = Image.fromarray(img) #convert numpy array to image
im.show()
