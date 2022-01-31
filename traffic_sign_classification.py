# -*- coding: utf-8 -*-
"""traffic_sign_classification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PWAZg027tZSsenowLyup9rQUa_dskBVJ
"""

from google.colab import drive 
drive.mount ('/content/drive')

import keras

from tensorflow.keras.applications import VGG16

import cv2
image= cv2.imread ('/content/drive/MyDrive/Traffic_sign/Train/0/00000_00000_00000.png')

conv_base= VGG16 (weights= 'imagenet', include_top=False, input_shape= (150,150,3))

from keras import models 
from keras import layers

model= models.Sequential ()
model.add(conv_base)
model.add(layers.Flatten())
model.add(layers.Dense (256, activation='relu'))
model.add(layers.Dense (43, activation='softmax'))

train_dir= '/content/drive/MyDrive/Traffic_sign/Train'

conv_base.trainable= False

from tensorflow.keras import optimizers
model.compile (optimizer= optimizers.Adam (learning_rate=0.01), loss= 'categorical_crossentropy', metrics= ['accuracy'])

from keras.preprocessing.image import ImageDataGenerator

datagen= ImageDataGenerator (rescale=1./255)

train_generator= datagen.flow_from_directory (train_dir, target_size= (150,150), batch_size=50, class_mode='categorical')

test_dir= '/content/drive/MyDrive/Traffic_sign/Test'

history= model.fit_generator (train_generator, steps_per_epoch=100, epochs=20,verbose=2)

import numpy as np
from PIL import Image
pic= '/content/drive/MyDrive/Traffic_sign/Train/Class 12: Main road/00012_00000_00001.png'
Pic_1= Image.open (pic)
# convert to array and rescale
pic_array=np.array (Pic_1).astype ('float32')/255

from skimage import transform 
#resize
np_image= transform.resize(pic_array, (150,150,3))

np_image.shape

np_image= np.expand_dims (np_image, axis=0)

np_image.shape

np_image

pred_class= model.predict (np_image)

pred_class