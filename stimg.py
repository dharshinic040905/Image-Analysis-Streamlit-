import streamlit as st
import google.generativeai as genai
from PIL import Image
genai.configure(api_key="AIzaSyAlBSBJTJK1fflXebjYnhtNiiVmpTRfea4")
model=genai.GenerativeModel("gemini-2.5-flash")
st.title("Image Q&A WITH GEMINI")
a=st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
prompt=st.text_input("Enter your question about the image")
if st.button("Submit"):
        img = Image.open(a)
        response = model.generate_content([img,prompt])
        st.write(response.text)