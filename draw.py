import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

#Paint a certain colour
blank[:] = 0,255,255
cv.imshow('Green', blank)
#Rectangle
cv.rectangle(blank, (0,0), (250, 250), (0,255,0), thickness=2)
cv.imshow('Rectangle', blank)

#Circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=3)
cv.imshow('Circle', blank)
cv.waitKey(0)

