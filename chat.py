import google.generativeai as genai
import streamlit as st
genai.configure(api_key="AIzaSyCmX2NeH2gNOE6QPL6r7HOUXO8fuqUfzd4")
model= genai.GenerativeModel("gemini-2.5-flash")
st.title("chat with gemini")
prompt= st.text_input("enter the question")
a="You are a Cybersecurity Awareness Training expert.only answer question based on Cybersecurity awareness training.if user as any other question other than this  answer them I don't have answer."
response = model.generate_content(prompt+a)
st.write(response.text)