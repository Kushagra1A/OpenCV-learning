import cv2 as cv

img = cv.imread('Images/waltuh.jpg')
# cv.imshow('Lady', img)
img = cv.resize(img, (800, 600))

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

print(f'No. of Faces: {len(face_rect)}')

for (x,y,w,h) in face_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

cv.imshow('Detected Faces', img)


cv.waitKey(0)
cv.destroyAllWindows()