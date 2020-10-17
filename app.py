import streamlit as st
from PIL import Image
from predict import   detecto_m
import matplotlib.pyplot as plt


def main():
    pages = ['Home', 'Detecto']

    option = st.sidebar.selectbox('Data Science for Marketing Dashboards', options=pages)

    if option == 'Home':
        st.markdown('# Object Detection')
        st.markdown('Object Detection.'\
            ' The app is built by [Boadzie Daniel](https://boadzie.surge.sh/)')
        st.image('./img/Dan.jpg', width=200)
        st.markdown('---')
        
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
