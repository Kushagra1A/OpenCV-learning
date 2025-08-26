import cv2 as cv

img = cv.imread('Images/pollenbee.jpg')
cv.imshow('Bee', img)

#averaging blur
avg = cv.blur(img, (3,3))
cv.imshow('Average', avg)

#gaussian blur
gaus = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow('Gauss', gaus)

#median blur
median = cv.medianBlur(img, 3)
cv.imshow('Median', median)

#bilateral filterning
bifil = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('bifil', bifil)

cv.waitKey(0)
cv.destroyAllWindows()