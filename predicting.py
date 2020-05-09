# Predicting
from keras.models import load_model
import numpy as np
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Convolution2D
from keras.layers import MaxPool2D
from keras.layers import Flatten

model = load_model("model.h5")
# model.summary()
check_image = image.load_img("data/check/0.jpeg",target_size=(32,32))

check_image = image.img_to_array(check_image)

check_image = np.expand_dims(check_image,axis=0)

res = model.predict(check_image)

# training_set.class_indices

if(res[0][0]==0):
    print("predicted person is normal person")
else:
    print("predicted person shows symptoms of COVID-19")

