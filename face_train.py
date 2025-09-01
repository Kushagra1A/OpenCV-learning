import os
import cv2 as cv
import numpy as np

people = []
for i in os.listdir('Z:/faces_train'):
    people.append(i)
#i -> barack obama, christian bale...

DIR = r'Z:/faces_train'

haar_cascade = cv.CascadeClassifier('haar_faces.xml')

features = []
labels = []

def preprocessing():
    for person in people:
        path = os.path.join(DIR, person)
        #path = z:/faces_train + Barack Obama == Z:\faces_train\Barack Obama

        label = people.index(person) #returns value as 0/1/2..

        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            img_arr = cv.imread(img_path)
            gray = cv.cvtColor(img_arr, cv.COLOR_BGR2GRAY)

            face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

            for (x,y,w,h) in face_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)


preprocessing()

print('Training Done ------------------------')
features = np.array(features, dtype = 'object')
labels = np.array(labels)

# print(f'length features: {len(features)}')
# print(f'length labels: {len(labels)}')

face_recognizer = cv.face.LBPHFaceRecognizer_create()

#train the recognizer on features and labels
face_recognizer.train(features, labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)