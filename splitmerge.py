import cv2 as cv
import numpy as np

img = cv.imread('Images/pikachu.jpg')
cv.imshow('image', img)

blank = np.zeros((img.shape[0], img.shape[1]), dtype = 'uint8')

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Grayscaled', gray)

b,g,r = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('blue', blue)
cv.imshow('green', green)
cv.imshow('red', red)

# mergedimg = cv.merge([b,g,r])
# cv.imshow('merged', mergedimg)


cv.waitKey()
cv.destroyAllWindows()