from saved_model import get_pred
from keras.preprocessing import image

img = image.load_img('test.png', grayscale=True, target_size=(48, 48))
result = get_pred(img)

print(result)
