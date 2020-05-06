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

from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory('data/train',target_size=(32,32),batch_size=32,class_mode='binary')

test_set = test_datagen.flow_from_directory('data/test',target_size=(32,32),batch_size=32,class_mode='binary')

model.fit_generator(
        training_set,
        steps_per_epoch=148,
        epochs=7,
        validation_data=test_set,
        validation_steps=40)

# Predicting 
import numpy as np
from keras.preprocessing import image

check_image = image.load_img("data/check/0.jpeg",target_size=(32,32))

check_image = image.img_to_array(check_image)

check_image = np.expand_dims(check_image,axis=0)

res = model.predict(check_image)

training_set.class_indices

if(res[0][0]==0):
    print("predicted person is normal person")
else:
    print("predicted person is COVID-19 affected person")

print()