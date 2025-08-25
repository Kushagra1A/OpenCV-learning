import cv2 as cv
import numpy as np
#we can draw and write on both normal images and blank images created using numpy!

blank = np.zeros((500,500,3), dtype='uint8') #dtype = 'uint8' is data type of an image.

# rat = cv.imread('Images/pikachu.jpg')
# cv.imshow('YELLOWRAT', rat)

# cv.imshow('Blank', blank)

blank[:] = 0 ,55,0 #green
# cv.imshow('Green', blank)
blank[200:300, 300:400] = 132,205,240
# cv.imshow('Green1', blank)

cv.rectangle(blank, (0,0), (blank.shape[0]//2, blank.shape[1]//2), (255,255,255), thickness=cv.FILLED)
# cv.imshow('Rectangle', blank)

cv.circle(blank, (blank.shape[0]//2, blank.shape[1]//2), 50, (0,0,55), thickness=-1)
# cv.imshow('Cicle', blank)

cv.line(blank, (200,300) , (400,500), (255,0,0), thickness=3)
cv.imshow('Line', blank)

cv.putText(blank, 'POLLEN BEE', (225,225), cv.FONT_HERSHEY_TRIPLEX, 0.5, (0,255,0), thickness=1)
cv.imshow('Text', blank)

cv.waitKey(0)
cv.destroyAllWindows()