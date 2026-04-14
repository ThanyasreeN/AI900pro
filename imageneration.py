import requests
import streamlit as st
prompt=st.text_input("Enter your question about the image:")
url="https://image.pollinations.ai/prompt/"+requests.utils.quote(prompt)
img=requests.get(url).content
with open("img.png","wb") as f:
    f.write(img)
st.image("img.png")