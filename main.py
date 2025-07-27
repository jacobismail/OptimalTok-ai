import streamlit as st
from pages.Home import show_home
from pages.Music import show_music

st.set_page_config(page_title="OptimalTok.ai", layout="centered")

st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Go to", ["Home", "Music & Remix"])

if page == "Home":
    show_home()
elif page == "Music & Remix":
    show_music()
