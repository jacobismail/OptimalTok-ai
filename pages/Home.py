import streamlit as st
from utils.shared_state import init_session_state

st.set_page_config(page_title="OptimalTok.ai", layout="centered")
init_session_state()

st.title("🎯 OptimalTok.ai")
st.markdown("**The Ultimate TikTok Creative Engine — Powered by AI**")

st.markdown("##### 📥 Step 1: Enter your TikTok Prompt")
prompt = st.text_area("Describe your TikTok concept, idea, or theme in as much detail as you'd like:", key="main_prompt")

if prompt:
    st.session_state["user_prompt"] = prompt
    st.success("✅ Prompt received! You can now proceed to the other tabs.")
else:
    st.info("💡 Tip: Be specific. The more details you give, the more optimized your results will be.")
