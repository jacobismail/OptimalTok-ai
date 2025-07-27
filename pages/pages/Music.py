import streamlit as st

def show_music():
    st.title("🎵 Tab 2 – Music & Remix")

    st.write("Generate or remix Assyrian music clips here. This tab includes:")
    st.markdown("""
    - AI-recommended Assyrian songs to remix  
    - Style suggestions (modern, traditional, club, cinematic, etc.)  
    - Suno.ai prompt output + suggested slider settings  
    - Buttons for:  
        - 🔁 Regenerate suggestions  
        - 🎧 Hear a sample  
        - 📝 Generate or Enhance Lyrics  
    """)

    st.info("All outputs assume Assyrian songs by default unless overridden in your input.")
