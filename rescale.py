import cv2 as cv

def rescaleFrame(frame , scale = 0.5): #default value
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# def changeRes(width,height):
#     capture.set(3,width)
#     capture.set(4,height)

    
# cat = cv.imread('Images/cat_large.jpg')
# cv.imshow('Image' , cat)

# resized_cat = rescaleFrame(cat)
# cv.imshow("image2" , resized_cat)

# cv.waitKey(0)

earthvid = cv.VideoCapture("Videos/sample.mp4")

while True:
    isTrue, frame = earthvid.read()
    resizedvid = rescaleFrame(frame)
    if not isTrue:
        break
    cv.imshow('vid',frame)
    cv.imshow('resized',resizedvid)

    if cv.waitKey(10) & 0XFF == ord('d'):
        break

cv.destroyAllWindows()    