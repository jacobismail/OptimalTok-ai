import streamlit as st
from openai import OpenAI
import base64

client = OpenAI()

def generate_image(prompt):
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1792",
        quality="standard",
        n=1
    )
    return response.data[0].url

def display_download_button(image_url):
    image_bytes = client.images.download(image_url)
    base64_img = base64.b64encode(image_bytes).decode()
    href = f'<a href="data:image/jpeg;base64,{base64_img}" download="generated.jpg">📥 Download Image</a>'
    st.markdown(href, unsafe_allow_html=True)

st.markdown("### Enter your video idea or prompt:")
prompt = st.text_input("", placeholder="Describe the scene...")

if prompt:
    st.success("Prompt received. Generating...")
    image_url = generate_image(prompt)
    st.image(image_url, caption="Generated Image", use_column_width=True)
    display_download_button(image_url)
