from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg19 import  preprocess_input
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from detecto import core, utils, visualize
from PIL import Image
import numpy as np

def cat_vs_dog(image_path): 
    model = load_model('models/model.h5')
    imagez = image.load_img(image_path, target_size=(224, 224))
    imagez = img_to_array(imagez)
    imagez = np.expand_dims(imagez, axis=0)
    predicted = model.predict(imagez)
    max_index = np.argmax(predicted)
    if max_index == 0:
        return "It's a Cat!"
    elif max_index == 1:
        return  "It's a Dog!"
    
############################ Fashion Mnist ################################
def detecto_m(pic): 
    image = utils.read_image(pic)
    model = core.Model()
    labels, boxes, scores = model.predict_top(image)
    result = visualize.show_labeled_image(image, boxes, labels)
    return result