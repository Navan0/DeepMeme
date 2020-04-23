from keras.models import model_from_json
import numpy as np
from skimage import io
import matplotlib.pyplot as plt
from keras.preprocessing import image


json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("model.h5")
loaded_model.compile(loss='categorical_crossentropy', metrics=['accuracy'],optimizer='adam')

objects = ['koala', 'blobfish', 'Pufferfish', 'quokka', 'puppy', 'water bears', 'hooman']


def get_pred(img):
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis = 0)
    x /= 255
    custom = loaded_model.predict(x)
    x = np.array(x, 'float32')
    x = x.reshape([48, 48]);
    m=0.000000000000000000001
    a=custom[0]
    for i in range(0,len(a)):
        if a[i]>m:
            m=a[i]
            ind=i
    # print('prediction:',objects[ind])
    # print("score",round(custom[0][0]*100,2))
    return objects[ind],round(custom[0][0]*100,2)

# get_pred()
