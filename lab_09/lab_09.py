#To create an opencv-python program to segment a given RGB/grayscale image based on K-means algorithm.
import matplotlib as plt
import numpy as np
import cv2
path = r'D:\Academy\fourth_year_2nd_semester\lab\image_processing\lap_codes\lab_09\itsohk.png'
img = cv2.imread(path)

# Preprocessing the Image

img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
twoDimage = img.reshape((-1,3))
twoDimage = np.float32(twoDimage)

# Defining Parameters
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 2
attempts=10

# Apply K-Means

ret,label,center=cv2.kmeans(twoDimage,K,None,criteria,attempts,cv2.KMEANS_PP_CENTERS)
center = np.uint8(center)
res = center[label.flatten()]
result_image = res.reshape((img.shape))

# Image Show
cv2.imshow('image', result_image)

# waits for user to press any key
# (this is necessary to avoid Python kernel form crashing)
cv2.waitKey(0)

# closing all open windows
cv2.destroyAllWindows()
