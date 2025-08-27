import cv2 as cv
import numpy as np

img = cv.imread('Images/bee.jpg')
# cv.imshow('bee', img)

blank = np.zeros((img.shape[0], img.shape[1]), dtype = 'uint8')
# cv.imshow('Blank', blank)

rect = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
cv.imshow('Rectangle', rect)

circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 200, 255, -1)
cv.imshow('Circle', circle)

wshape = cv.bitwise_or(rect, circle)
cv.imshow('wshape', wshape)

maskedimg = cv.bitwise_and(img,img, mask=rect)
cv.imshow('MASKED', maskedimg)
maskedimg1 = cv.bitwise_and(img,img, mask=circle)
cv.imshow('MASKED1', maskedimg1)
maskedimg2 = cv.bitwise_and(img,img,mask=wshape)
cv.imshow('MASKED2', maskedimg2)


cv.waitKey(0)
cv.destroyAllWindows()
