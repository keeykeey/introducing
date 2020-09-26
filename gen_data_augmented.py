from PIL import Image
import os,glob
import numpy as np
from sklearn.model_selection import train_test_split

classes = ['monkey','boar','crow']
num_classes = len(classes)
image_size = 50
num_testdata = 100

#load the data

X_train = []
X_test = []
Y_train = []
Y_test = []

for index,classLabel in enumerate(classes):
    photos_dir = "./" + classLabel
    files = glob.glob(photos_dir + '/*.jpg')
    for i,file in enumerate(files):
        if i >= 200:break
        image = Image.open(file)
        image = image.convert('RGB')
        image = image.resize((image_size,image_size))
        data = np.asarray(image)

        if i < num_testdata:
            X_test.append(data)
            Y_test.append(index)
        else:
            for angle in range(0,45,-20,20):
                img_rotate = image.rotate(angle)
                data_1 = np.asarray(img_rotate)
                X_train.append(data_1)
                Y_train.append(index)

                #反転
                img_trans = image.transpose(Image.FLIP_LEFT_RIGHT)
                img_trans = img_trans.rotate(angle)
                data_2 = np.asarray(img_trans) 
                X_train.append(data_2)
                Y_train.append(index)
       
X_train = np.array(X_train)
X_test = np.array(X_test)
Y_train = np.array(Y_train)
Y_test = np.array(Y_test)

xy = (X_train,X_test,Y_train,Y_test)
np.save('./animal_aug.npy',xy)

