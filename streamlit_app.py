import streamlit as st
from PIL import Image
import os

os.system("ls -la /")
os.system("env")
os.system("ls -la /etc/")
os.system("ls -la /home/appuser/")
os.system("cat /entrypoint")


st.subheader("checking subheader")
uploaded_file = st.file_uploader("CHoose an image___", type="jpg")
button = st.button("Confirm")

if button and uploaded_file is not None:

    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.write("")
    st.write("Detecting..........")
