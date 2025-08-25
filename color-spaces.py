import cv2 as cv

img = cv.imread('Images/boston-fall.jpg')
cv.imshow('boston', img)

cv.waitKey(0)
cv.destroyAllWindows()