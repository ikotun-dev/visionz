import cv2 as cv
img = cv.imread('images/IMG_2529.JPG')

cv.imshow('FIRST', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow('blur', blur)
#
# canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny', canny)

ret, thres = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thres', thres)

contours, heirachies = cv.findContours(thres, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f"{len(contours)} contour(s) found")
cv.waitKey(0)