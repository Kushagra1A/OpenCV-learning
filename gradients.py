import cv2 as cv

img = cv.imread('Images/pikachu.jpg')
cv.imshow('Pika', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
cv.imshow('Laplacian', lap)

#sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
cv.imshow('x', sobelx)
cv.imshow('y', sobely)

combinedsobel = cv.bitwise_or(sobelx, sobely)
cv.imshow('combined', combinedsobel)

cv.waitKey(0)
cv.destroyAllWindows()