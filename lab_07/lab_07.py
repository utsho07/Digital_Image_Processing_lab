#To create an opencv-python program to segment a given RGB/grayscale image based on thresholding. 

#Import libraries and Images
import cv2
path=r'D:\Academy\fourth_year_2nd_semester\lab\image_processing\lap_codes\lab_07\itsohk.png'
img = cv2.imread(path)
#Preprocessing the Imagef
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  #BGR → RGB Conversion: OpenCV reads images as BGR, but converting to RGB is useful for display (e.g., in matplotlib).

# Convert RGB to HSV
# HSV (Hue, Saturation, Value) is often better for color segmentation than RGB.
hsv_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2HSV)


#Define the Color Range to be Detected
light_blue = (90, 70, 50)
dark_blue = (128, 255, 255)
# You can use the following values for green
# light_green = (40, 40, 40)
# dark_green = (70, 255, 255)


mask = cv2.inRange(hsv_img, light_blue, dark_blue)

# Apply the Mask
result = cv2.bitwise_and(img, img, mask=mask)

# Image Show
cv2.imshow('image', result)
  
#waits for user to press any key 
#(this is necessary to avoid Python kernel form crashing)
cv2.waitKey(0) 
  
#closing all open windows 
cv2.destroyAllWindows() 