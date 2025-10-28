import numpy as np

from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam

from tensorflow.keras.layers import (
    Conv2D,
    Dense,
    Flatten,
    BatchNormalization,
    MaxPooling2D
)
 
from tensorflow.keras.preprocessing.image import ImageDataGenerator

 
def load_train(path):
    train_datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

    train_data = train_datagen.flow_from_directory(
        path,
        target_size=(150, 150),
        batch_size=60,
        class_mode='sparse',  
        subset='training',
        seed=12345
    )
    
    return train_data
 
 
def create_model(input_shape):
    model = Sequential()
    model.add(Conv2D(input_shape=input_shape, 
                     kernel_size=(3, 3),
                     filters=5,
                     activation='relu',
                     padding='same'
    ))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(kernel_size=(3, 3),
                     filters=10,
                     activation='relu',
                     padding='same'
    ))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(kernel_size=(3, 3),
                     filters=20,
                     activation='relu',
                     padding='same'
    ))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Flatten())
    model.add(Dense(units=400, activation="relu"))
    model.add(Dense(units=100, activation="relu"))
    model.add(Dense(units=50, activation="relu"))
    model.add(Dense(units=12, activation='softmax'))

    optimizer = Adam(learning_rate=0.01)
    
    model.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy', 
    metrics=['acc']) 

    # model.summary()
    

    return model
 
 
def train_model(
        model, 
        train_data, 
        test_data, 
        batch_size=None, 
        epochs=30,
        steps_per_epoch=None, 
        validation_steps=None
):

    model.fit(train_data, 
    validation_data=test_data,
    batch_size=batch_size, epochs=epochs,
    steps_per_epoch=steps_per_epoch,
    validation_steps=validation_steps,
    verbose=2)
 
    return model

# create_model((150, 150, 3))