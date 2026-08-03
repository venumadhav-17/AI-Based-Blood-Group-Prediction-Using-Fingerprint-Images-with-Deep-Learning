import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, Input
from tensorflow.keras.preprocessing.image import ImageDataGenerator

print("===== BLOOD GROUP TRAINING STARTED =====")

# SETTINGS
img_size = 128
batch_size = 16
epochs = 20

# DATA GENERATOR
datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2
)

# TRAINING DATA
train_generator = datagen.flow_from_directory(
    'dataset',
    target_size=(img_size, img_size),
    batch_size=batch_size,
    class_mode='categorical',
    subset='training'
)

# 🔥 PRINT CLASS ORDER
print("Class Indices:", train_generator.class_indices)

# VALIDATION DATA
val_generator = datagen.flow_from_directory(
    'dataset',
    target_size=(img_size, img_size),
    batch_size=batch_size,
    class_mode='categorical',
    subset='validation'
)

# MODEL
model = Sequential([
    Input(shape=(img_size, img_size, 3)),

    Conv2D(32, (3,3), activation='relu'),
    MaxPooling2D(2,2),

    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D(2,2),

    Conv2D(128, (3,3), activation='relu'),
    MaxPooling2D(2,2),

    Flatten(),
    Dense(256, activation='relu'),
    Dropout(0.5),
    Dense(8, activation='softmax')
])

# COMPILE
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# TRAIN
model.fit(
    train_generator,
    validation_data=val_generator,
    epochs=epochs
)

# SAVE MODEL (NEW FORMAT)
model.save("blood_group_model.keras")

print("===== MODEL TRAINED & SAVED SUCCESSFULLY =====")