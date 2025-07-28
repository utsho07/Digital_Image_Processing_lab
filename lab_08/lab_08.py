import cv2

img = cv2.imread(r'problem_08/itsohk.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh =cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

contour_img = cv2.drawContours(img.copy(), contours, -1, (0, 255, 0), 2)


cv2.imshow("Original", img  )
cv2.imshow("Thresholded", thresh)
cv2.imshow("Contours", contour_img)
cv2.waitKey(0)