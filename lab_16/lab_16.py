#To create an opencv-python program to smooth a given RGB/grayscale image by a median filter. 

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r'D:\Academy\fourth_year_2nd_semester\lab\image_processing\lap_codes\lab_16\inp3.jpeg')

blur = cv2.medianBlur(img,5)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Median Blurred')
plt.xticks([]), plt.yticks([])
plt.show()