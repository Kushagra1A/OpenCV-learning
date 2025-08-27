import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('Images/boston-fall.jpg')
img = cv.resize(img, (800,500))
cv.imshow('BOSTON', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# #gray histogram
# ghist = cv.calcHist([gray], [0], None, [256], [0,256])

# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(ghist)
# plt.xlim(0,256)
# plt.show()

blank = np.zeros((500,800), dtype='uint8')
rect = cv.rectangle(blank, (280, 150), (520, 250), 255, -1)
cv.imshow('Rect', rect)

mask = cv.bitwise_and(gray, gray, mask=rect)
cv.imshow('MASKED IMG', mask)

# ghist = cv.calcHist([gray], [0], rect, [256], [0,256])

# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(ghist)
# plt.xlim(0,256)
# plt.show()

plt.figure()
plt.title('Colored Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
for i,color in enumerate(colors):
    hist = cv.calcHist([img], [i], rect, [256], [0,256])
    plt.plot(hist, color= color)
    plt.xlim([0, 256])

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
