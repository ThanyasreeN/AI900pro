import streamlit as st
st.title("hello world app")
name = st.text_input("Enter your name")
st.write(name)