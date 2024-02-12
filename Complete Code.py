# import os
# import numpy as np
# import cv2
# import matplotlib.pyplot as plt
# import pickle
# import random
# from sklearn.model_selection import train_test_split
# from sklearn.svm import SVC

#----------------------------For the classifing the dataset in to catagories and store in data.pickle--------------------------------------------

# dir = 'C:\\Users\\91978\\Desktop\\Internship\\SVM\\PetImages'

# catagories = ['Cat', 'Dog']
# data = []

# for catagory in catagories:
#     path = os.path.join(dir, catagory)
#     label = catagories.index(catagory)

#     for img in os.listdir(path):
#         imgpath = os.path.join(path, img)
#         pet_img=cv2.imread(imgpath,0)
#         try:
#             pet_img=cv2.resize(pet_img,(50,50))
#             image = np.array(pet_img).flatten()
#             data.append([image,label])
#         except Exception as e:
#             pass

# pick_in = open('data.pickle','wb')
# pickle.dump(data,pick_in)
# pick_in.close()

#--------------------------------------------------------------Training the Model --------------------------------------------------------------
# pick_in = open('data.pickle','rb')
# data=pickle.load(pick_in)
# pick_in.close()

# random.shuffle(data)
# features = []
# labels = []

# for feature , label in data:
#     features.append(feature)
#     labels.append(label)


# xtrain, xtest, ytrain, ytest =train_test_split(features, labels, test_size= 0.98) 

# model =SVC(C=1,kernel='poly',gamma='auto')
# model.fit(xtrain, ytrain)

# pick = open('model.sav','wb')
# pickle.dump(model,pick)
# pick.close()

#------------------------------------Prediction of the training model ----------------------------------------------------
# pick_in = open('data.pickle','rb')
# data=pickle.load(pick_in)
# pick_in.close()

# random.shuffle(data)
# features = []
# labels = []

# for feature , label in data:
#     features.append(feature)
#     labels.append(label)


# xtrain, xtest, ytrain, ytest =train_test_split(features, labels, test_size= 0.01) 

# # model =SVC(C=1,kernel='poly',gamma='auto')
# # model.fit(xtrain, ytrain)

# pick = open('model.sav','rb')
# model=pickle.load(pick)
# pick.close()

# prediction=model.predict(xtest)

# accuracy = model.score(xtest, ytest)

# catagories = ['Cat','Dog']
# print("Accuracy of the Model is :", accuracy*100,"%")

# print ("Predictions is :",catagories[prediction[0]])

# pet=xtest[0].reshape(50,50)
# plt.imshow(pet,cmap='gray')
# plt.show()