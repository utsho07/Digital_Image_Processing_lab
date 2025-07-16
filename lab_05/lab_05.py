#To create an opencv-python program to enhance brightness of a given RGB/grayscale image.

from PIL import Image
from PIL import ImageEnhance

# Opens the image file
image = Image.open(r'D:\Academy\fourth_year_2nd_semester\lab\image_processing\lap_codes\lab_05\gfg.png')

# shows image in image viewer
image.show()


# Enhance Brightness
curr_bri = ImageEnhance.Brightness(image)
new_bri = 2.5

# Brightness enhanced by a factor of 2.5
img_brightened = curr_bri.enhance(new_bri)

# shows updated image in image viewer
img_brightened.show()
