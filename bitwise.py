import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
# cv.imshow('RECTANGLE', rectangle)

circle = cv.circle(blank, (200,200), 200, 255, -1)
# cv.imshow('CIRCLE', circle)

#bitwise AND
bit_and = cv.bitwise_and(rectangle, circle)
cv.imshow('AND', bit_and)

#bitwise OR
bit_or = cv.bitwise_or(rectangle, circle)
cv.imshow('OR', bit_or)

#bitwise XOR
bit_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('XOR', bit_xor)

#bitwise NOT
bit_not = cv.bitwise_not(circle)
cv.imshow('NOT', bit_not)

#personal experimentation

# img1 = cv.imread('Images/bee.jpg')
# img2 = cv.imread('Images/pollenbee.jpg')

# img3 = cv.resize(img1, (200,200))
# img4 = cv.resize(img2, (200, 200))

# beeand = cv.bitwise_and(img3, img4)
# beeor = cv.bitwise_or(img3, img4)
# beexor = cv.bitwise_xor(img3, img4)

# cv.imshow('BEEAND', beeand)
# cv.imshow('BEEOR', beeor)
# cv.imshow('BEEXOR', beexor)

cv.waitKey(0)
cv.destroyAllWindows()