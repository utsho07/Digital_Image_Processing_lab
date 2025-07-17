# To create an opencv-python program to smooth a given RGB/grayscale image by a 2Dfilter. 

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r'D:\Academy\fourth_year_2nd_semester\lab\image_processing\lap_codes\lab_12\inp3.jpeg')

kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('2D Filter Averaging')
plt.xticks([]), plt.yticks([])
plt.show()