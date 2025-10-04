import streamlit as st
from google import genai

cortana = genai.Client(api_key = "AIzaSyC7eFq4iUcUvpQPlZKVpr7fgrx85PzGpP4")
st.title("GenAI")

image = st.file_uploader('Upload Image')

query = st.text_input("Query")
response = cortana.models.generate_content(model = "gemini-2.5-flash", contents = query)

if st.button("Send"):
    st.write("Response: " + response.text)
    

