import streamlit as st
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg19 import decode_predictions, preprocess_input
from PIL import Image
from skimage import io
from predict import  cat_vs_dog, detecto_m
import matplotlib.pyplot as plt


def main():
    pages = ['Home', 'Cat_vs_Dog', 'Detecto']

    option = st.sidebar.selectbox('Data Science for Marketing Dashboards', options=pages)

    if option == 'Home':
        st.markdown('# Welcome to the Machine Learning Land')
        st.markdown('This app contains a series of Machine Learning Apps showing Image Classification Object Detection.'\
            ' The app is built by [Boadzie Daniel](https://boadzie.surge.sh/) and The Students of [Artificial Intelligence Movement(AIM)](https://www.aimovement.club/)')
        st.image('./img/Dan.jpg', width=200)
        st.image('./img/AIM.jpeg', width=700)
        st.markdown('---')

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
        
        ######################## Detecto   ################################
    elif option == 'Detecto':
        st.markdown("# Object Dector")
        st.markdown("#### A Simple Object detector using Detecto")
        st.markdown("---")

        uploaded_file = st.file_uploader("Choose an pic...", type="jpg")
        if uploaded_file is not None:
            # imagez = Image.open(uploaded_file)
            # imagez = imagez.convert("RGBA")
            st.image(uploaded_file, caption='Your Image.', use_column_width=True)
            st.success("#### And taraaaaa!")
            result = detecto_m(uploaded_file)
            result = plt.plot()
            st.pyplot(result)
            st.balloons()
    
    
        
        

if __name__=='__main__':
    main()
