# To create an opencv-python program to smooth a given RGB/grayscale image by an average filter. 
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r'D:\Academy\fourth_year_2nd_semester\lab\image_processing\lap_codes\lab_14\inp3.jpeg')

blur = cv2.blur(img,(5,5))

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Average Blurred')
plt.xticks([]), plt.yticks([])
plt.show()