import streamlit as st

st.set_page_config(page_title="OptimalTok.ai", layout="centered")

st.title("OptimalTok.ai 🚀")
st.write("Your AI-powered TikTok content generator and optimizer.")

prompt = st.text_input("Enter your video idea or prompt:")

if prompt:
    st.success("Prompt received. Generating...")
    # Placeholder until full backend is live
    st.image("https://placehold.co/600x800?text=Image+Here", caption="AI-Generated Image (Coming Soon)")
    st.video("https://www.w3schools.com/html/mov_bbb.mp4")

    st.write("💡 Suggestions for CapCut Editing will appear here.")
else:
    st.info("Waiting for prompt...")
