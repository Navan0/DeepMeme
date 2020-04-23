from keras.models import model_from_json
from keras.preprocessing import image
import numpy as np
from skimage import io
import matplotlib.pyplot as plt


json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("model.h5")
print("Loaded model from disk")
loaded_model.compile(loss='categorical_crossentropy', metrics=['accuracy'],optimizer='adam')

objects = ['koala', 'blobfish', 'Pufferfish', 'quokka', 'puppy', 'water bears', 'hooman']
def emotion_analysis(emotions):
    objects = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']
    y_pos = np.arange(len(objects))
    plt.bar(y_pos, emotions, align='center', alpha=0.9)
    plt.tick_params(axis='x', which='both', pad=10,width=4,length=10)
    plt.xticks(y_pos, objects)
    plt.ylabel('percentage')
    plt.title('emotion')

plt.show()


img = image.load_img('test.png', grayscale=True, target_size=(48, 48))
show_img=image.load_img('test.png', grayscale=False, target_size=(200, 200))
x = image.img_to_array(img)
x = np.expand_dims(x, axis = 0)

x /= 255

custom = loaded_model.predict(x)
print(custom)

# print("%s: %.2f%%" % (loaded_model.metrics_names[1], scores[1]*100))
emotion_analysis(custom[0])

x = np.array(x, 'float32')
x = x.reshape([48, 48]);

plt.gray()
plt.imshow(show_img)
plt.show()

m=0.000000000000000000001
a=custom[0]
for i in range(0,len(a)):
    if a[i]>m:
        m=a[i]
        ind=i

print('prediction:',objects[ind])
print("score",round(custom[0][0]*100,2))
