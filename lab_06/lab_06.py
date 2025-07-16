#To create an opencv-python program to enhance contrast of a given RGB/grayscale image. 

from PIL import Image
from PIL import ImageEnhance

# Opens the image file
image = Image.open(r'D:\Academy\fourth_year_2nd_semester\lab\image_processing\lap_codes\lab_06\gfg.png')

# shows image in image viewer
image.show()


# Enhance Contrast
curr_con = ImageEnhance.Contrast(image)
#new_con = 0.3
new_con = 8.3

# Contrast enhanced by a factor of 0.3
img_contrasted = curr_con.enhance(new_con)

# shows updated image in image viewer
img_contrasted.show()
