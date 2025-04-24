import streamlit as st
import requests
import random
import google.generativeai as genai

st.set_page_config(page_title="Nova Net", layout="wide", page_icon="💫")

# NASA API key
API_KEY = "ZUyBjPsg0MqHf8kPZVgoZEPJlwaGuH7Fgswc7Bto"  # Replace with your own key if needed

# Function to get Astronomy Picture of the Day
def get_apod():
    url = f"https://api.nasa.gov/planetary/apod?api_key=ZUyBjPsg0MqHf8kPZVgoZEPJlwaGuH7Fgswc7Bto"
    response = requests.get(url)
    return response.json()

# Configure with your API key
genai.configure(api_key="AIzaSyCo_0KAksVDduggseFuvrDyVtcpjRPTAuY")

# Use the latest model that supports generate_content
model = genai.GenerativeModel("models/gemini-pro")

def get_gemini_response(user_input):
    try:
        response = model.generate_content(user_input)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

if "active_tab" not in st.session_state:
    st.session_state.active_tab = "🏠 Home"

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

if st.session_state.active_tab == "🏠 Home":
    st.markdown("""<div style='text-align: center; margin-top: 2rem;'>
                <h1 style='font-size: 60px;'>Welcome to NovaNet!</h1>
                <h3>Explore the wonders of the universe...</h3>
                <h2> </h2>
                </div>""", unsafe_allow_html=True)

# Tab names
tabs = [
    "🏠 Home", "🔍 Mysteries", "🪐 Exoplanets", "🚀 Missions",
    "⚙️ Tech", "📰 News", "💬 Theories", "🧬 Astrobiology",
    "⌛ Black Holes", "❓ Quizzes", "🤖 AI Conversations", "📖 About"
]

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
    st.markdown("""<div style='text-align: center; margin-top: 2rem;'>
                    <h1>🌌 Space Fact of the Day</h1>
                  </div>""", unsafe_allow_html=True)

    space_facts = [
        "A day on Venus is longer than a year.",
        "Neutron stars can spin 600 times per second.",
        "There’s a planet made of diamonds – 55 Cancri e.",
        "The largest volcano in the solar system is on Mars – Olympus Mons.",
        "The Moon is slowly drifting away from Earth (about 3.8 cm per year)."
    ]

    fact = random.choice(space_facts)

    st.markdown(f"""<div style='text-align: center; margin-top: 2rem;'>
                    <h3>{fact}</h3>
                  </div>""", unsafe_allow_html=True)
    
    st.markdown("""<div style='text-align: center; margin-top: 3rem;'>
                <h1>📸 NASA's Astronomy Picture of the Day</h1>
              </div>""", unsafe_allow_html=True)

    apod = get_apod()
    if apod:
        st.markdown(f"""
        <div style='text-align: center;'>
            <img src="{apod["url"]}" alt="{apod["title"]}" style="max-width: 90%; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.4);">
            <p style='margin-top: 1rem; font-weight: bold;'>{apod["title"]}</p>
        </div>
        """, unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: justify; margin-top: 1rem;'>{apod['explanation']}</p>", unsafe_allow_html=True)

    # 🧠 Interactive Poll
    st.markdown("""<div style='text-align: center; margin-top: 3rem;'>
                <h2>📊 Quick Poll</h2>
                <h4>Which space topic excites you the most?</h4>
                </div>""", unsafe_allow_html=True)

    options = [
        "🚀 Space Missions",
        "🕳️ Black Holes & Time Travel",
        "🛸 Aliens & Civilizations",
        "🪐 Exoplanets & New Worlds",
        "🧠 AI in Space"
        ]

    selected_option = st.radio("", options, index=0, key="space_poll")

    st.markdown("""
    <style>
        .stRadio label {
            font-size: 50px !important;
        }
    </style>
    """, unsafe_allow_html=True)
    
    if selected_option:
        st.markdown(f"<div style='text-align: center;'><h4>You chose: <strong>{selected_option}</strong></h4></div>", unsafe_allow_html=True)

elif st.session_state.active_tab == "🔍 Mysteries":
    st.markdown("""
    <h1 style='text-align: center;'>🕵️‍♂️ Unsolved Mysteries of the Universe 🌌</h1>
    <h4 style='text-align: center;'>Here are some of the most intriguing space mysteries that remain unsolved:</h4>
    <h3> </h3>
    """, unsafe_allow_html=True)
    
    mysteries = [
        {"title": "Dark Matter & Dark Energy 💫", 
         "description": "What are they, and why do they make up most of the universe's mass-energy content? "
                        "<a href='https://en.wikipedia.org/wiki/Dark_matter' target='_blank'>Learn more</a>."},
        {"title": "The Fermi Paradox 👽", 
         "description": "Why have we not yet encountered any extraterrestrial civilizations? "
                        "<a href='https://en.wikipedia.org/wiki/Fermi_paradox' target='_blank'>Learn more</a>."},
        {"title": "The Wow! Signal 📡", 
         "description": "A mysterious radio signal from space that has never been explained. "
                        "<a href='https://en.wikipedia.org/wiki/Wow!_signal' target='_blank'>Learn more</a>."},
        {"title": "The Nature of Black Holes ⚫", 
         "description": "Understanding the true nature of singularities and the event horizon. "
                        "<a href='https://en.wikipedia.org/wiki/Black_hole' target='_blank'>Learn more</a>."},
        {"title": "Quantum Gravity ⚛️", 
         "description": "How to reconcile general relativity and quantum mechanics. "
                        "<a href='https://en.wikipedia.org/wiki/Quantum_gravity' target='_blank'>Learn more</a>."}
    ]
    
    for mystery in mysteries:
        st.markdown(f"""
        <div style='margin-bottom: 20px; text-align: center;'>
            <h3>{mystery['title']}</h3>
            <p>{mystery['description']}</p>
        </div>
        """, unsafe_allow_html=True)

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

elif st.session_state.active_tab == "🤖 AI Conversations":
    st.title("🤖 AI Conversations")
    st.markdown("Talk to Gemini AI about space, science, or anything cosmic!")

    user_input = st.text_input("Ask something about the universe...")

    if user_input:
        with st.spinner("Gemini is thinking..."):
            response = get_gemini_response(user_input)
        st.markdown("**Gemini Says:**")
        st.success(response)

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
