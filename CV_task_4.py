import tensorflow as tf
from tensorflow.keras.applications.resnet import ResNet50
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout, BatchNormalization
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau

def load_train(path):
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        validation_split=0.2,
        rotation_range=20,  
        width_shift_range=0.2,
        height_shift_range=0.2,
        horizontal_flip=True
    )
    train_data = train_datagen.flow_from_directory(
        path,
        target_size=(150, 150),
        batch_size=32,  
        class_mode='sparse',
        subset='training',
        seed=12345
    )
    return train_data

def create_model(input_shape=(150, 150, 3)):
    backbone = ResNet50(
        input_shape=input_shape,
        weights='/datasets/keras_models/resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5',
        include_top=False,
        classes=12
    )
    backbone.trainable = True
    for layer in backbone.layers[:]:  
        layer.trainable = False
    model = Sequential([
        backbone,
        GlobalAveragePooling2D(),
        BatchNormalization(),
        # Dense(128, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.02)), 
        # Dropout(0.5),
        # Dense(64, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.02)),
        # BatchNormalization(),
        Dropout(0.5),
        Dense(12, activation='softmax')
    ])

    optimizer = Adam(learning_rate=0.0005) 

    model.compile(
        optimizer=optimizer,
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )

    return model

def train_model(model, train_data, test_data):
    callbacks = [
        EarlyStopping(
            monitor='val_accuracy',
            patience=5,  # Уменьшить
            restore_best_weights=True
        ),
        ReduceLROnPlateau(  
            monitor='val_accuracy',
            factor=0.2, 
            patience=3,
            min_lr=0.00001
        )
    ]
    model.fit(
        train_data,
        validation_data=test_data,
        epochs=20,
        verbose=2,
        steps_per_epoch=50,
        validation_steps=25,
        callbacks=callbacks
    )
    return model