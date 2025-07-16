#To create an opencv-python program to enhance color of a given RGB/grayscale image.

from PIL import Image
from PIL import ImageEnhance

# Opens the image file
image = Image.open(r'D:\Academy\fourth_year_2nd_semester\lab\image_processing\lap_codes\lab_04\gfg.png')

# shows image in image viewer
image.show()


# Enhance Color Level
curr_col = ImageEnhance.Color(image)
new_col = 2.5

# Color level enhanced by a factor of 2.5
img_colored = curr_col.enhance(new_col)

# shows updated image in image viewer
img_colored.show()
