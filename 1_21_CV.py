import pandas as pd
import numpy as np

import tensorflow as tf
from tensorflow.keras.applications.resnet import ResNet50
from tensorflow.keras.layers import (
    GlobalAveragePooling2D, 
    Dense, 
    Dropout, 
    BatchNormalization
)
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau



def load_train(path):
    labels = pd.read_csv(path + 'labels.csv')
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        validation_split=0.2,
        rotation_range=20,  
        width_shift_range=0.2,
        height_shift_range=0.2,
        horizontal_flip=True
    )
    train_flow = train_datagen.flow_from_dataframe(
        dataframe=labels,
        directory=path + 'final_files/',
        x_col='file_name',
        y_col='real_age',
        target_size=(224, 224),
        batch_size=16,
        class_mode='raw',
        subset='training',
        seed=12345)

    return train_flow

def load_test(path):
    labels = pd.read_csv(path + 'labels.csv')
    test_datagen = ImageDataGenerator(
        validation_split=0.25, 
        horizontal_flip=True, 
        rescale=1./255
    )
    test_flow = test_datagen.flow_from_dataframe(
        dataframe=labels,
        directory=path + 'final_files/',
        x_col='file_name',
        y_col='real_age',
        target_size=(224, 224),
        batch_size=16,
        class_mode='raw',
        subset='validation',
        seed=12345)

    return test_flow


def create_model(input_shape):

    backbone = ResNet50(
        input_shape=input_shape,
        weights='/datasets/keras_models/resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5', 
        include_top=False
    )
    model = Sequential([
        backbone,
        GlobalAveragePooling2D(),
        Dense(1, activation='relu')
    ])
    model.compile(optimizer=Adam(lr=0.0001), loss='mse', metrics=['mae'])

    return model


def train_model(
        model, 
        train_data, 
        test_data, 
        batch_size=None, 
        epochs=25,
        steps_per_epoch=None, 
        validation_steps=None
):
    callbacks = [
        EarlyStopping(
            monitor='val_mae',
            patience=10,  
            restore_best_weights=True
        ),
        # ReduceLROnPlateau(  
        #     monitor='val_mae',
        #     factor=0.2, 
        #     patience=3,
        #     min_lr=0.00001
        # )
    ]
    model.fit(
        train_data,
        validation_data=test_data,
        batch_size=batch_size, 
        epochs=epochs,
        steps_per_epoch=steps_per_epoch,
        validation_steps=validation_steps,
        verbose=2,
        callbacks=callbacks
        )

    return model