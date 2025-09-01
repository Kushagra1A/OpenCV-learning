import numpy as np
import cv2 as cv
import os

haar_cascade = cv.CascadeClassifier('haar_faces.xml')

people = []
for i in os.listdir('Z:/faces_train'):
    people.append(i)

features = np.load('features.npy', allow_pickle=True)
labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread('Z:/Train/faces_validation/Walter White/waltuh4.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Unidentified', gray)

#detect the face in the image first!

face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
for (x,y,w,h) in  face_rect:
    faces_roi = gray[y:y+h, x:x+w]

    label, confidence = face_recognizer.predict(faces_roi)

    print(f'Label = {people[label]} with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 0.75, (0, 255, 0), thickness=2)
    cv.rectangle(img, (x,y) , (x+w, y+h), (0, 255, 0), thickness=1)

cv.imshow('Detected', img)

cv.waitKey(0)
cv.destroyAllWindows()