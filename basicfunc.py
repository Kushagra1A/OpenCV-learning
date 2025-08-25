import cv2 as cv

img = cv.imread('Images/squirtle.jpg')
# cv.imshow('squirtle', img)

# grayimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('graysquirtle', grayimg)

blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow('blur', blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow('edges', canny)
# a blurred image will catch less edges than compared to a normal image

dilated = cv.dilate(canny, (5,5), iterations=3)
cv.imshow('Dilate', dilated)

eroded = cv.erode(dilated, (5,5), iterations=3)
cv.imshow('Eroded', eroded)

resized = cv.resize(img, (720,600))
cv.imshow('Resized', resized)

cropped = img[50:200, 200:400]
cv.imshow('crop', cropped)

cv.waitKey(0)
cv.destroyAllWindows()