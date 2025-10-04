import streamlit as st
from google import genai

cortana = genai.Client(api_key = "AIzaSyC7eFq4iUcUvpQPlZKVpr7fgrx85PzGpP4")
st.title("Image Describer")

image = st.file_uploader('Upload Image', type=["jpg", "jpeg","png"])
query = st.text_input("Query")

if st.button("Send"):
    if image is not None:
        response = cortana.models.generate_content(model = "gemini-2.5-flash",
                                               contents = [{"role": "user", "parts":
                                                            [{"text": query},
                                                             {"inline_data": {"mime_type": image.type, "data": image.read()}}]}])
        st.write("Response: " + response.text)
    else:
        st.warning("Upload an image before sending.")

