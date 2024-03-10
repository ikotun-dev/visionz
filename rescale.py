import cv2 as cv
img = cv.imread('images/IMG_2529.JPG')

cv.imshow('FIRST', img)

def rescaleFrame(frame, scale=0.75):
    #Images, Videos and Live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def change_res(width, height):
    #Live video
    capture.set(3, width)
    capture.set(4, height)



capture = cv.VideoCapture('videos/Typ.mp4')
while True:
    isTrue, frame = capture.read()

    frameResized = rescaleFrame(frame, scale=0.2)
    cv.imshow('Video', frame)
    cv.imshow('Video', frameResized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
