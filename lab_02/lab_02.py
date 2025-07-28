import cv2
import matplotlib.pyplot as plt


img = cv2.imread(r'D:\Academy\fourth_year_2nd_semester\lab\image_processing\practice\problem_02\1713256915670.jpg', 0)

equilize_image = cv2.equalizeHist(img)

orig_img= cv2.calcHist([img],[0], None, [256], [0, 256])
eqi_image = cv2.calcHist([equilize_image],[0], None, [256], [0, 256])

plt.figure(figsize=[10,6])
plt.subplot(1,2,1)
plt.plot(orig_img)
plt.title('Original Image Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Number of pixels')

plt.subplot(1,2,2)
plt.plot(eqi_image)
plt.title('Equalized Image Histogram')  
plt.xlabel('Pixel Intensity')
plt.ylabel('Number of pixels')


plt.show()