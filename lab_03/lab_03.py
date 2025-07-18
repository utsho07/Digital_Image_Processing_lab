#To create an opencv-python program in order to convert a given RGB/grayscale image to a negative image.
import cv2
import numpy as np

# Hardcoded image path (Change this to your image path)
IMAGE_PATH = "rgb.jpg"  # or "grayscale.jpg"

# Read the image (automatically detects color/grayscale)
img = cv2.imread(r'D:\Academy\fourth_year_2nd_semester\lab\image_processing\lap_codes\lab_03\rgb.jpg', cv2.IMREAD_UNCHANGED)

# Calculate negative (works for both RGB and grayscale)
negative = 255 - img

# Save the negative image
output_path = IMAGE_PATH.rsplit('.', 1)[0] + '_inverted.png'
cv2.imwrite(output_path, negative)

# Display the negative image
cv2.imshow('Negative Image', negative)
cv2.waitKey(0)
cv2.destroyAllWindows()