import cv2 as cv

# img = cv.imread("Images/pikachu.jpg")

# cv.imshow('pikachu' , img)

capearth = cv.VideoCapture('Videos/sample.mp4')

while True:
    isTrue, frame = capearth.read() #capture.read() return 2 values 
    if not isTrue:
        break
    cv.imshow('Video' , frame)

    if cv.waitKey(100) & 0xFF == ord("d"):
        break

capearth.release()
cv.destroyAllWindows()