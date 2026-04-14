import google.generativeai as genai
import streamlit as st
from PIL import Image #Pillow library for image processing - PIL 
genai.configure(api_key="AIzaSyDtTq0VQwhisnnCTJ8uKulrj9qVGAaf_t0")
model=genai.GenerativeModel("gemini-2.5-flash")
st.title("Image Q&A with Gemini")
a=st.file_uploader("Upload an image", type=["jpg","jpeg","png"])
prompt=st.text_input("Enter the question about the image:")
if st.button('submit'):
    img= Image.open(a)
    response = model.generate_content([img, prompt]) #[] podhala na + podanum
    st.write(response.text)