import cv2 as cv
# img = cv.imread('images/IMG_2529.JPG')
#
# cv.imshow('FIRST', img)
capture = cv.VideoCapture('videos/Typ.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()


#cv.waitKey(0)
