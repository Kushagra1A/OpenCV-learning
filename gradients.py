import cv2 as cv

img = cv.imread('Images/pikachu.jpg')
cv.imshow('Pika', img)





cv.waitKey(0)
cv.destroyAllWindows()