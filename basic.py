import cv2 as cv
img = cv.imread('images/IMG_2529.JPG')

cv.imshow('FIRST', img)

# grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

# Edge cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny', canny)

# Dilating the image
dilated = cv.dilate(canny, (3,3), iterations=2)

cv.waitKey(0)