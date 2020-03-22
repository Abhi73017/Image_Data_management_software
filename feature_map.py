from glob import glob

from PIL import Image
from keras import Sequential
from keras.callbacks import ModelCheckpoint
from keras.layers import Conv2D, Activation, MaxPooling2D, Flatten, Dropout, Dense
from keras.optimizers import Adam, SGD
import os
import pandas as pd
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
import numpy as np


class feature_map():

    def __init__(self):
        pass

    def load_data(self):
        directory = os.path.join('H:\ML_AI_Projects\Skin cancer cell classification\ISIC cancer dataset\resized images')
        dir1=os.path.join('H:\ML_AI_Projects\Skin cancer cell classification\ISIC cancer dataset')
        cell_type = {
            'nv': '0',
            'mel': '1',
            'bkl': '2',
            'bcc': '3',
            'akiec': '4',
            'vasc': '5',
            'df': '6'
        }

        image_path_dict = {os.path.splitext(os.path.basename(x))[0]: x for x in
                           glob(os.path.join(directory, '*', '*.jpg'))}
        len(image_path_dict)

        skin_can_DF = pd.read_csv(os.path.join(dir1, 'HAM10000_metadata.csv'))

        skin_can_DF['path'] = skin_can_DF['image_id'].map(image_path_dict.get)
        skin_can_DF['cell_type'] = skin_can_DF['dx'].map(cell_type.get)
        skin_can_DF['cell_type_idx'] = pd.Categorical(skin_can_DF['cell_type']).codes

        skin_can_DF['image'] = skin_can_DF['path'].map(lambda x: np.asarray(Image.open(x)))
        train_DF, test_DF = train_test_split(skin_can_DF, test_size=0.65, random_state=1234)


        x_train = np.asarray(train_DF['image'].tolist())
        x_test = np.asarray(test_DF['image'].tolist())

        x_train_mean = np.mean(x_train)
        x_test_mean = np.mean(x_test)

        x_train_std = np.std(x_train)
        x_test_std = np.std(x_test)

        x_train = (x_train - x_train_mean) / x_train_std
        x_test = (x_test - x_test_mean) / x_test_std

        y_train = train_DF['cell_type']
        y_train = np.array(y_train)
        y_test = test_DF['cell_type']
        y_test = np.array(y_test)

        y_train = to_categorical(y_train, num_classes=7)
        y_test = to_categorical(y_test, num_classes=7)

        return x_train, x_test, y_train, y_test

    def build_model(self):

        model = Sequential()
        model.add(Conv2D(64, kernel_size=3, input_shape = (28, 28, 3)))

        model.add(Conv2D(32, (3, 3), padding='same'))
        model.add(Activation('relu'))
        model.add(MaxPooling2D((2, 2), padding='valid'))

        model.add(Conv2D(64, (3, 3), padding='same'))
        model.add(Activation('relu'))
        model.add(MaxPooling2D((2, 2), padding='valid'))

        model.add(Conv2D(128, (3, 3), padding='same'))
        model.add(Activation('relu'))
        model.add(MaxPooling2D((2, 2), padding='valid'))

        model.add(Conv2D(256, (3, 3), padding='same'))
        model.add(Activation('relu'))
        model.add(MaxPooling2D((2, 2), padding='valid'))

        model.add(Flatten())
        model.add(Dropout(0.5))

        model.add(Dense(128))

        model.add(Dense(64))
        model.add(Dense(1))

        model.compile(optimizer=Adam(lr=0.0001), loss="mse")

        x_train, x_test, y_train, y_test = feature_map.load_data(self)

        filepath = "F:\Data management software\models\weights-improvement-{epoch:02d}-{val_acc:.2f}.hdf5"
        checkpoint = ModelCheckpoint(filepath, monitor='val_acc', verbose=1, save_best_only=True, mode='max')

        sgd = SGD(lr=0.1, decay=1e-6, momentum=0.9, nesterov=True)
        model.compile(optimizer=sgd, loss='categorical_crossentropy', metrics=['accuracy'])
        '''
        datagen = ImageDataGenerator(featurewise_center=False, samplewise_center=False,
                                     featurewise_std_normalization=False, samplewise_std_normalization=False,
                                     zca_whitening=False, rotation_range=10, width_shift_range=0.1,
                                     height_shift_range=0.1, horizontal_flip=False, vertical_flip=False)
        '''
        history = model.fit(x_train, y_train, epochs=30,zverbose=1, steps_per_epoch=72,
                                      callbacks=[checkpoint])

    def load_model(self):
        pass

    def sub_model(self):
        pass


a=feature_map()
a.build_model()