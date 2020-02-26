from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
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

#####################################################################################
############################## Cats vs Dogs ########################################
        
    elif option == 'Cat_vs_Dog':
        st.markdown("# Cats Vs. Dogs Classifier")
        st.markdown("#### A Simple Cat vs Dog Classifier using Transfer Learning")
        st.markdown("---")

        uploaded_file = st.file_uploader("Choose an image...", type="jpg")
        if uploaded_file is not None:
            imagez = Image.open(uploaded_file)
            st.image(imagez, caption='Your Image.', use_column_width=True)
            st.write("")
            # st.write("Predicting...")
            label = cat_vs_dog(uploaded_file)
            st.balloons()
            st.success(label)