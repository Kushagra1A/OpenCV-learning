import cv2 as cv

img = cv.imread('Images/pollenbee.jpg')
cv.imshow('bee', img)

# #BGR to Grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Grayscaled', gray)

# #BGR to HSV
# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('HSV', hsv)

# lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('LAB', lab)

# l, a, b = cv.split(lab)
# cv.imshow('L', l)
# cv.imshow('A', a)
# cv.imshow('B', b)

#BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

cv.waitKey(0)
cv.destroyAllWindows()