import cv2

img = cv2.imread(r'D:\Academy\fourth_year_2nd_semester\lab\image_processing\practice\problem_07\itsohk.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
theshold_value = 127

_, thesholded = cv2.threshold(gray, theshold_value, 255, cv2.THRESH_BINARY )

cv2.imshow('original image', img)
cv2.imshow('Thesholed image', thesholded)
cv2.waitKey(0)
