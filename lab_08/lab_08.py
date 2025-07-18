#To create an opencv-python program to segment a given RGB/grayscale image based on the contour detection algorithm.
# Importing libraries and Images.
import cv2
import matplotlib.pyplot as plt
import numpy as np
path = r'D:\Academy\fourth_year_2nd_semester\lab\image_processing\lap_codes\lab_08\itsohk.png'
img = cv2.imread(path)
img = cv2.resize(img,(256,256))

# Preprocessing the Image
#cv2.cvtColor(img, cv2.COLOR_RGB2GRAY): Converts the image to grayscale (needed for most OpenCV operations).
#cv2.threshold: Converts the grayscale image to a binary image (black and white) using the mean pixel value as the threshold. cv2.THRESH_BINARY_INV inverts the result (so objects become white, background black).
#cv2.Canny: Detects edges in the binary image.
#cv2.dilate: Makes the edges thicker, which helps in finding contours.
#cv2.imshow('image 1', edges): Shows the edge-detected image.
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
_,thresh = cv2.threshold(gray, np.mean(gray), 255, cv2.THRESH_BINARY_INV)
edges = cv2.dilate(cv2.Canny(thresh,0,255),None)
# Image Show
cv2.imshow('image 1', edges)

# waits for user to press any key
# (this is necessary to avoid Python kernel form crashing)
#cv2.waitKey(0)

# closing all open windows
#cv2.destroyAllWindows()

#Detecting and Drawing Contours

cnt = sorted(cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2], key=cv2.contourArea)[-1]
mask = np.zeros((256,256), np.uint8)
masked = cv2.drawContours(mask, [cnt],-1, 255, -1)

# Image Show
cv2.imshow('image 2', masked)

# waits for user to press any key
# (this is necessary to avoid Python kernel form crashing)
#cv2.waitKey(0)

# closing all open windows
#cv2.destroyAllWindows()

# Segmenting the Regions

dst = cv2.bitwise_and(img, img, mask=mask)
segmented = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)

# Image Show
cv2.imshow('image 3', segmented)

# waits for user to press any key
# (this is necessary to avoid Python kernel form crashing)
cv2.waitKey(0)

# closing all open windows
cv2.destroyAllWindows()




