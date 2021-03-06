# ------------------------------------------------------------------------
# Convolutional Neural Network Creation 

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Convolution2D
from keras.layers import MaxPool2D
from keras.layers import Flatten

model = Sequential()

model.add(Convolution2D(32,3,3,input_shape=(32,32,3),activation="relu"))

model.add(MaxPool2D(pool_size=(2,2)))

model.add(Flatten())


model.add(Dense(output_dim=128,activation="relu"))
model.add(Dense(output_dim=1,activation="sigmoid"))


# model.summary()

model.compile(optimizer="adam",loss="binary_crossentropy",metrics=['accuracy'])

# ------------------------------------------------------------------------
# Image Preprocessing

from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory('data/train',target_size=(32,32),batch_size=64,class_mode='binary')

test_set = test_datagen.flow_from_directory('data/test',target_size=(32,32),batch_size=64,class_mode='binary')

# ------------------------------------------------------------------------
# Fitting Data

model.fit_generator(
        training_set,
        steps_per_epoch=5216,
        epochs=5, verbose=1,
        validation_data=test_set,
        validation_steps=624)

# ------------------------------------------------------------------------
# Saving Model

model.save("model.h5")
