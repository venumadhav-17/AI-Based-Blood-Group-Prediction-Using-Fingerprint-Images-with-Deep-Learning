from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator

img_size = 128
batch_size = 16

model = load_model("blood_group_model.h5")

datagen = ImageDataGenerator(rescale=1./255)

test_generator = datagen.flow_from_directory(
    'dataset',
    target_size=(img_size,img_size),
    batch_size=batch_size,
    class_mode='categorical'
)

loss, accuracy = model.evaluate(test_generator)

print("Test Accuracy:", accuracy)