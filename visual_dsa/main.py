import streamlit as st
from prompts import dsa_prompts
from llm_utils import generate_manim_code
from manim_utils import save_script, render_video

st.set_page_config(page_title="VisualDSA", layout="wide")
st.title("🧠 VisualDSA: DSA Visualization Powered by LLMs")

topic = st.selectbox("Choose a DSA Concept", list(dsa_prompts.keys()))
custom_prompt = st.text_area("Or write your own prompt", height=150)
show_code = st.checkbox("Show Generated Code")

if st.button("Generate Animation"):
    prompt = custom_prompt.strip() if custom_prompt else dsa_prompts[topic]
    with st.spinner("Generating Manim code..."):
        code = generate_manim_code(prompt)

    if show_code:
        st.code(code, language="python")

    script_name = topic.replace(" ", "_")
    script_path = save_script(code, script_name)

    with st.spinner("Rendering video..."):
        try:
            video_path = render_video(script_path)
            if video_path:
                st.success("✅ Video Generated!")
                st.video(video_path)
            else:
                st.error("❌ Could not locate video file.")
        except Exception as e:
            st.error(f"Render error: {e}")

st.markdown("---")
st.caption("Built with ❤️ using Manim, Streamlit, and Groq LLaMA 3")
