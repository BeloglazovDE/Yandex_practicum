import numpy as np

from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam

from tensorflow.keras.layers import (
    Conv2D,
    Dense,
    Flatten,
    AvgPool2D,
    MaxPooling2D
)
 
 
def load_train(path):
    features_train = np.load(path + 'train_features.npy')
    target_train = np.load(path + 'train_target.npy')
    features_train = np.expand_dims(features_train, axis=-1) / 255
    
    return features_train, target_train
 
 
def create_model(input_shape):
    model = Sequential()
    model.add(Conv2D(input_shape=input_shape, 
                     kernel_size=(3, 3),
                     filters=10,
                     activation='relu'
    ))
    model.add(Flatten())
    model.add(Dense(units=50, activation="relu"))
    model.add(Dense(units=10, activation='softmax'))

    optimizer = Adam()
    
    model.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy', 
    metrics=['acc']) 
    
    return model
 
 
def train_model(
        model, 
        train_data, 
        test_data, 
        batch_size=40, 
        epochs=50,
        steps_per_epoch=None, 
        validation_steps=None
):
    features_train, target_train = train_data
    features_test, target_test = test_data

    model.fit(features_train, target_train, 
              validation_data=(features_test, target_test),
              batch_size=batch_size, 
              epochs=epochs,
              steps_per_epoch=steps_per_epoch,
              validation_steps=validation_steps,
              verbose=2, 
              shuffle=True
    )
 
    return model