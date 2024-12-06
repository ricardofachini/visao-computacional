# 3. Import libraries and modules
import numpy as np
from keras.api.models import Sequential
from keras.api.layers import Dense, Dropout, Activation, Flatten
from keras.api.layers import Convolution2D, MaxPooling2D
from keras.api.utils import to_categorical
from keras.api.datasets import mnist

import tensorflow
from tensorflow.keras import layers

print(tensorflow.__version__)
