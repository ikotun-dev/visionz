import cv2 as cv
img = cv.imread('images/IMG_2529.JPG')

cv.imshow('FIRST', img)

# gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# hsv
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

