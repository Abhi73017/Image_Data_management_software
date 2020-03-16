from _ast import Lambda
from keras import Sequential
from keras.layers import Conv2D, Activation, MaxPooling2D, Flatten, Dropout, Dense
from keras.optimizers import Adam


class feature_map():

    def __init__(self):
        pass

    def load_data(self):
        pass

    def build_model(self):

        model = Sequential()
        model.add(Conv2D(64, kernel_size=3, input_shape = (28, 28, 1)))

        model.add(Conv2D(32, (3, 3), padding='same'))
        model.add(Activation('relu'))
        model.add(MaxPooling2D((2, 2), padding='valid'))

        model.add(Conv2D(64, (3, 3), padding='same'))
        model.add(Activation('relu'))
        model.add(MaxPooling2D((2, 2), padding='valid'))

        model.add(Conv2D(128, (3, 3), padding='same'))
        model.add(Activation('relu'))
        model.add(MaxPooling2D((2, 2), padding='valid'))

        model.add(Flatten())
        model.add(Dropout(0.5))

        model.add(Dense(128))

        model.add(Dense(64))
        model.add(Dense(1))

        model.compile(optimizer=Adam(lr=0.0001), loss="mse")

    def load_model(self):
        pass

    def sub_model(self):
        pass


a=feature_map()
a.model()