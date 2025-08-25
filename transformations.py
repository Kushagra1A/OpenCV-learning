import cv2 as cv
import numpy as np

img = cv.imread('Images/pikachu.jpg')
cv.imshow('boston', img)

def translate(img, x, y):
    transmatrix = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transmatrix, dimensions)

# translatedimg = translate(img, -100, -100)
# cv.imshow('Trans', translatedimg)

def rotation(img, angle, rotPoint=None):
    (height, width) = (img.shape[0], img.shape[1])
    if rotPoint is None:
        rotPoint = (height//2, width//2)
    rotMatrix = cv.getRotationMatrix2D(rotPoint, angle, 1.0)

    dimensions = (height, width)

    return cv.warpAffine(img, rotMatrix, dimensions)



# rotimg = rotation(img, 45)
# cv.imshow('rotation', rotimg)

# rotrotimg = rotation(rotimg, 120)
# cv.imshow('rotrotation', rotrotimg)

# resized = cv.resize(rotimg, (200,200), interpolation=cv.INTER_CUBIC)
# cv.imshow('resized', resized)

flip = cv.flip(img, -1)
cv.imshow('Flipped', flip)

cv.waitKey(0)