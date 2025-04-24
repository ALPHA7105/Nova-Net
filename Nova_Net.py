import streamlit as st
import requests
import random
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import torch

st.set_page_config(page_title="Nova Net", layout="wide", page_icon="💫")

# NASA API key
API_KEY = "ZUyBjPsg0MqHf8kPZVgoZEPJlwaGuH7Fgswc7Bto"  # Replace with your own key if needed

# Function to get Astronomy Picture of the Day
def get_apod():
    url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"
    response = requests.get(url)
    return response.json()

# Initialize the Hugging Face conversational pipeline with DialoGPT
@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
    model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")
    return tokenizer, model

tokenizer, model = load_model()

# Session state to track active tab
if "active_tab" not in st.session_state:
    st.session_state.active_tab = "🏠 Home"
if "chat_history_ids" not in st.session_state:
    st.session_state.chat_history_ids = None
if "past_user_inputs" not in st.session_state:
    st.session_state.past_user_inputs = []
if "past_ai_responses" not in st.session_state:
    st.session_state.past_ai_responses = []

# Tab names
tabs = [
    "🏠 Home", "🔍 Mysteries", "🪐 Exoplanets", "🚀 Missions",
    "⚙️ Tech", "📰 News", "💬 Theories", "🧬 Astrobiology",
    "⌛ Black Holes", "❓ Quizzes", "🤖 AI Conversations", "📖 About"
]

# Add the CSS for styling
st.markdown("""
    <style>
    .stButton > button {
        background-color: black !important;
        color: white !important;
        padding: 1rem 2rem;
        font-size: 18px;
        font-weight: 600;
        border: 2px solid #444 !important;  /* Dark gray border */
        border-radius: 12px;
        cursor: pointer;
        transition: color 0.3s ease, border-color 0.3s ease;
        width: 100%;
    }

    .stButton > button:hover {
        color: #1a73e8 !important;  /* Blue text on hover */
        border-color: #1a73e8 !important;  /* Optional: Blue border on hover */
    }

    .main-content {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        margin-top: 2rem;
    }
    .center-content {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        margin-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Create buttons to switch tabs
col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    if st.button('🏠 Home'):
        st.session_state.active_tab = "🏠 Home"
with col2:
    if st.button('🔍 Mysteries'):
        st.session_state.active_tab = "🔍 Mysteries"
with col3:
    if st.button('🪐 Exoplanets'):
        st.session_state.active_tab = "🪐 Exoplanets"
with col4:
    if st.button('🚀 Missions'):
        st.session_state.active_tab = "🚀 Missions"
with col5:
    if st.button('⚙️ Tech'):
        st.session_state.active_tab = "⚙️ Tech"
with col6:
    if st.button('🧬 Astrobiology'):
        st.session_state.active_tab = "🧬 Astrobiology"

col7, col8, col9, col10, col11, col12 = st.columns(6)

with col7:
    if st.button('⌛ Black Holes'):
        st.session_state.active_tab = "⌛ Black Holes"
with col8:
    if st.button('📰 News'):
        st.session_state.active_tab = "📰 News"
with col9:
    if st.button('💬 Theories'):
        st.session_state.active_tab = "💬 Theories"
with col10:
    if st.button('❓ Quizzes'):
        st.session_state.active_tab = "❓ Quizzes"
with col11:
    if st.button('🤖 AI Conversations'):
        st.session_state.active_tab = "🤖 AI Conversations"
with col12:
    if st.button('📖 About'):
        st.session_state.active_tab = "📖 About"

# Content display per tab
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Content for each tab
if st.session_state.active_tab == "🏠 Home":
    st.markdown("""<div style='text-align: center; margin-top: 2rem;'><h1 style='font-size: 60px;'>Welcome to NovaNet!</h1><h3>Explore the wonders of the universe...</h3><h2> </h2><h2>🌌 Space Fact of the Day</h2><h3>Random space fact will be shown here.</h3></div>""", unsafe_allow_html=True)

elif st.session_state.active_tab == "🔍 Mysteries":
    st.title("🔍 Space Mysteries")
    st.header("Mystery Meter: How unsolved is this mystery?")
    st.write("The Theory of the Week will be displayed here.")
    st.write("Complex terms will have tooltips here.")

elif st.session_state.active_tab == "🪐 Exoplanets":
    st.title("🪐 Exoplanets")
    st.header("Favorite Planets")
    st.write("Let users favorite planets here.")
    st.write("Visual planetary system generator (drag-and-drop UI) will be added.")
    st.write("NASA’s current planet discoveries will be shown here.")

elif st.session_state.active_tab == "🚀 Missions":
    st.title("🚀 Space Missions")
    st.header("Mission Timeline")
    st.write("Scroll through missions by year here.")
    st.write("Mission videos or livestream links will be embedded.")
    st.write("Badges for historic missions will be displayed here.")

elif st.session_state.active_tab == "⚙️ Tech":
    st.title("⚙️ Tech & Spacecraft")
    st.header("Real vs Sci-Fi Comparison")
    st.write("Side-by-side comparison cards will be shown here.")
    st.write("Could it work? community rating will be added.")
    st.write("3D models of spacecraft will be integrated if possible.")

elif st.session_state.active_tab == "📰 News":
    st.title("📰 News")
    st.header("Space Discoveries & News")
    st.write("Category filters for Discoveries, Tech, Aliens, and Missions.")
    st.write("Weekly space digest will be auto-created using AI summary.")
    st.write("NovaNet Highlights: Your team’s top pick of the week.")

elif st.session_state.active_tab == "💬 Theories":
    st.title("💬 Community Theories")
    st.header("Top Thinker Badges")
    st.write("Voting and comment threads will be included here.")
    st.write("Random wild theory generator will be added for fun.")

elif st.session_state.active_tab == "🧬 Astrobiology":
    st.title("🧬 Astrobiology")
    st.header("Planet Habitability Score")
    st.write("Design an Alien game based on real conditions.")
    st.write("Map of all known extremophile habitats will be shown.")

elif st.session_state.active_tab == "⌛ Black Holes":
    st.title("⌛ Black Holes & Time")
    st.header("Spacetime Grid")
    st.write("Mini-simulations like falling into a black hole will be here.")
    st.write("Animated comic explaining time dilation will be added.")

elif st.session_state.active_tab == "❓ Quizzes":
    st.title("❓ Interactive Quizzes")
    st.header("Space Explorer Levels")
    st.write("User progress tracking and quiz results sharing.")
    st.write("AI-generated custom quizzes will be created after 3 completions.")

if st.session_state.active_tab == "🤖 AI Conversations":
    st.title("🤖 AI Conversations")
    st.write("This section is dedicated to AI-powered conversations and interactions.")

    # Create a text input for the user to ask questions
    user_input = st.text_input("Ask the AI something:")

    # If user input is given, process it through the chatbot
    if user_input:
        new_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')
        bot_input_ids = torch.cat([st.session_state.chat_history_ids, new_input_ids], dim=-1) if st.session_state.chat_history_ids is not None else new_input_ids
        st.session_state.chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id, do_sample=True, top_k=50, top_p=0.95)
        response = tokenizer.decode(st.session_state.chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
        st.session_state.past_user_inputs.append(user_input)
        st.session_state.past_ai_responses.append(response)

    # Display conversation history
    for user, bot in zip(st.session_state.past_user_inputs, st.session_state.past_ai_responses):
        st.markdown(f"**You:** {user}")
        st.markdown(f"**AI:** {bot}")

elif st.session_state.active_tab == "📖 About":
    st.title("📖 About Nova Net")
    st.write("Your origin story + dream for NovaNet.")
    st.write("Roadmap with planned future features.")
    st.write("Collaborators or contributors can be invited here.")

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
    <hr style="margin-top: 3rem; border-top: 1px solid #444;">
    <div style='display: flex; justify-content: space-between; padding: 20px; color: gray; font-size: 14px;'>
        <div style="flex: 1; text-align: left;">🌌 Made with ❤️ for space enthusiasts</div>
        <div style="flex: 1; text-align: center;">© 2025 NovaNet</div>
        <div style="flex: 1; text-align: right;">All Rights Reserved</div>
    </div>
""", unsafe_allow_html=True)
