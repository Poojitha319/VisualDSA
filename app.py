# visualdsa_app.py

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import subprocess
from groq import Groq

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="Visual DSA - AI Learning Platform",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---- API CONFIG ----
GROQ_API_KEY = "Enter your Groq API key here"
MODEL_NAME = "llama-3.3-70b-versatile"

groq_client = Groq(api_key=GROQ_API_KEY)

# ---- SESSION STATE ----
if 'user_progress' not in st.session_state:
    st.session_state.user_progress = {
        'completed_topics': [],
        'current_streak': 0,
        'total_points': 0,
        'learning_path': 'beginner'
    }

# ---- DSA TOPICS ----
dsa_topics = {
    'Arrays': {
        'difficulty': 'Easy',
        'concepts': ['Linear Search', 'Binary Search'],
        'description': 'Contiguous memory elements'
    },
    'Graphs': {
        'difficulty': 'Hard',
        'concepts': ['DFS', 'BFS'],
        'description': 'Vertices and edges'
    },
    'Dynamic Programming': {
        'difficulty': 'Hard',
        'concepts': ['Memoization', 'Tabulation'],
        'description': 'Break into subproblems'
    },
}

# ---- SIDEBAR ----
st.sidebar.title("🔎 Navigation")
page = st.sidebar.radio("Select Page", ["🏠 Dashboard", "📚 Learn", "🎯 Practice", "🤖 Tutor", "🎬 Video"])

# ---- DASHBOARD ----
if page == "🏠 Dashboard":
    st.title("📊 Your Progress Dashboard")
    topics = list(dsa_topics.keys())
    progress_data = np.random.randint(30, 100, len(topics))
    fig = px.bar(x=topics, y=progress_data, title="Topic Mastery")
    st.plotly_chart(fig, use_container_width=True)

# ---- LEARN ----
elif page == "📚 Learn":
    st.title("📘 Learn Topics")
    for topic, info in dsa_topics.items():
        with st.expander(f"{topic} - {info['difficulty']}"):
            st.write(info['description'])
            st.write("**Concepts:**")
            for c in info['concepts']:
                st.markdown(f"- {c}")

# ---- PRACTICE ----
elif page == "🎯 Practice":
    st.title("💪 Practice Problems")
    problems = [
        {"name": "Two Sum", "difficulty": "Easy", "solved": True},
        {"name": "DFS", "difficulty": "Hard", "solved": False},
    ]
    for prob in problems:
        status = "✅" if prob['solved'] else "❌"
        st.write(f"{status} {prob['name']} - {prob['difficulty']}")

# ---- AI TUTOR ----
elif page == "🤖 Tutor":
    st.title("🤖 Ask Your AI Tutor")
    user_query = st.text_input("Ask anything about DSA:")
    if st.button("Get Answer") and user_query:
        with st.spinner("Thinking..."):
            chat = groq_client.chat.completions.create(
                messages=[
                    {"role": "system", "content": "You are a DSA teacher."},
                    {"role": "user", "content": user_query}
                ],
                model=MODEL_NAME
            )
            response = chat.choices[0].message.content
            st.success(response)

# ---- VIDEO GENERATOR ----
elif page == "🎬 Video":
    st.title("🎥 DSA Video Visualizer")
    algo = st.selectbox("Choose an algorithm", ["Binary Search", "DFS", "Knapsack"])
    generate = st.button("Generate Video")

    PROMPTS = {
        "Binary Search": """Create a Manim animation to explain how Binary Search works on a sorted array [1, 3, 5, 7, 9] while searching for 5. Highlight mid, low, high at each step.""",
        "DFS": """Create a Manim animation to demonstrate Depth First Search traversal on a graph with 5 nodes. Show stack updates, node visits, and backtracking.""",
        "Knapsack": """Visualize 0/1 Knapsack Problem with a table showing choices and recursive decisions. Highlight picked items dynamically."""
    }

    if generate and algo:
        with st.spinner("Generating..."):
            prompt = PROMPTS[algo]
            response = groq_client.chat.completions.create(
                messages=[
                    {"role": "system", "content": "You're a Manim expert."},
                    {"role": "user", "content": prompt}
                ],
                model=MODEL_NAME
            )
            script = response.choices[0].message.content

            # Save Manim script
            filename = "manim_script.py"
            with open(filename, "w") as f:
                f.write(script)

            # Render Video
            try:
                subprocess.run(["manim", filename, "-ql"], check=True)
                video_path = "media/videos/manim_script/480p15/ManimScript.mp4"
                st.video(video_path)
            except Exception as e:
                st.error("Video generation failed. Check Manim installation.")
