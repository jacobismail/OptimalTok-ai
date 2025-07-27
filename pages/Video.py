import streamlit as st
from openai import OpenAI

client = OpenAI()

st.markdown("### Generate a Seamlessly Looping Clip")

prompt = st.text_input("Describe your looping clip scene:")

if prompt:
    st.success("Prompt received. Generating still frames...")

    frame_urls = []
    for i in range(1, 5):  # Simulate 4-frame sequence
        frame_prompt = f"{prompt}, frame {i}, consistent composition, seamless loop"
        response = client.images.generate(
            model="dall-e-3",
            prompt=frame_prompt,
            size="1024x1792",
            quality="standard",
            n=1
        )
        frame_urls.append(response.data[0].url)

    for url in frame_urls:
        st.image(url, use_column_width=True)
