import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
import pickle
import random
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

#----------------------------For the classifing the dataset in to catagories and store in data.pickle--------------------------------------------

dir = 'C:\\Users\\91978\\Desktop\\Internship\\SVM\\PetImages'

catagories = ['Cat', 'Dog']
data = []

for catagory in catagories:
    path = os.path.join(dir, catagory)
    label = catagories.index(catagory)

    for img in os.listdir(path):
        imgpath = os.path.join(path, img)
        pet_img=cv2.imread(imgpath,0)
        try:
            pet_img=cv2.resize(pet_img,(50,50))
            image = np.array(pet_img).flatten()
            data.append([image,label])
        except Exception as e:
            pass

pick_in = open('data.pickle','wb')
pickle.dump(data,pick_in)
pick_in.close()