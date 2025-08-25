import cv2 as cv
import numpy as np

img = cv.imread('Images/squirtle.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)
blur = cv.GaussianBlur(gray, (3,3), cv.BORDER_DEFAULT)
#cv.imshow('blurred', blur)
canny = cv.Canny(blur, 125, 175)
#cv.imshow('Edges', canny)

blank = np.zeros((img.shape[0], img.shape[1], 3), dtype = 'uint8')
#cv.imshow('Blank', blank)

contours, hierarchy = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)

print(f'{len(contours)} contour(s) found!')

cv.waitKey(0)