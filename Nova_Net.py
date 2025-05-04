from datetime import datetime, timedelta
import streamlit as st
import pandas as pd
import requests
import hashlib
import random
import json
import time
import html
import csv
import os

st.set_page_config(page_title="NovaNet", layout="wide", page_icon="💫")

if "active_tab" not in st.session_state:
    st.session_state.active_tab = "🏠 Home"

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

st.markdown("""
    <div style='text-align: center; margin-top: 1rem;'>
        <h1 style='font-size: 60px; margin-bottom: 0;'>💫 NovaNet</h1>
        <h3 style='margin-top: 0;'>Where curiosity meets the cosmos...</h3>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")


# Tab names
tabs = [
    "🏠 Home", "🔍 Mysteries", "🪐 Exoplanets", "🚀 Missions",
    "⚙️ Tech", "📰 News", "💬 Theories", "🧬 Astrobiology",
    "⌛ Black Holes", "❓ Quizzes", "🤖 Nova AI", "📖 About"
]

# Create buttons to switch tabs
col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    if st.button("🏠 Home"):
        st.session_state.active_tab = "🏠 Home"
with col2:
    if st.button("🔍 Mysteries"):
        st.session_state.active_tab = "🔍 Mysteries"
with col3:
    if st.button("🪐 Exoplanets"):
        st.session_state.active_tab = "🪐 Exoplanets"
with col4:
    if st.button("🚀 Missions"):
        st.session_state.active_tab = "🚀 Missions"
with col5:
    if st.button("⚙️ Tech"):
        st.session_state.active_tab = "⚙️ Tech"
with col6:
    if st.button("🧬 Astrobiology"):
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
    if st.button('🤖 Nova AI'):
        st.session_state.active_tab = "🤖 Nova AI"
with col12:
    if st.button('📖 About'):
        st.session_state.active_tab = "📖 About"

st.markdown("---")

# Content display per tab
st.markdown('<div class="main-content">', unsafe_allow_html=True)

if st.session_state.active_tab == "🏠 Home":
    
    API_KEY = "ZUyBjPsg0MqHf8kPZVgoZEPJlwaGuH7Fgswc7Bto"

    def get_apod():
        url = f"https://api.nasa.gov/planetary/apod?api_key=ZUyBjPsg0MqHf8kPZVgoZEPJlwaGuH7Fgswc7Bto"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            st.error(f"Error fetching APOD: {e}")
            return None

    # Fun facts
    fun_facts = [
        "One day on Venus is longer than its entire year!",
        "Neutron stars can spin 600 times per second.",
        "There’s a planet made of diamonds called 55 Cancri e.",
        "Jupiter has 95 known moons as of 2024!",
        "A spoonful of a neutron star weighs about a billion tons.",
        "The Moon is slowly drifting away from Earth—about 4cm every year."
    ]

    # Title and Intro
    st.markdown("""<div style='text-align: center; margin-top: 2rem;'>
                   <h1>🌎 Home</h1>
                   </div>""", unsafe_allow_html=True)

    st.markdown("""<div style='text-align: center; margin-top: 2rem; font-size: 18px; line-height: 1.6;'>
                   Welcome to <strong>NovaNet</strong> — your gateway to the universe. From mind-bending space mysteries and NASA missions to exoplanets, black holes, astrobiology, and the latest tech, NovaNet brings the cosmos to your screen in a way that's interactive, intelligent, and inspiring. With real-time data, AI conversations, community theories, and much more, NovaNet isn't just a space platform — it's your personal mission control for exploring the stars.
                   </div>""", unsafe_allow_html=True)

    st.markdown("---")

    # NASA APOD (Astronomy Picture of the Day)
    st.markdown("""<div style='text-align: center; margin-top: 3rem;'>
                <h1>📸 NASA's Astronomy Picture of the Day</h1>
              </div>""", unsafe_allow_html=True)

    apod = get_apod()
    if apod:
        st.markdown(f"""
        <div style='text-align: center;'>
            <img src="{apod["url"]}" alt="{apod["title"]}" style="max-width: 40%; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.4);">
            <p style='margin-top: 1rem; font-weight: bold; font-size: 1.2rem;'>{apod["title"]}</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: justify; margin-top: 1rem; font-size: 1rem;'>{apod['explanation']}</p>", unsafe_allow_html=True)

    st.divider()

    # Fun Fact
    st.subheader("🚀 Fun Space Fact")
    st.info(random.choice(fun_facts))
    st.divider()

    # Community Poll
    st.subheader("🗳️ Community Poll")
    poll_question = "Do you think humans will land on Mars before 2040?"
    options = ["Yes, definitely!", "Maybe", "No way!"]
    vote = st.radio(poll_question, options)

    if vote:
        st.success(f"You selected: {vote}")

    st.divider()

    # Astronaut Spotlight
    st.subheader("👨‍🚀 Astronaut Spotlight")
    st.markdown("""
    Each month, NovaNet will spotlight one of the incredible astronauts who have made monumental contributions to space exploration. This month, we're honoring **Sally Ride**, the first American woman in space.
    Sally Ride made history when she flew aboard the Space Shuttle Challenger on June 18, 1983, becoming the first American woman in space. Her legacy continues to inspire future generations of space explorers.
    """)
    st.divider()

    # Space Concept of the Month
    st.subheader("💡 Concept of the Month")
    st.markdown("""
    **Gravitational Waves**: Gravitational waves are ripples in spacetime caused by some of the most violent and energetic processes in the universe, like colliding black holes. These waves were first directly detected in 2015 by LIGO, opening a whole new way to observe the universe.
    """)
    st.divider()

    # Space Quote of the Month
    st.subheader("💬 Space Quote of the Month")
    st.markdown("""
    > "The important achievement of Apollo was demonstrating that humanity is not forever chained to this planet and our visions go rather further than that and our opportunities are unlimited." – **Neil Armstrong**
    """)
    st.divider()

    # Space Technology Spotlight
    st.subheader("⚙️ Technology Spotlight")
    st.markdown("""
    **James Webb Space Telescope (JWST)**: Launched in 2021, JWST is the most powerful space telescope ever built. It is designed to study the infrared universe, including the formation of stars, galaxies, and planetary systems. The JWST promises to answer some of the most profound questions about the universe's origin and structure.
    """)

    st.markdown("""
    <br><br>
    <div style='text-align: right; font-size:18px; margin-right: 30px;'>
        <b>Next: 🔍 Mysteries ➡️</b>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.active_tab == "🔍 Mysteries":
    st.markdown("""
        <h1 style='text-align: center;'>🕵️‍♂️ Unsolved Mysteries of the Universe 🌌</h1>
        <p style='text-align: center;'>Here are some of the most intriguing space mysteries that remain unsolved:</p>
    """, unsafe_allow_html=True)
    st.markdown("---")
    
    mysteries = [
        {"title": "Dark Matter & Dark Energy 💫", 
         "description": "What are they, and why do they make up most of the universe's mass-energy content? "
                        "<a href='https://en.wikipedia.org/wiki/Dark_matter' target='_blank'>Learn more</a>"},
        {"title": "The Fermi Paradox 👽", 
         "description": "Why have we not yet encountered any extraterrestrial civilizations? "
                        "<a href='https://en.wikipedia.org/wiki/Fermi_paradox' target='_blank'>Learn more</a>"},
        {"title": "The Wow! Signal 📡", 
         "description": "A mysterious radio signal from space that has never been explained. "
                        "<a href='https://en.wikipedia.org/wiki/Wow!_signal' target='_blank'>Learn more</a>"},
        {"title": "The Nature of Black Holes ⚫", 
         "description": "Understanding the true nature of singularities and the event horizon. "
                        "<a href='https://en.wikipedia.org/wiki/Black_hole' target='_blank'>Learn more</a>"},
        {"title": "Quantum Gravity ⚛️", 
         "description": "How to reconcile general relativity and quantum mechanics. "
                        "<a href='https://en.wikipedia.org/wiki/Quantum_gravity' target='_blank'>Learn more</a>"},
        {"title": "The Multiverse Theory 🌐", 
         "description": "Is there more than one universe? Exploring the idea of parallel universes. "
                        "<a href='https://en.wikipedia.org/wiki/Multiverse' target='_blank'>Learn more</a>"},
        {"title": "The Search for Alien Life 👽", 
         "description": "How can we detect signs of extraterrestrial life, and why haven't we found any proof yet? "
                        "<a href='https://en.wikipedia.org/wiki/Search_for_extraterrestrial_intelligencee' target='_blank'>Learn more</a>"},
        {"title": "The Origin of Cosmic Rays ⚡", 
         "description": "What causes the high-energy cosmic rays that bombard Earth, and where do they come from? "
                        "<a href='https://en.wikipedia.org/wiki/Cosmic_ray' target='_blank'>Learn more</a>"}
        ]

    col1, col2 = st.columns(2)
    
    with col1:
        for mystery in mysteries[:4]:
            st.markdown(f"""
            <div style='margin-bottom: 20px; text-align: left;'>
                <h3>{mystery['title']}</h3>
                <p>{mystery['description']}</p>
            </div>
            """, unsafe_allow_html=True)

    with col2:
        for mystery in mysteries[4:]:
            st.markdown(f"""
            <div style='margin-bottom: 20px; text-align: left;'>
                <h3>{mystery['title']}</h3>
                <p>{mystery['description']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("""
    <h2 style='text-align: center;'>⚠️ Space Anomalies ⚡</h2>
    <p style='text-align: center;'>These are some of the most perplexing anomalies in space that scientists are still trying to understand:</p>
    """, unsafe_allow_html=True)

    anomalies = [
        {"title": "The Great Attractor 🌀", 
         "description": "A mysterious gravitational anomaly pulling galaxies towards it. Scientists are still unsure of its nature. "
                        "<a href='https://en.wikipedia.org/wiki/Great_Attractor' target='_blank'>Learn more</a>."},
                        
        {"title": "Fast Radio Bursts (FRBs) ⚡", 
         "description": "Intense bursts of radio waves from deep space that last only milliseconds, with unknown origins. "
                        "<a href='https://en.wikipedia.org/wiki/Fast_radio_burst' target='_blank'>Learn more</a>."},
                        
        {"title": "The Black Knight Satellite 🛰️", 
         "description": "A purported alien satellite in Earth’s orbit that has intrigued conspiracy theorists for decades. "
                        "<a href='https://en.wikipedia.org/wiki/Black_Knight_satellite' target='_blank'>Learn more</a>."},
                        
        {"title": "Tabby's Star 🌟", 
         "description": "A star that dims and brightens in ways that cannot be easily explained. Could it be a sign of alien megastructures? "
                        "<a href='https://en.wikipedia.org/wiki/KIC_8462852' target='_blank'>Learn more</a>."},
                        
        {"title": "Hawking Radiation 🔥", 
         "description": "Theoretical radiation emitted by black holes, proposed by Stephen Hawking. Still unproven but could unlock a new understanding of black holes. "
                        "<a href='https://en.wikipedia.org/wiki/Hawking_radiation' target='_blank'>Learn more</a>."},
                        
        {"title": "Oumuamua 🛸", 
         "description": "A mysterious interstellar object that passed through our solar system in 2017, sparking debates about its origins. "
                        "<a href='https://en.wikipedia.org/wiki/1I/2017_U1' target='_blank'>Learn more</a>."}
    ]

    col1, col2 = st.columns(2)

    with col1:
        for anomaly in anomalies[:3]:
            st.markdown(f"""
            <div style='margin-bottom: 20px; text-align: left;'>
                <h3>{anomaly['title']}</h3>
                <p>{anomaly['description']}</p>
            </div>
            """, unsafe_allow_html=True)

    with col2:
        for anomaly in anomalies[3:]:
            st.markdown(f"""
            <div style='margin-bottom: 20px; text-align: left;'>
                <h3>{anomaly['title']}</h3>
                <p>{anomaly['description']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("<h2 style='text-align: center;'>🧠 Theories & Hypotheses</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div style='text-align: left;'>
        <h4>🌌 Dark Matter Web</h4>
        <p>What if it's the intelligent framework of the universe?</p>
        <a href='https://en.wikipedia.org/wiki/Dark_matter' target='_blank'>🔗 Learn More</a>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style='text-align: left; margin-top: 2rem;'>
        <h4>💥 White Holes</h4>
        <p>Theoretical opposites of black holes. Could they exist?</p>
        <a href='https://en.wikipedia.org/wiki/White_hole' target='_blank'>🔗 Learn More</a>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style='text-align: left;'>
        <h4>🧬 Shadow Biospheres</h4>
        <p>Alien life forms we can't detect with current tools?</p>
        <a href='https://en.wikipedia.org/wiki/Shadow_biosphere' target='_blank'>🔗 Learn More</a>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style='text-align: left; margin-top: 2rem;'>
        <h4>🛰️ Simulation Hypothesis</h4>
        <p>Are we living inside a cosmic simulation?</p>
        <a href='https://en.wikipedia.org/wiki/Simulation_hypothesis' target='_blank'>🔗 Learn More</a>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("<h2 style='text-align: center;'>🏆 Mystery of the Month</h2>", unsafe_allow_html=True)

    st.markdown("""
    <div style='text-align: center;'>
    <h3>📡 The Wow! Signal</h3>
    <p>A strange radio signal was detected in 1977 from deep space. And it never repeated again.</p>
    <video width='560' height='315' controls>
      <source src='https://www.youtube.com/watch?app=desktop&v=aseyBWZa3pY&t=0s' type='video/webm'>
      Your browser does not support the video tag.
    </video>
    <p>“Wow!” – the signal that still puzzles scientists.</p>
    <p><i>🚧 This video might not work, as video options are still under development. 🛠️</i><p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("<h2 style='text-align: center;'>📹 Video & Documentation</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div style='text-align: center;'>
        <h4>🎬 Dark Universe Explained</h4>
        <a href='https://www.youtube.com/watch?v=QAa2O_8wBUQ' target='_blank'>▶️ Watch on YouTube</a>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style='text-align: center;'>
        <h4>📄 PDF: NASA Unexplained Files</h4>
        <a href='https://ntrs.nasa.gov/api/citations/20090010233/downloads/20090010233.pdf' target='_blank'>📥 Download PDF</a>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""---""")
    st.markdown("""
    <div style='text-align: center;'>
        <h2>🧩 Unlocking the Universe’s Secrets</h2>
        <p style='font-size:18px;'>
            The cosmos holds mysteries beyond our wildest dreams. 🛸✨<br><br>
            From dark matter to ancient signals, each mystery invites us to imagine, explore, and question everything.<br><br>
            The adventure has just begun — are you ready to solve the universe's greatest puzzles? 🔍🚀
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <br><br>
    <div style='text-align: right; font-size:18px; margin-right: 30px;'>
        <b>Next: 🪐 Exoplanets ➡️</b>
    </div>
    """, unsafe_allow_html=True)


elif st.session_state.active_tab == "🪐 Exoplanets":
    st.markdown("""<div style='text-align: center; margin-top: 2rem;'>
                    <h1>🪐 Explore Exoplanets</h1>
                    <p style='text-align: center;'>Discover alien worlds beyond our solar system...</p>
                    </div>""", unsafe_allow_html=True)
    
    # 1. What are Exoplanets?
    st.markdown("---")
    st.markdown("""<div style='text-align: left; margin-top: 2rem;'>
                    <h2>🔭 What are Exoplanets?</h2>
                  </div>""", unsafe_allow_html=True)
    st.markdown("""
    An exoplanet is any planet beyond our solar system. Most of them orbit other stars, but some free-floating exoplanets, called rogue planets, are untethered to any star. We’ve confirmed more than 5,800 exoplanets out of the billions that we believe exist.  
    [🔗 Learn More](https://exoplanets.nasa.gov/what-is-an-exoplanet/)
    """)
    
    # 2. Famous Exoplanets
    st.markdown("---")
    st.markdown("""<div style='text-align: left; margin-top: 2rem;'>
                    <h2>🌟 Famous Exoplanets</h2>
                  </div>""", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("**🌍 Kepler-452b**")
        st.markdown("""
    An "Earth-cousin" that orbits a star like our sun in the habitable zone, where liquid water could exist.  
    [🔗 Learn More](https://science.nasa.gov/exoplanet-catalog/kepler-452-b/)
    """)
    with col2:
        st.markdown("**💎 55 Cancri e**")
        st.markdown("""
    This super hot world is covered in a global ocean of lava and has sparkling skies.    
    [🔗 Learn More](https://science.nasa.gov/exoplanet-catalog/55-cancri-e/)
    """)
    with col3:
        st.markdown("**🌬️ HD 189733b**")
        st.markdown("""
    This far-off blue planet may look like a friendly haven – but don’t be deceived! Weather here is deadly. The planet’s cobalt blue color comes from a hazy, blow-torched atmosphere containing clouds laced with glass.    
    [🔗 Learn More](https://science.nasa.gov/exoplanet-catalog/hd-189733-b/)
    """)

    col4, col5, col6 = st.columns(3)
    with col4:
        st.markdown("**🔮 TRAPPIST-1e**")
        st.markdown("""
    A terrestrial exoplanet that orbits an M-type star. Its mass is 0.692 Earths, it takes 6.1 days to complete one orbit of its star, and is 0.02925 AU from its star. Its discovery was announced in 2017.    
    [🔗 Learn More](https://science.nasa.gov/exoplanet-catalog/trappist-1-e/)
    """)
    with col5:
        st.markdown("**🧊 Gliese 581g**")
        st.markdown("""
    May have begun as a mini-Neptune, but is now a rocky world a little bigger than Earth. The planet may have lost one atmosphere but gained another from volcanic activity.    
    [🔗 Learn More](https://science.nasa.gov/exoplanet-catalog/gj-1132-b/)
    """)
    with col6:
        st.markdown("**🔥 WASP-12b**")
        st.markdown("""
    This doomed planet is a hot Jupiter that orbits so close to its parent star, it's being torn apart. It takes this alien world only 1.1 days to completely circle its sun.    
    [🔗 Learn More](https://science.nasa.gov/exoplanet-catalog/wasp-12-b/)
    """)
    st.markdown("---")
    st.markdown("""<div style='text-align: left; margin-top: 2rem;'>
                    <h2>🚀 Exploration Missions</h2>
                  </div>""", unsafe_allow_html=True)
    col7, col8 = st.columns(2)
    with col7:
        st.markdown("**🔭 Kepler**")
        st.markdown("""
                    The Kepler space telescope is a defunct space telescope launched by NASA in 2009 to discover Earth-sized planets orbiting other stars.    
                    [🔗 Learn More](https://en.wikipedia.org/wiki/Kepler_space_telescope)
                    """)
        st.markdown(" ")
        st.markdown("**📡 TESS**")
        st.markdown("""
                    Transiting Exoplanet Survey Satellite (TESS) is a space telescope for NASA's Explorer program, designed to search for exoplanets using the transit method in an area 400 times larger than that covered by the Kepler mission.    
                    [🔗 Learn More](https://en.wikipedia.org/wiki/Transiting_Exoplanet_Survey_Satellite)
                    """)           
    with col8:
        st.markdown("**🌠 JWST**")
        st.markdown("""
                    The James Webb Space Telescope (JWST) is a space telescope designed to conduct infrared astronomy. As the largest telescope in space, it is equipped with high-resolution and high-sensitivity instruments, allowing it to view objects too old, distant, or faint for the Hubble Space Telescope.    
                    [🔗 Learn More](https://en.wikipedia.org/wiki/James_Webb_Space_Telescope)
                    """)
        st.markdown(" ")
        st.markdown("**🛰️ PLATO (Coming soon)**")
        st.markdown("""
                    Planetary Transits and Oscillations of stars (PLATO) is a space telescope under development by the European Space Agency for launch in 2026.    
                    [🔗 Learn More](https://en.wikipedia.org/wiki/PLATO_(spacecraft))
                    """)

    st.markdown("---")    
    st.markdown("""<div style='text-align: left; margin-top: 2rem;'>
                    <h2>📊 Exoplanet Stats</h2>
                  </div>""", unsafe_allow_html=True)
    st.markdown("""
    - 🌌 **Discovered so far**: Over 5,000  
    - 🧬 **Earth-like**: Around 60  
    - 💠 **Habitable Zone Planets**: 30+  
    [🌐 More Data](https://exoplanetarchive.ipac.caltech.edu/)
    """)

    st.markdown("""---""")
    st.markdown("""
    <div style='text-align: center;'>
        <h2>🪐 Exploring Distant Worlds</h2>
        <p style='font-size:18px;'>
            Exoplanets remind us that our universe is vast, mysterious, and full of possibilities. 🌌<br><br>
            From gas giants to Earth-like worlds, each discovery brings us closer to answering the ultimate question: <br><br>
            <strong>Are we alone?</strong><br><br>
            Keep looking up. The next Earth could be just a telescope away! 🔭
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <br><br>
    <div style='text-align: right; font-size:18px; margin-right: 30px;'>
        <b>Next: 🚀 Missions ➡️</b>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.active_tab == "🚀 Missions":
    st.markdown("<h1 style='text-align: center;'>🚀 Space Missions</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Explore humanity’s boldest steps into the cosmos.</p>", unsafe_allow_html=True)
    
    st.divider()
    #Historic Missions
    st.markdown("### 🕰️ Historic Missions")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**🌕 Apollo 11**")
        st.markdown("""
        - **Objective**: Perform a crewed lunar landing and return to Earth.
        - **Launch Date**: July 16, 1969
        - **Highlights**: Neil Armstrong and Buzz Aldrin became the first humans to walk on the Moon on July 20, 1969.  
        - **Learn More**: [NASA Apollo 11 Overview](https://www.nasa.gov/missions/apollo-11-mission-overview/)
        """)
    with col2:
        st.markdown("**🛰️ Sputnik 1**")
        st.markdown("""
        - **Objective**: First artificial Earth satellite.
        - **Launch Date**: October 4, 1957
        - **Highlights**: Marked the beginning of the space age and the U.S.-U.S.S.R space race.  
        - **Learn More**: [Sputnik 1 - Wikipedia](https://en.wikipedia.org/wiki/Sputnik_1)
        """)
    col3, col4 = st.columns(2)
    with col3:
        st.markdown("**🚀 Voyager 1**")
        st.markdown("""
        - **Objective**: Study the outer Solar System and interstellar space.
        - **Launch Date**: September 5, 1977
        - **Highlights**: First spacecraft to reach interstellar space; still transmitting data.  
        - **Learn More**: [NASA Voyager Mission](https://voyager.jpl.nasa.gov/)
        """)
    with col4:
        st.markdown("**🛸 Luna 2**")
        st.markdown("""
        - **Objective**: First human-made object to reach the Moon.
        - **Launch Date**: September 12, 1959
        - **Highlights**: Impacted the Moon's surface, confirming that the Moon had no significant magnetic field.  
        - **Learn More**: [Luna 2 - Wikipedia](https://en.wikipedia.org/wiki/Luna_2)
        """)
    
    st.divider()
    #Current Missions
    st.markdown("### 🛰️ Current Missions")
    col5, col6 = st.columns(2)
    with col5:
        st.markdown("**🔭 James Webb Space Telescope (JWST)**")
        st.markdown("""
        - **Objective**: Observe the universe's first galaxies, stars, and planetary systems.
        - **Launch Date**: December 25, 2021
        - **Highlights**: Provides unprecedented infrared observations from the second Lagrange point (L2).  
        - **Learn More**: [NASA JWST Mission](https://science.nasa.gov/mission/webb/)
        """)
    with col6:
        st.markdown("**🚁 Perseverance & Ingenuity (Mars 2020)**")
        st.markdown("""
        - **Objective**: Search for signs of ancient life and collect Martian soil samples.
        - **Launch Date**: July 30, 2020
        - **Highlights**: Perseverance rover is exploring Mars; Ingenuity helicopter achieved the first powered flight on another planet.  
        - **Learn More**: [NASA Mars 2020 Mission](https://mars.nasa.gov/mars2020/)
        """)
    col7, col8 = st.columns(2)
    with col7:
        st.markdown("**🛰️ Artemis I**")
        st.markdown("""
        - **Objective**: Uncrewed test flight around the Moon to prepare for future crewed missions.
        - **Launch Date**: November 16, 2022
        - **Highlights**: Successfully tested NASA's Space Launch System and Orion spacecraft.  
        - **Learn More**: [NASA Artemis I Mission](https://www.nasa.gov/artemis-1)
        """)
    with col8:
        st.markdown("**🪐 Juno**")
        st.markdown("""
        - **Objective**: Study Jupiter's composition, gravity field, magnetic field, and polar magnetosphere.
        - **Launch Date**: August 5, 2011
        - **Highlights**: Provided detailed images and data about Jupiter's atmosphere and magnetic field.  
        - **Learn More**: [NASA Juno Mission](https://www.nasa.gov/mission_pages/juno/main/index.html)
        """)

    st.divider()
    #Future & Upcoming Missions
    st.markdown("### 🔮 Future & Upcoming Missions")
    col9, col10 = st.columns(2)
    with col9:
        st.markdown("**🚀 Artemis II**")
        st.markdown("""
        - **Objective**: First crewed mission to orbit the Moon since Apollo 17.
        - **Planned Launch**: Early 2026
        - **Highlights**: Will test life-support systems and demonstrate capabilities for deep space missions.  
        - **Learn More**: [NASA Artemis II Mission](https://www.nasa.gov/artemis-ii)
        """)
    with col10:
        st.markdown("**🌌 LUVOIR (Large UV Optical Infrared Surveyor)**")
        st.markdown("""
        - **Objective**: Proposed space telescope to study a broad range of astrophysical questions.
        - **Status**: Conceptual design phase
        - **Highlights**: Aims to detect exoplanets and characterize their atmospheres.  
        - **Learn More**: [NASA LUVOIR Concept](https://asd.gsfc.nasa.gov/luvoir/)
        """)
    col11, col12 = st.columns(2)
    with col11:
        st.markdown("**🪐 Dragonfly**")
        st.markdown("""
        - **Objective**: Explore Titan's prebiotic chemistry and habitability.
        - **Planned Launch**: July 2028
        - **Highlights**: Will use a rotorcraft to fly to multiple locations on Titan.  
        - **Learn More**: [NASA Dragonfly Mission](https://dragonfly.jhuapl.edu/)
        """)
    with col12:
        st.markdown("**🌍 Mars Sample Return**")
        st.markdown("""
        - **Objective**: Retrieve samples collected by Perseverance and return them to Earth.
        - **Planned Launch**: Late 2020s
        - **Highlights**: A collaborative effort between NASA and ESA to bring Martian samples to Earth.  
        - **Learn More**: [Mars Sample Return](https://science.nasa.gov/mission/mars-sample-return/)
        """)
    
    st.divider()
    st.markdown("<h2 style='text-align: center;'>🔬 Key Space Experiments</h2>", unsafe_allow_html=True)

    exp1, exp2 = st.columns(2)

    with exp1:
        st.markdown("**🧪 Microgravity Science**")
        st.markdown("""
        ISS experiments show how microgravity affects fluids, fire, and human biology.
        [Learn more](https://en.wikipedia.org/wiki/Scientific_research_on_the_International_Space_Station)
    """)
        st.markdown("**🧬 GeneLab on ISS**")
        st.markdown("""
        Research on DNA and gene behavior in space—vital for long-duration missions.
        [Learn more](https://www.nasa.gov/osdr-genelab-about/)
    """)

    with exp2:
        st.markdown("**🥬 Veggie Experiment**")
        st.markdown("""
        Growing plants aboard the ISS to support food sustainability in space.
        [Learn more](https://science.nasa.gov/mission/veggie/)
    """)
        st.markdown("**🛰 Cold Atom Lab**")
        st.markdown("""
        The first quantum physics lab in space—studies ultra-cold atoms in microgravity.
        [Learn more](https://www.jpl.nasa.gov/missions/cold-atom-laboratory-cal/)
    """)

    # Earth Missions Section
    st.divider()
    st.markdown("<h2 style='text-align: center;'>🌍 Earth-Focused Missions</h2>", unsafe_allow_html=True)

    earth1, earth2 = st.columns(2)

    with earth1:
        st.markdown("**🌀 Sentinel-6 Michael Freilich**")
        st.markdown("""
        Measures sea level rise, ocean circulation, and climate change indicators.
        [Learn more](https://www.nasa.gov/sentinel-6/)
    """)
        st.markdown("**🌦️ GPM (Global Precipitation Measurement)**")
        st.markdown("""
        Tracks global rainfall and weather patterns in real time.
        [Learn more](https://gpm.nasa.gov/)
    """)

    with earth2:
        st.markdown("**🌍 Landsat 9**")
        st.markdown("""
        Continues a 50-year mission of capturing satellite imagery of Earth’s surface.
        [Learn more](https://landsat.gsfc.nasa.gov/landsat-9/)
    """)
        st.markdown("**🌬️ OCO-2 (Carbon Observatory)**")
        st.markdown("""
        Monitors global CO₂ levels to study Earth’s carbon cycle.
        [Learn more](https://science.nasa.gov/mission/oco-2/)
    """)

    # Mission of the Month Section
    st.divider()
    st.markdown("<h2 style='text-align: center;'>🧭 Mission of the Month</h2>", unsafe_allow_html=True)

    st.markdown("""
    <div style='text-align: center;'>
    <h2>🌖 Europa Clipper</h4>
    <h6>Launched in 2024, Europa Clipper will explore Jupiter’s icy moon Europa to determine if it could support life. It will carry a suite of scientific instruments to scan the moon’s surface, subsurface ocean, and magnetic environment.</h6>
    <a href='https://europa.nasa.gov/' target='_blank'>🔗 Learn More</a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""---""")
    st.markdown("""
    <div style='text-align: center;'>
        <h2>🚀 Missions: Humanity's Bold Steps into the Cosmos</h2>
        <p style='font-size:18px;'>
            Every mission — from Apollo to Perseverance to future journeys to Mars — tells a story of courage, innovation, and discovery. 🌍🌌<br><br>
            These are not just spacecraft — they are dreams launched into the stars.<br><br>
            🌠 The next giant leap could be just around the corner. Stay tuned, stay inspired!
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <br><br>
    <div style='text-align: right; font-size:18px; margin-right: 30px;'>
        <b>Next: ⚙️ Tech ➡️</b>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.active_tab == "⚙️ Tech":
    st.markdown("""
    <h1 style='text-align: center; margin-top: 1rem;'>⚙️ Space Technology</h1>
    <p style='text-align: center; font-size: 18px;'>Explore the incredible technology powering our journey into the cosmos!</p>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🚀 Propulsion Systems")
    propsys1, propsys2 = st.columns(2)    
    with propsys1:
        st.markdown("""
        - **💥 Ion Thrusters** – Ion thrusters use electricity to accelerate ions, producing a small but continuous thrust. Although they’re not powerful enough to launch spacecraft from Earth, they are incredibly efficient for long-distance missions in space. NASA’s Dawn spacecraft used ion propulsion to explore Vesta and Ceres in the asteroid belt.  [🔗Learn More](https://en.wikipedia.org/wiki/Ion_thruster)
        - **🔥 Chemical Rockets** – Chemical rockets are the most commonly used propulsion system for space launches. By igniting fuel and oxidizer in a combustion chamber, they generate high-pressure exhaust that propels spacecraft into orbit. They are powerful and reliable, ideal for lifting heavy payloads from Earth.  [🔗Learn More](https://en.wikipedia.org/wiki/Rocket_engine)
        """)
    with propsys2:
        st.markdown("""
        - **⚛️ Nuclear Thermal Propulsion** – Nuclear thermal propulsion involves heating a liquid propellant, like hydrogen, using a nuclear reactor, and expelling it to produce thrust. This method could cut travel time to Mars in half and is being explored as a future deep space transportation method.  [🔗Learn More](https://en.wikipedia.org/wiki/Nuclear_thermal_rocket)
        - **🌕 Solar Sails** – Solar sails harness the pressure of sunlight to propel spacecraft. They have no fuel requirements and are ideal for extremely long-duration missions. NASA’s NEA Scout and the Planetary Society’s LightSail projects use this innovative propulsion system.  [🔗Learn More](https://en.wikipedia.org/wiki/Solar_sail)
        """)
    st.markdown("---")

    st.markdown("### 👨‍🚀 Space Suits & Life Support")
    suits1, suits2 = st.columns(2)    
    with suits1:
        st.markdown("""
        - **🧑‍🚀 Artemis AxEMU Suits** – NASA's Exploration Extravehicular Mobility Unit (xEMU) suits are designed for the Artemis missions. They offer improved mobility, better dust protection, and longer life support than previous suits, allowing astronauts to explore the Moon's surface more effectively.  [🔗Learn More](https://www.axiomspace.com/axiom-suit)
        - **🧊 Life Support Systems** – Life support systems maintain habitable conditions for astronauts, controlling oxygen, carbon dioxide, humidity, and temperature. On the ISS, these systems recycle air and water, ensuring long-term survival in space.  [🔗Learn More](https://en.wikipedia.org/wiki/Life-support_system)
        """)
    with suits2:
        st.markdown("""
        - **🔬 Radiation Protection** – Space suits and habitats must shield astronauts from harmful radiation. Modern designs include multi-layer insulation and radiation-blocking materials, essential for deep space missions beyond Earth’s magnetic field.  [🔗Learn More](https://en.wikipedia.org/wiki/Life-support_system)
        - **💨 CO₂ Scrubbers** – CO₂ scrubbers are critical components in spacecraft. They remove carbon dioxide exhaled by astronauts using chemical absorbers, keeping air breathable and preventing toxic buildup in closed environments.  [🔗Learn More](https://en.wikipedia.org/wiki/Solar_sail)
        """)
    st.markdown("---")
    
    st.markdown("### 🤖 Rovers & Robotics")
    rovers1, rovers2 = st.columns(2)    
    with rovers1:
        st.markdown("""
        - **🤖 Perseverance Rover** – NASA’s Perseverance rover explores Mars with advanced AI, capable of autonomous navigation and sample collection. It's searching for signs of ancient life and caching samples for a future return mission.  [🔗Learn More](https://science.nasa.gov/mission/mars-2020-perseverance/)
        - **🐾 Autonomous Navigation** – Modern rovers like Perseverance use computer vision and AI to avoid obstacles and make real-time decisions. This allows them to cover more ground efficiently without waiting for Earth-based commands.  [🔗Learn More](https://www.nasa.gov/solar-system/nasas-self-driving-perseverance-mars-rover-takes-the-wheel/)
        """)
    with rovers2:
        st.markdown("""
        - **🔧 Robotic Arms** – Rovers are equipped with robotic arms that can drill, collect soil samples, and analyze rock textures. These tools are essential for scientific discovery on planetary surfaces.  [🔗Learn More](https://science.nasa.gov/planetary-science/programs/mars-exploration/rover-basics/)
        - **🛠️ In-Space Assembly Robots** – Future missions will rely on robots to build space structures. NASA and companies like Made In Space are developing robotic systems for satellite repair and orbital construction.   [🔗Learn More](https://www-robotics.jpl.nasa.gov/what-we-do/research-tasks/in-space-robotic-assembly-and-maintenance/)
        """)
    st.markdown("---")

    st.markdown("### 🪟 Space Habitats")
    hab1, hab2 = st.columns(2)    
    with hab1:
        st.markdown("""
        - **🛰️ Lunar Gateway** – The Lunar Gateway is a planned space station that will orbit the Moon. It will serve as a research lab, crew transfer station, and support platform for lunar surface missions and deep space travel.  [🔗Learn More](https://www.nasa.gov/mission/gateway/)
        - **🧱 3D-Printed Moon Bases** – Using lunar regolith as raw material, 3D printing technology could build durable shelters on the Moon. This reduces the need to transport heavy materials from Earth, making lunar colonization more feasible.  [🔗Learn More](https://www.nasa.gov/technology/manufacturing-materials-3-d-printing/nasa-looks-to-advance-3d-printing-construction-systems-for-the-moon-and-mars/)
        """)
    with hab2:
        st.markdown("""
        - **🌱 BioDomes** – BioDomes are closed-loop ecosystems designed to grow food in space. They recycle air and water, offering a sustainable way to support life during long missions or on other planets.  [🔗Learn More](https://wonderopolis.org/wonder/What-Is-a-Biodome)
        - **🏠 Inflatable Modules** – Inflatable habitats like Bigelow’s BEAM are compact during launch and expand in space, providing more room with less weight. They are being tested for future use on the Moon and Mars.   [🔗Learn More](https://en.wikipedia.org/wiki/Bigelow_Expandable_Activity_Module)
        """)
    st.markdown("---")

    st.markdown("### 📡 Satellite Technology")
    sat1, sat2 = st.columns(2)    
    with sat1:
        st.markdown("""
        - **📡 CubeSats** – CubeSats are miniature satellites used for low-cost scientific experiments, technology testing, and student projects. Despite their small size, they can perform many of the same functions as larger satellites.  [🔗Learn More](https://www.nasa.gov/what-are-smallsats-and-cubesats/)
        - **🛰️ Communication Satellites** – These satellites relay television, radio, and internet signals across the globe. Positioned in geostationary orbit, they form the backbone of global communication infrastructure.  [🔗Learn More](https://en.wikipedia.org/wiki/Communications_satellite)
        """)
    with sat2:
        st.markdown("""
        - **🗺️ Earth Observation Tech** – Satellites equipped with high-resolution cameras and sensors monitor the Earth’s surface, tracking environmental changes, natural disasters, and human activity for science and security.  [🔗Learn More](https://en.wikipedia.org/wiki/Earth_observation_satellite)
        - **🌍 Navigation Satellites** – Systems like GPS rely on satellites to provide real-time location data. They support everything from navigation apps to military operations and scientific surveys.   [🔗Learn More](https://en.wikipedia.org/wiki/Satellite_navigation)
        """)
    st.markdown("---")

    st.markdown("### 🧠 Advanced Materials & AI")
    ai1, ai2 = st.columns(2)    
    with ai1:
        st.markdown("""
        - **🧪 Aerogels** – Aerogels are ultra-light materials known for their insulating properties. Used in rovers and suits, they help protect astronauts and electronics from extreme space temperatures.  [🔗Learn More](https://en.wikipedia.org/wiki/Aerogel)
        - **⚙️ Shape Memory Alloys** – These smart materials return to a preset shape after deformation. They’re used in robotic actuators and deployable structures for space missions.  [🔗Learn More](https://en.wikipedia.org/wiki/Shape-memory_alloy)
        """)
    with ai2:
        st.markdown("""
        - **🔍 Smart Sensors** – Advanced sensors with AI processing are used to monitor spacecraft systems, planetary environments, and even astronaut health in real-time.  [🔗Learn More](https://sensorpartners.com/en/knowledge-base/artificial-intelligenc-and-sensors-a-powerful-combination/#:~:text=Smart%20home%3A%20AI%20is%20used,a%20car%20without%20human%20input.)
        - **🧠 AI in Spacecraft** – AI enhances spacecraft with autonomous decision-making, data analysis, and fault detection. It allows missions to respond to unforeseen challenges without relying on Earth-based commands.   [🔗Learn More](https://www.nasa.gov/organizations/ocio/dt/ai/2024-ai-use-cases/)
        """)
    st.markdown("---")

    st.markdown("### 🔋 Energy Systems")
    enrgy1, enrgy2 = st.columns(2)    
    with enrgy1:
        st.markdown("""
        - **🛰️ Solar Panels on ISS** – The International Space Station uses massive solar arrays to generate electricity. These panels are carefully oriented to capture sunlight as the station orbits Earth.  [🔗Learn More](https://www.nasa.gov/image-article/solar-arrays-international-space-station-2/)
        - **☀️ Next-gen Solar Arrays** – New designs feature flexible, foldable panels with higher efficiency and lighter weight, ideal for future missions where mass and space are limited.  [🔗Learn More](https://news.mit.edu/2021/photovoltaic-efficiency-solar-0224)
        """)
    with enrgy2:
        st.markdown("""
        - **🔌 Nuclear Batteries** – Radioisotope Thermoelectric Generators (RTGs) convert heat from radioactive decay into electricity. Used on missions like Voyager and Curiosity, they provide long-lasting power far from the Sun.  [🔗Learn More](https://en.wikipedia.org/wiki/Atomic_battery)
        - **⚡ Wireless Power Transfer** – Future missions may use beamed microwaves or lasers to transfer power across space, enabling remote charging of rovers or lunar bases.  [🔗Learn More](https://en.wikipedia.org/wiki/Wireless_power_transfer)
        """)
    st.markdown("---")

    st.markdown("### 🧪 Experimental Tech")
    exptech1, exptech2 = st.columns(2)    
    with exptech1:
        st.markdown("""
        - **🧲 Magnetic Shielding** – Magnetic fields can protect astronauts from cosmic rays and solar radiation. Researchers are testing this concept to create a safer space environment for long-duration missions.  [🔗Learn More](https://en.wikipedia.org/wiki/Electromagnetic_shielding#Magnetic_shielding)
        - **🌐 Space Elevators** – A space elevator would connect Earth’s surface to orbit using a super-strong cable. Though still theoretical, it could revolutionize space travel by making launches cheaper and safer.  [🔗Learn More](https://en.wikipedia.org/wiki/Space_elevator)
        """)
    with exptech2:
        st.markdown("""
        - **📦 Autonomous Cargo Landers** – SpaceX and other companies are developing spacecraft that can deliver supplies to the Moon or Mars autonomously, enabling frequent and reliable resupply missions.  [🔗Learn More](https://en.wikipedia.org/wiki/Starship_HLS)
        - **🛸 Plasma Propulsion** – This cutting-edge system uses superheated ionized gas for high-speed space travel. It offers potential for interplanetary journeys much faster than current technology.   [🔗Learn More](https://en.wikipedia.org/wiki/Plasma_propulsion_engine)
        """)

    st.markdown("""---""")
    st.markdown("""
    <div style='text-align: center;'>
        <h2>⚙️ The Future is Being Built</h2>
        <p style='font-size:18px;'>
            Every new engine, habitat, AI, and satellite brings humanity one step closer to becoming an interplanetary species. 🌍🚀<br><br>
            Space technology is not just science fiction anymore — it’s shaping the future of exploration, survival, and discovery.<br><br>
            🛠️ Keep watching the stars, and the innovations that get us there!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <br><br>
    <div style='text-align: right; font-size:18px; margin-right: 30px;'>
        <b>Next: 🧬 Astrobiology ➡️</b>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.active_tab == "🧬 Astrobiology":
    st.markdown("""
    <h1 style='text-align: center; margin-top: 1rem;'>🧬 Astrobiology</h1>
    <p style='text-align: center; font-size: 18px;'>Explore the origins, evolution, and possibilities of life beyond Earth. 🧬🌌</p>
    """, unsafe_allow_html=True)
    st.divider()
    
    st.subheader("🌌 What is Astrobiology?")
    st.write("Astrobiology is the scientific study of life in the universe — its origins, evolution, distribution, and future. It combines biology, chemistry, physics, and planetary science to understand if life exists beyond Earth, and how it could thrive in different environments.")
    st.markdown("[Learn More](https://astrobiology.nasa.gov/)")
    st.divider()
    
    st.subheader("🌡️ Conditions for Life")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("💧 Liquid Water")
        st.write("Water is essential because it’s a perfect solvent for life's chemistry. Most life as we know it depends on the presence of liquid water.")
        st.markdown("[Learn More](https://astrobiology.nasa.gov/education/alp/water-so-important-for-life/#:~:text=Water%20has%20been%20found%20in,to%20understanding%20how%20life%20works.)")

        st.markdown("🌎 Stable Atmosphere")
        st.write("An atmosphere protects life from harmful radiation and helps regulate surface temperatures, making a planet habitable.")
        st.markdown("[Learn More](https://en.wikipedia.org/wiki/Extraterrestrial_atmosphere)")

    with col2:
        st.markdown("🌡️ Right Temperature")
        st.write("Planets need to be in the 'Goldilocks Zone' — not too hot and not too cold — so water can stay liquid.")
        st.markdown("[Learn More](https://science.nasa.gov/solar-system/temperatures-across-our-solar-system/)")

        st.markdown("☀️ Energy Source")
        st.write("A constant energy supply, like sunlight or geothermal heat, is necessary to power life processes.")
        st.markdown("[Learn More](https://en.wikipedia.org/wiki/Solar_energy)")
    st.divider()
    
    st.subheader("🧊 Extremophiles on Earth")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("🔥 Life in Hydrothermal Vent")
        st.write("Microbes thrive deep underwater at boiling temperatures, proving that sunlight isn't required for life.")
        st.markdown("[Learn More](https://en.wikipedia.org/wiki/Hydrothermal_vent#:~:text=Hydrothermal%20vent%20communities%20are%20able,large%20population%20of%20chemoautotrophic%20bacteria.)")

        st.markdown("❄️ Life Beneath Antarctic Ice")
        st.write("Bacteria and algae survive under kilometers of ice, hinting at possibilities for life on icy moons like Europa.")
        st.markdown("[Learn More](https://www.bbc.com/future/article/20221202-the-rich-marine-life-under-frozen-ice)")

    with col2:
        st.markdown("🧪 Life in Acidic Lakes")
        st.write("Some microbes flourish in highly acidic, toxic lakes, showing how adaptable life can be.")
        st.markdown("[Learn More](https://en.wikipedia.org/wiki/Ephemeral_acid_saline_lake)")

        st.markdown("🧂 Halophiles in Salt Flats")
        st.write("Salt-loving microbes inhabit extremely salty environments, similar to possible conditions on Mars.")
        st.markdown("[Learn More](https://en.wikipedia.org/wiki/Halophile)")
    st.divider()

    st.subheader("🧪 Famous Experiments")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("⚡ Miller-Urey Experiment")
        st.write("In 1953, scientists simulated early Earth conditions and produced amino acids — life's building blocks — showing that organic molecules can form naturally.")
        st.markdown("[Learn More](https://en.wikipedia.org/wiki/Miller%E2%80%93Urey_experiment)")

        st.markdown("🧬 RNA World Hypothesis")
        st.write("Suggests that life may have started with self-replicating RNA molecules before DNA-based life evolved.")
        st.markdown("[Learn More](https://en.wikipedia.org/wiki/RNA_world)")

    with col2:
        st.markdown("☄️ Panspermia Theory")
        st.write("The idea that life or its ingredients may have been delivered to Earth via comets or meteorites.")
        st.markdown("[Learn More](https://en.wikipedia.org/wiki/Panspermia)")

        st.markdown("🌋 Deep-Sea Vent Theory")
        st.write("Suggests that life began in deep-sea vents, protected from surface dangers like asteroid impacts.")
        st.markdown("[Learn More](https://en.wikipedia.org/wiki/Hydrothermal_vent#:~:text=One%20current%20theory%20is%20that,components%20present%20in%20modern%20cells.)")
    st.divider()

    st.subheader("🪐 Potential Places for Life")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("🔴 Mars")
        st.write("Mars has water ice, ancient riverbeds, and seasonal methane releases — possible hints of past or even underground life.")
        st.markdown("[Learn More](https://mars.nasa.gov/)")

        st.markdown("🌊 Europa")
        st.write("Jupiter’s icy moon Europa holds a global ocean beneath its crust, making it a top target for finding alien microbes.")
        st.markdown("[Learn More](https://europa.nasa.gov/why-europa/europa-up-close/)")

    with col2:
        st.markdown("🧊 Enceladus")
        st.write("Saturn's moon Enceladus has geysers shooting water into space, suggesting a subsurface ocean with potential for life.")
        st.markdown("[Learn More](https://science.nasa.gov/saturn/moons/enceladus/)")

        st.markdown("🌑 Titan")
        st.write("Titan has lakes of liquid methane and a thick atmosphere — could exotic, methane-based life exist there?")
        st.markdown("[Learn More](https://solarsystem.nasa.gov/moons/saturn-moons/titan/overview/)")
    st.divider()

    st.subheader("🔎 Search for Biosignatures")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("🌀 Oxygen and Methane")
        st.write("Scientists look for unexpected gases like oxygen and methane in exoplanet atmospheres, which could hint at biological activity.")
        st.markdown("[Learn More](https://www.nasa.gov/missions/with-mars-methane-mystery-unsolved-curiosity-serves-scientists-a-new-one-oxygen/)")

        st.markdown("🎯 Spectroscopy Techniques")
        st.write("Analyzing light from distant worlds reveals atmospheric chemicals — a key method for biosignature detection.")
        st.markdown("[Learn More](https://science.nasa.gov/mission/hubble/science/science-behind-the-discoveries/hubble-spectroscopy/)")

    with col2:
        st.markdown("📡 Technosignatures")
        st.write("Scientists also search for evidence of technology, such as radio waves or industrial pollution on distant planets.")
        st.markdown("[Learn More](https://science.nasa.gov/universe/search-for-life/searching-for-signs-of-intelligent-life-technosignatures/)")

        st.markdown("🧪 Organic Molecules on Mars")
        st.write("The Curiosity rover has detected complex organics in Martian soil — key ingredients for life.")
        st.markdown("[Learn More](https://www.nasa.gov/news-release/nasa-finds-ancient-organic-material-mysterious-methane-on-mars/)") 
    st.divider()

    st.subheader("📈 The Drake Equation")
    st.write("Developed by Frank Drake, this famous formula estimates the number of active, communicative extraterrestrial civilizations in the Milky Way.")
    st.markdown("[Learn More](https://en.wikipedia.org/wiki/Drake_equation)")
    st.divider()

    st.markdown("📡Messages to Space")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("🔭 SETI (Search for Extraterrestrial Intelligence)")
        st.write("SETI listens for artificial radio signals from space that might indicate alien civilizations.")
        st.markdown("[Learn More](https://en.wikipedia.org/wiki/Search_for_extraterrestrial_intelligence)")

        st.markdown("📜 Arecibo Message")
        st.write("In 1974, a powerful radio message was sent from Earth to a distant star cluster, designed to introduce humanity to alien civilizations.")
        st.markdown("[Learn More](https://en.wikipedia.org/wiki/Arecibo_message)")

    with col2:
        st.markdown("🌌 Voyager Golden Record")
        st.write("The Voyager spacecrafts carry a golden record with images and sounds from Earth, intended as a message for any extraterrestrials.")
        st.markdown("[Learn More](https://en.wikipedia.org/wiki/Voyager_Golden_Record)")

        st.markdown("🛰️ Breakthrough Listen")
        st.write("A project dedicated to scanning the skies for signs of advanced alien technologies using powerful radio telescopes.")
        st.markdown("[Learn More](https://breakthroughinitiatives.org/initiative/1)")
    st.divider()

    st.subheader("🚀 Astrobiology Missions")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("🔴 Mars Perseverance Rover")
        st.write("The rover is searching for ancient signs of microbial life and collecting samples to return to Earth.")
        st.markdown("[Learn More](https://mars.nasa.gov/mars2020/)")

        st.markdown("🛰️ Europa Clipper")
        st.write("A NASA mission launching soon to explore Europa’s ocean and search for signs of habitability.")
        st.markdown("[Learn More](https://europa.nasa.gov/)")

    with col2:
        st.markdown("🌖 Dragonfly Mission to Titan")
        st.write("A NASA drone-like spacecraft will explore Titan’s surface and chemistry, searching for prebiotic conditions.")
        st.markdown("[Learn More](https://dragonfly.jhuapl.edu/)")

        st.markdown("🛰️ James Webb Space Telescope")
        st.write("JWST is already analyzing exoplanet atmospheres for potential biosignatures.")
        st.markdown("[Learn More](https://jwst.nasa.gov/content/about/mission.html)")
    st.divider()

    st.subheader("🧬 Life Beyond DNA? 👾")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("🌌 Silicon-Based Life")
        st.write("Silicon, like carbon, can form complex molecules. Some scientists speculate that alien life could be based on silicon instead of carbon.")
        st.markdown("[Learn More](https://en.wikipedia.org/wiki/Silicon-based_life)")

        st.markdown("🔥 Plasma Lifeforms")
        st.write("Theoretical plasma-based life could exist inside stars or extreme environments, based purely on energy and particles.")
        st.markdown("[Learn More](https://en.wikipedia.org/wiki/Plasma-based_life)")

    with col2:
        st.markdown("❄️ Ammonia-Based Life")
        st.write("Instead of water, some life might use ammonia as a solvent, especially on colder planets and moons.")
        st.markdown("[Learn More](https://en.wikipedia.org/wiki/Hypothetical_types_of_biochemistry#Ammonia)")

        st.markdown("🧠 Non-Carbon Consciousness")
        st.write("Speculative ideas include intelligent clouds of gas or purely electromagnetic 'life' with no physical form.")
        st.markdown("[Learn More](https://en.wikipedia.org/wiki/Hypothetical_types_of_biochemistry#Dusty_plasma-based)")

    st.markdown("""---""")
    st.markdown("""
    <div style='text-align: center;'>
        <h2>🛸 The Search Continues...</h2>
        <p style='font-size:18px;'>
            Astrobiology teaches us that life might be out there — waiting to be discovered among the stars. ✨<br><br>
            With every mission, every experiment, and every observation, we get closer to answering one of humanity’s greatest questions:<br>
            <b>Are we alone in the universe?</b>
        </p>
        <p style='font-size:18px;'>
            🔭 Stay tuned for the latest discoveries, missions, and breakthroughs!
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <br><br>
    <div style='text-align: right; font-size:18px; margin-right: 30px;'>
        <b>Next: ⌛ Black Holes ➡️</b>
    </div>
    """, unsafe_allow_html=True)

if st.session_state.active_tab == "⌛ Black Holes":
    st.markdown("<h1 style='text-align: center;'>⌛ Black Holes</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Explore the most mysterious and powerful objects in the universe — black holes! 🌌</p>", unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### 🕳️ What Are Black Holes?")
    st.write("""
    Black holes are regions in space where gravity is so intense that nothing—not even light—can escape. 
    They form from the collapse of massive stars after they burn out their nuclear fuel. 
    Rather than sucking everything nearby, black holes only affect objects that come very close. 
    They were predicted by Einstein's theory of general relativity and later confirmed through astronomical observations.
    """)
    st.markdown("[🔗 Learn More](https://science.nasa.gov/astrophysics/focus-areas/black-holes)")

    st.markdown("---")

    st.markdown("### 🔭 Types of Black Holes")
    st.write("""
    Black holes come in different sizes:
    - **Stellar Black Holes**: Created from collapsing massive stars.
    - **Supermassive Black Holes**: Found at galactic centers, millions to billions of times the Sun's mass.
    - **Intermediate Black Holes**: Rare middleweights that may explain galactic formation.
    - **Primordial Black Holes**: Hypothetical black holes from the early universe.

    """)
    st.markdown("[🔗 Learn More](https://imagine.gsfc.nasa.gov/science/objects/black_holes1.html)")

    st.markdown("---")

    st.markdown("### 🧠 Anatomy of a Black Hole")
    st.write("""
    A black hole consists of:
    - **Event Horizon**: The boundary beyond which escape is impossible.
    - **Singularity**: The infinitely dense center.
    - **Accretion Disk**: A hot, glowing ring of matter falling inward, often visible by X-rays.

    """)
    st.markdown("[🔗 Learn More](https://science.nasa.gov/universe/black-holes/anatomy/)")

    st.markdown("---")

    st.markdown("### ⏳ Time Dilation and Black Holes")
    st.write("""
    Near black holes, time slows dramatically—a prediction of Einstein's theory.
    Objects falling into a black hole appear frozen at the event horizon to distant observers.
    Meanwhile, for the falling object, time passes normally but leads to an unavoidable fate.
    
    For advanced readers: Gravitational time dilation happens when time moves at different speeds depending on how close you are to something with a lot of gravity. If you're closer to a strong source of gravity (like a planet or a star), time passes more slowly for you. If you move farther away, time speeds up.

    Albert Einstein predicted this effect in his theory of relativity, and scientists have confirmed it with experiments. For example, atomic clocks placed at different heights (where gravity is slightly weaker or stronger) show tiny differences in time — just a few billionths of a second.

    Over billions of years, this tiny effect adds up: Earth's core is about 2.5 years younger than its surface! To see bigger time differences, we would need to measure farther away from Earth or near a much bigger gravitational source.
    """)
    st.markdown("[🔗 Learn More](https://science.nasa.gov/universe/what-happens-when-something-gets-too-close-to-a-black-hole/)")

    st.markdown("---")

    st.markdown("### 📸 Famous Black Holes")
    st.write("""
    Two major black holes made history:
    - **Sagittarius A\***: The supermassive black hole at our galaxy’s core.
    - **M87\***: The first black hole ever photographed, showing a stunning 'shadow'.

    These discoveries transformed black holes from theory to reality.
    """)
    st.markdown("[🔗 Learn More](https://en.wikipedia.org/wiki/List_of_most_massive_black_holes)")

    st.markdown("---")

    st.markdown("### 🌌🌀 Theoretical Concepts and Wild Ideas")
    st.write("""
    Exciting black hole theories include:
    - **Wormholes**: Hypothetical bridges through spacetime.
    - **White Holes**: Possible opposites that expel matter.
    - **Hawking Radiation**: The slow evaporation of black holes.
    - **Time Travel**: Speculative theories using spinning black holes.

    """)
    st.markdown("🔗 Learn More About: [Wormholes ](https://en.wikipedia.org/wiki/Wormhole), [White Holes ](https://en.wikipedia.org/wiki/White_hole), [Hawking Radiation ](https://en.wikipedia.org/wiki/Hawking_radiation), [Time Travel](https://en.wikipedia.org/wiki/Time_travel)")

    st.markdown("---")

    st.markdown("### 🤯 Mysteries That Puzzle Scientists")
    st.write("""
    Black holes leave scientists with big questions:
    - What happens at the singularity?
    - Is information lost forever?
    - Could black holes spawn new universes?

    Answering these could unlock quantum gravity theories.
    """)
    st.markdown("[🔗 Learn More](https://news.uchicago.edu/explainer/black-holes-explained)")

    st.markdown("---")

    st.markdown("### 📡 How We Observe Black Holes")
    st.write("""
    Even invisible, black holes reveal themselves by:
    - **X-ray emissions** from accretion disks.
    - **Gravitational waves** from black hole mergers.
    - **Star motions** indicating hidden massive objects.

    New tools like the Event Horizon Telescope are making the invisible visible.
    """)
    st.markdown("[🔗 Learn More](https://science.nasa.gov/universe/black-holes/#:~:text=Finding%20Black%20Holes&text=Scientists%20primarily%20detect%20and%20study,wavelengths%2C%20including%20X%2Drays.)")

    st.markdown("---")

    st.markdown("### 🚀 Black Holes and Future Space Travel")
    st.write("""
    Wild ideas suggest:
    - Using spinning black holes to generate energy (Penrose Process).
    - Using black holes as cosmic engines.
    - Exploring wormholes for interstellar shortcuts.

    Black holes continue to stretch the limits of our imagination.
    """)
    st.markdown("[🔗 Learn More](https://www.nsf.gov/news/could-we-harness-energy-black-holes)")

    st.markdown("---")

    st.markdown("""
    <div style='text-align: center; margin-top: 3rem;'>
        <h2>🌌 The Mystery Deepens...</h2>
        <p style='font-size: 18px;'>
            Black holes challenge everything we know about the universe — from gravity to the nature of time itself. 🕳️✨<br><br>
            As we explore deeper into space and decode the data from telescopes and simulations,<br>
            the secrets of the cosmos may finally begin to unfold.<br><br>
            🧠 Could black holes be keys to understanding the universe... or even gateways to others?<br><br>
            <b>Keep watching the skies. The story isn't over yet.</b>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <br><br>
    <div style='text-align: right; font-size:18px; margin-right: 30px;'>
        <b>Next: 📰 News ➡️</b>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.active_tab == "📰 News":
    st.markdown("""
        <div style='text-align: center; margin-top: 2rem;'>
            <h1>🚀 Latest Space News</h1>
            <p>Stay updated with breaking space missions, launches, and discoveries.</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    response = requests.get("https://api.spaceflightnewsapi.net/v4/articles/?limit=6")
    data = response.json()
    
    col1, col2 = st.columns(2)
    for i, article in enumerate(data["results"]):
        column = col1 if i % 2 == 0 else col2

        with column:
            st.image(article["image_url"], width=280, caption=None, use_container_width=False)
            st.markdown(f"### 📰 {article['title']}", unsafe_allow_html=True)
            st.markdown(f"{article['summary'][:150]}...", unsafe_allow_html=True)
            st.markdown(f"<a href='{article['url']}' target='_blank' style='color: #1f77b4; font-weight: bold;'>🔗 Read More</a>", unsafe_allow_html=True)
            st.markdown(" ")

    st.markdown("---")

    st.markdown("## 🗞️ This Week in Space")
    st.markdown("Get weekly updates in astronomy and space science.")
   
    API_KEY = "pub_83956fe7ac44c59d22831b1cd7d23e188272d"
    URL = f"https://newsdata.io/api/1/news?apikey=pub_83956fe7ac44c59d22831b1cd7d23e188272d&q=astronomy&language=en&category=science"

    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()  # Raise error for bad status codes
        data = response.json()

        if isinstance(data, dict) and "results" in data:
            results = data["results"]
            if results:
                col1, col2 = st.columns(2)

                for idx, article in enumerate(results[:6]):  # Adjust number of articles as needed
                    with (col1 if idx % 2 == 0 else col2):
                        st.markdown(f"### 📰 {article.get('title', 'No Title')}")
                        st.write(article.get('description', 'No description available.'))
                        st.markdown(f"[Read More]({article.get('link', '#')})")
            else:
                st.warning("⚠️ No results found.")
        else:
            st.error("🚫 Unexpected data format received from API.")

    except requests.exceptions.Timeout:
        st.error("⏳ The request timed out. Try again later.")
    except requests.exceptions.RequestException as e:
        st.error(f"🚨 An error occurred: {str(e)}")
    except ValueError:
        st.error("❌ Could not decode the response as JSON.")

    st.markdown("---")

    st.markdown("## 🧪 Science Spotlight")
    st.markdown("Get insights into fascinating space experiments, discoveries, and innovations from across the galaxy.")
    
    SCIENCE_URL = "https://newsdata.io/api/1/news?apikey=pub_83956fe7ac44c59d22831b1cd7d23e188272d&q=Space%20Discovery&language=en&category=science"

    response = requests.get(SCIENCE_URL, timeout=10)

    if response.status_code == 200:
        data = response.json()
        results = data.get("results", [])

        # Filter articles for relevant space or science content
        filtered_results = [
            article for article in results
            if ('space' in (article.get("title", "") or "").lower() or
                'space' in (article.get("description", "") or "").lower() or
                'science' in (article.get("title", "") or "").lower() or
                'science' in (article.get("description", "") or "").lower())
        ]

        if filtered_results:
            article = filtered_results[0]
            title = article.get("title", "No Title")
            description = article.get("description", "No summary available.")
            link = article.get("link", "#")

            st.markdown(f"#### {title}")
            st.write(description)
            st.markdown(f"[🔗 Read More]({link})", unsafe_allow_html=True)

        else:
            st.warning("⚠️ No space or science articles found at the moment.")
    else:
        st.error("🚫 Failed to fetch science news.")
        
    st.markdown("---")

    st.markdown("## 🗓️ Upcoming Events & Launches")
    st.markdown("Never miss an important mission, launch, or skywatching event.")

    try:
        launch_response = requests.get("https://ll.thespacedevs.com/2.2.0/launch/upcoming/?limit=6", timeout=10)
        launch_data = launch_response.json()
        launches = launch_data.get("results", [])

        if launches:
            col1, col2 = st.columns(2)

            for i, launch in enumerate(launches):
                column = col1 if i % 2 == 0 else col2
                with column:
                    st.markdown(f"### 🚀 {launch.get('name', 'No Name')}")
                    st.markdown(f"**Date:** {launch.get('net', 'TBD')}")
                    st.markdown(f"**Location:** {launch.get('pad', {}).get('location', {}).get('name', 'Unknown')}")
                    st.markdown(f"**Provider:** {launch.get('launch_service_provider', {}).get('name', 'Unknown')}")
                    st.markdown(f"[🔗 More Info]({launch.get('url', '#')})", unsafe_allow_html=True)
        else:
            st.warning("⚠️ No upcoming launches found right now.")
    except Exception as e:
        st.error("🚫 Failed to fetch upcoming launches.")

    st.markdown("---")

    st.markdown("## 🌐 Global Space News")
    st.markdown("Explore space updates from around the world – ISRO, CNSA, ESA, JAXA and more.")

    API_KEY = "pub_83956fe7ac44c59d22831b1cd7d23e188272d"
    GLOBAL_NEWS_URL = f"https://newsdata.io/api/1/news?apikey=pub_83956fe7ac44c59d22831b1cd7d23e188272d&q=ISRO OR CNSA OR ESA OR JAXA&language=en&category=science"

    try:
        response = requests.get(GLOBAL_NEWS_URL, timeout=10)
        if response.status_code == 200:
            data = response.json()
            articles = data.get("results", [])

            if articles:
                col1, col2 = st.columns(2)
                for i, article in enumerate(articles[:4]):  # Show top 4 articles
                    column = col1 if i % 2 == 0 else col2
                    with column:
                        st.markdown(f"#### 🌍 {article['title']}")
                        st.write(article.get('description', 'No description available.'))
                        st.markdown(f"[🔗 Read More]({article['link']})", unsafe_allow_html=True)
            else:
                st.warning("⚠️ No global articles found at the moment.")
        else:
            st.error("🚫 Failed to fetch global space news.")
    except Exception as e:
        st.error("🚫 Request failed or timed out.")

elif st.session_state.active_tab == "💬 Theories":
    st.title("💬 Public Theories")
    st.markdown("Share your space theories or browse what others think. Inspire and be inspired.")
    st.markdown("_This is a prototype version. Theories are not stored permanently and will reset when the app refreshes._")

    if "theories" not in st.session_state:
        st.session_state.theories = []

    # Input form
    name = st.text_input("Your Name")
    theory_title = st.text_input("Theory Title")
    theory_content = st.text_area("Your Theory")

    if st.button("📤 Submit"):
        if name.strip() and theory_title.strip() and theory_content.strip():
            new_theory = {
                "name": name.strip(),
                "title": theory_title.strip(),
                "content": theory_content.strip(),
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "reported": False
            }
            st.session_state.theories.append(new_theory)
            st.success("✅ Theory submitted!")
        else:
            st.error("⚠️ Name, title, and theory content are all required.")

    st.markdown("---")
    st.markdown("### 🌌 Theories from the Community")

    if not st.session_state.theories:
        st.info("No theories yet. Be the first to share!")
    else:
        for i, theory in enumerate(reversed(st.session_state.theories)):
            with st.container():
                st.markdown(f"**🧑 {theory['name']}**")
                st.markdown(f"### 📝 {theory['title']}")
                st.markdown(f"> {theory['content']}  \n*🕒 {theory['timestamp']}*")

                col1, col2 = st.columns(2)

                with col1:
                    if not theory["reported"]:
                        if st.button("🚩 Report", key=f"report_{i}"):
                            theory["reported"] = True
                            st.success("🚩 Report submitted for review.")
                    else:
                        st.info("Already reported.")

                with col2:
                    if st.button("🗑️ Delete (if yours)", key=f"delete_{i}"):
                        del st.session_state.theories[len(st.session_state.theories) - 1 - i]
                        st.success("Deleted successfully.")
                        st.rerun()

elif st.session_state.active_tab == "❓ Quizzes":
    for key in ['quiz_started', 'score', 'question_num', 'quiz_done', 'current_q', 'answered']:
        if key not in st.session_state:
            st.session_state[key] = False if key == 'quiz_started' else 0 if key in ['score', 'question_num'] else None

    st.title("🧠 Nova Quiz")
    st.markdown("Test your knowledge in Science, Space, Computers, Math, and General Trivia!")

    if not st.session_state.quiz_started:
        st.markdown("### 📋 Instructions")
        st.markdown("""
        - Select a **category** and **difficulty** level for your quiz.
        - You'll be asked **5 multiple-choice questions**.
        - Click **Submit** after selecting your answer.
        - Click **Next** to move to the next question.
        - Your final score will be shown at the end.
        - You can restart the quiz by clicking the **Quizzes** tab again.
        """)

        category_map = {
            "Science & Nature": 17,
            "General Knowledge": 9,
            "Computers": 18,
            "Mathematics": 19
        }

        col1, col2 = st.columns(2)
        with col1:
            category_choice = st.selectbox("🧬 Category", list(category_map.keys()))
        with col2:
            difficulty = st.selectbox("🎯 Difficulty", ["Easy", "Medium", "Hard"])

        if st.button("🚀 Start Quiz"):
            st.session_state.quiz_started = True
            st.session_state.category_id = category_map[category_choice]
            st.session_state.difficulty = difficulty.lower()
            st.session_state.score = 0
            st.session_state.question_num = 0
            st.session_state.current_q = None
            st.session_state.answered = False
            st.session_state.quiz_done = False
            st.rerun()

    elif not st.session_state.quiz_done:
        def fetch_question():
            url = f"https://opentdb.com/api.php?amount=1&category={st.session_state.category_id}&type=multiple&difficulty={st.session_state.difficulty}"
            res = requests.get(url)
            if res.status_code == 200:
                data = res.json()
                if data["results"]:
                    qd = data["results"][0]
                    q = html.unescape(qd["question"])
                    correct = html.unescape(qd["correct_answer"])
                    incorrect = [html.unescape(i) for i in qd["incorrect_answers"]]
                    opts = incorrect + [correct]
                    random.shuffle(opts)
                    return q, opts, correct
            return None, None, None

        if st.session_state.current_q is None:
            q, opts, ans = fetch_question()
            if q:
                st.session_state.current_q = (q, opts, ans)
            else:
                st.warning("Could not load a question. Try again.")
                st.stop()

        q, opts, ans = st.session_state.current_q

        st.markdown(f"### Question {st.session_state.question_num + 1}")
        st.write(q)

        selected = st.radio("Choose your answer:", opts, index=None, key=f"q{st.session_state.question_num}")

        if not st.session_state.answered and st.button("✅ Submit"):
            if selected == ans:
                st.success("✅ Correct!")
                st.session_state.score += 1
            else:
                st.error(f"❌ Incorrect! The correct answer was: **{ans}**")
            st.session_state.answered = True

        if st.session_state.answered:
            if st.button("➡️ Next"):
                st.session_state.question_num += 1
                st.session_state.current_q = None
                st.session_state.answered = False
                if st.session_state.question_num >= 5:
                    st.session_state.quiz_done = True
                st.rerun()

    else:
        st.balloons()
        st.markdown("## 🎉 Quiz Completed!")
        st.markdown(f"**Your Final Score: {st.session_state.score} / 5**")

        if st.session_state.score == 5:
            st.success("🚀 Stellar! You're a true space expert!")
        elif st.session_state.score >= 3:
            st.info("🌌 Great job! You know your science well.")
        else:
            st.warning("🛰️ Keep exploring. The universe has much to teach!")

        # Reset state when quiz tab is revisited
        st.session_state.quiz_started = False
        st.session_state.quiz_done = False
        st.session_state.current_q = None
        st.session_state.question_num = 0
        st.session_state.score = 0
        st.session_state.answered = False
            
elif st.session_state.active_tab == "🤖 Nova AI":
    st.title("🤖 Nova AI")
    st.markdown("Talk to Nova AI about space, science, or anything cosmic!")
    st.markdown("🚧 *This section is under development, please come back later* 🛠️")

elif st.session_state.active_tab == "📖 About":
    st.markdown("<h1 style='text-align: center;'>📖 About NovaNet</h1>", unsafe_allow_html=True)

    st.markdown("""

    ---
    
    ## 💫 What is NovaNet?
    NovaNet is your ultimate portal into the universe. This isn't just a website—it's a living, breathing hub of discovery, built to spark curiosity and unlock the mysteries of space, science, and AI. Whether you're a student, a space enthusiast, or an aspiring scientist, NovaNet is designed to guide you through the wonders of the cosmos in an interactive and engaging way.

    With beautifully organized sections covering everything from black holes to alien life, real-world missions to futuristic tech, NovaNet connects the dots between imagination and knowledge. You can dive into the unknown, test your theories, learn through smart quizzes, and even chat with Nova AI, your intelligent guide through this cosmic journey.

    NovaNet’s mission is simple yet ambitious: to inspire the next generation of explorers and thinkers by making space science accessible, fun, and futuristic—for everyone.

    ---

    ## 👦 The Story Behind It
    Hi, I’m Sarvesh Kore, a 13-year-old explorer of science, technology, and the stars. Ever since I was little, I’ve been fascinated by the mysteries of space—how black holes warp time, what lies beyond our galaxy, and whether we’re truly alone in the universe. These questions didn’t just stay in my head—they became a mission.

    I created NovaNet as part of the ADNOC ENERGYai Challenge, but it’s more than just a competition entry. It’s a reflection of my passion for learning and my dream of building tools that could help others fall in love with science too. I started with simple ideas and turned them into code, using tools like Python, Scratch, and APIs to bring NovaNet to life.

    Working on this platform taught me not just programming, but perseverance. Every error was a puzzle. Every fix was a step forward. And now, NovaNet is my way of sharing what I’ve learned—and what I continue to discover—with the world.

    ---

    ## 🧩 Platform Features
    NovaNet offers a wide range of sections designed for learning, interaction, and discovery:
    - 🔍 **Mysteries** – Dive into mind-bending theories and unexplained phenomena in the universe
    - 🪐 **Exoplanets** – Explore thousands of worlds orbiting stars beyond our solar system
    - 🚀 **Missions** – Learn about space missions from Apollo to Artemis and beyond
    - ⚙️ **Tech** – Discover the cutting-edge technology making space exploration possible
    - 🧬 **Astrobiology** – Investigate the search for life in the universe and the conditions that support it
    - ⌛ **Black Holes** – Understand time, gravity, and singularities in one of space’s most extreme phenomena
    - 📰 **News** – Stay updated with the latest space science discoveries and missions
    - 💬 **Theories** – Share your thoughts and read what others think about the universe
    - ❓ **Quizzes** – Challenge your knowledge and test your learning with smart quizzes
    - 🤖 **AI Conversations** – Chat with AI on topics like space science, missions, and technology

    ---

    ## 🏆 The ADNOC ENERGYai Challenge
    NovaNet was created as a submission for the ADNOC ENERGYai Challenge, a competition that encourages innovative uses of artificial intelligence for the future. The challenge inspired me to think big—how could AI not only solve problems, but also educate, inspire, and connect people through science?

    Through NovaNet, I’m showcasing how AI can be used to simulate space missions, explain complex topics, and even interact with users in real-time. This challenge gave me the motivation to build something that’s not just futuristic, but useful and educational for students everywhere. It’s not about winning—it's about imagining what’s possible when young minds and AI work together.

    ---

    ## 🚀 Future Plans
    NovaNet is just getting started! Here’s a glimpse of what’s coming next:

    - 🧪 New Science Section – Covering physics, chemistry, and biology to connect space with everyday science.

    - 🧠 AI-Powered Learning Paths – Personalized study journeys based on your interests, quiz scores, and topics you love.

    - 🧑‍🚀 User Accounts (Join the Crew) – Create your profile, save your progress, and join a growing community of space enthusiasts.

    - 💡 AI Assistant Upgrades (Nova AI) – Advanced features like mission simulations, interactive lessons, and intelligent Q&A.

    - 📢 Community Theory Hub – Share ideas, comment, and rate theories to fuel collaborative learning.

    - 📚 Interactive Stories & Games – Experience space through educational games, choose-your-path stories, and simulations.

    - 🌐 Multi-language Support – Making NovaNet accessible to more users around the world.

    - 🎨 Design Revamp – A sleeker, more dynamic UI to improve how users explore and learn.

    These future features aim to make NovaNet more intelligent, interactive, and global—empowering students and dreamers to explore the universe like never before.

    ---

    ## 🚧 Behind the Scenes
    Creating NovaNet has been a journey of passion, learning, and exploration. I built it entirely using Python and Streamlit, focusing on speed, simplicity, and clarity in design. From designing the layout to writing the logic behind quizzes and AI conversations, every part was hand-crafted.

    One of the main challenges was combining interactive features—like theory sharing and quizzes—into a single platform that still feels smooth and easy to use. I also worked on integrating AI capabilities using the LLaMA 4 API, which powers the Nova AI assistant.

    I had to figure out how to:

    - Structure and display large amounts of space data effectively

    - Make the interface engaging and intuitive for all users

    - Add cool, futuristic ideas while keeping the app stable

    NovaNet is still evolving. While I haven't yet implemented real-time databases like Google Sheets or Firebase, I’ve planned their integration for future updates. For now, all the content is handled locally to keep things simple as I continue developing and testing.

    What started as a simple idea is now a fully working space exploration platform—and I’m just getting started!
    
    ---

    ## 🧪 Tech Stack
    NovaNet is built using a combination of cutting-edge tools that make the platform fast, interactive, and scalable:

    - 🐍 Python – Handles the backend logic, interactivity, and structure of the platform.

    - 🌐 Streamlit – Powers the web interface, enabling rapid development of dynamic, app-like features.

    - 🤖 LLaMA 4 API – Fuels the AI Conversations section, allowing users to chat about space with smart responses.

    - 📄 Google Sheets (Coming Soon) – Will be used to store community-submitted theories and quiz data.

    - 🔐 Firebase (Coming Soon) – Will be used for secure user authentication and account features.

    This modular tech stack keeps NovaNet flexible and ready for future upgrades like user accounts, data dashboards, and more intelligent learning systems.

    ---

    ## 📅 Development Timeline
    - 💡 Idea Phase (March 2025)
    NovaNet started as an idea for the ADNOC ENERGYai Challenge. The goal: create a space knowledge platform powered by AI and made by a student for students.

    - 🛠️ Initial Build (April 2025)
    Developed the main features including Mysteries, Missions, Quizzes, and AI Conversations using Python and Streamlit. Focused on layout, design, and interactivity.

    - 🌐 Current Version (May 2025)
    Added News, Exoplanets, Tech, and Astrobiology sections. Designed theory sharing features, with plans to connect Google Sheets and Firebase for live data in future updates.

    - 🔮 Upcoming Features (June–July 2025)
    Launching the public theory database, login system, and learning paths powered by AI. Backend integration with Sheets and Firebase is next in line.

    - 🚀 Future Vision (Late 2025–2026)
    Build NovaNet into a smart, adaptive educational space assistant. Add full user profiles, community interactions, and evolving AI-based learning tools.



    ---

    ## 🎯 NovaNet's Goals
    NovaNet isn't just a website—it's a mission to make space knowledge interactive, inspiring, and accessible. These are the core goals that drive its development:

    Short-Term Goals (2025)

    - Make space science fun, visual, and understandable for all age groups

    - Add more engaging features like AI conversations, quizzes, and interactive theories

    - Grow NovaNet’s user base among students and science lovers

    - Begin integrating AI-driven tools for personalized content recommendations

    Long-Term Goals (Beyond 2025)

    - Develop Nova AI, a powerful self-learning assistant that guides users through space topics

    - Turn NovaNet into a global knowledge hub for space education powered by real-time data and AI

    - Inspire thousands of young explorers to think beyond Earth and imagine the future

    - Add community features like profiles, content bookmarking, and theory debates

    - Eventually launch NovaNet as a mobile app and open platform for schools

    ---

    ## 🧠 Meet Nova AI
    **Nova AI** is the futuristic brain of NovaNet—an intelligent assistant built to explore space knowledge with you. While still in development, Nova AI aims to become an interactive, adaptive, and insightful learning companion. It’s designed to:

    - 💬 Answer questions about space science, missions, technology, and astrobiology
    - 🧭 Guide users through complex topics using simplified explanations and visual suggestions
    - 🧠 Learn from user interactions to provide smarter, more personalized answers over time
    - 🧪 Generate quizzes, theories, and even missions using AI to keep learning fresh and fun
    - 🔭 Simulate futuristic space scenarios, helping users think like astronauts, engineers, and scientists

    In the future, Nova AI will evolve to become more autonomous—offering personalized learning paths, collaborative discussions, and real-time knowledge updates based on global space data. It’s your co-pilot for the cosmos!

    ---

    ## 🛸 Why Space?
    Space has always felt like the final frontier—full of endless mysteries, discoveries waiting to be made, and questions that challenge our imagination. What lies beyond the stars? Are we alone in the universe? How does time behave near a black hole?

    For me, the fascination began with the unknown. The idea that there's so much out there we haven’t seen or understood made me curious, excited, and determined to learn more. Space combines everything I love: science, technology, creativity, and big ideas.

    NovaNet is my way of turning that passion into something real. It’s not just a project—it’s a mission to help others discover the same wonder, to inspire future explorers, and to show how far curiosity can take us.

    ---

    ## 🧭 User Guide
    NovaNet is designed to be interactive, educational, and fun. Here's how to explore it easily:

    - 🧭 Use the top tab menu to switch between pages like Mysteries, Missions, News, and more.

    - 🧪 Try the Quizzes to test your space knowledge and get instant feedback.

    - 💬 Visit the Theories page to read and share fascinating space ideas and concepts.

    - 📰 Check the News section to stay up to date with recent discoveries and global space events.

    - 🤖 Talk to Nova AI in the AI Conversations tab—ask space questions, brainstorm theories, or get topic help.

    - 🪐 Browse deep topics like Exoplanets, Black Holes, Astrobiology, and Space Tech.

    - 🧬 Look out for upcoming features like Learning Paths and User Profiles.

    Whether you're here to learn, explore, or share ideas, NovaNet gives you the tools to dive deep into the universe—your way.
    
    ---

    ## 🌍 Impact & Vision
    NovaNet isn't just a space project—it's a mission to spark curiosity and scientific thinking in students, educators, and dreamers around the world. It aims to:

    - 🌟 Inspire young minds to explore science, AI, and the universe

    - 📡 Make space education engaging, interactive, and accessible

    - 🌐 Build a global platform where users can share, learn, and grow together

    - 🧠 Encourage the use of AI for educational innovation

    In the future, NovaNet hopes to partner with schools, science clubs, and innovators to bring this learning revolution even further.

    ---

    ## 🧑‍🚀 Join the Crew (Coming Soon)
    Soon you'll be able to create your own profile, bookmark content, and participate in community events. This feature will allow deeper interaction and sharing across NovaNet.

    ---

    ## 🎥 Behind the Code (Coming Soon)
    Planning a short documentary video about how NovaNet was built—from idea to launch. It will include behind-the-scenes coding, challenges, and design thinking.

    ---

    ## 📞 Contact Us
    I would love to hear from you! Whether you have a question about NovaNet, want to collaborate, or just want to share your thoughts about space, feel free to reach out.

    ### 📧 Email:
    You can email at: ssworld7105@gmail.com.
    ### 📱 Phone:
    Or you can call or whatsapp at: +971563711020

    ---
    
    """)

    st.markdown("""
    <div style='text-align: center;'>
        <h2>🪐 Where Will You Go Next?</h2>
        <p>The universe is vast, and your journey has only just begun. As you explore NovaNet, remember that every click, every discovery, and every theory you encounter is just another step in your adventure through the cosmos. The stars, the mysteries, and the wonders of space await you. Keep pushing your curiosity further, and who knows where your knowledge will take you next?</p>
        <p>Whether you're here to dive into black holes, chat with Nova AI, or share your own theories, remember:</p>
        <p><em>every great discovery starts with a question.</em></p>
        <p>Let's explore the universe together, one idea at a time. 🚀💫</p>
    </div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
<hr style="margin-top: 3rem; border-top: 1px solid #444;">
<div style='display: flex; justify-content: space-between; padding: 20px; font-size: 15px; color: gray;'>

    <div style="flex: 1; text-align: left;">
        <b>🚀 Where curiosity meets the cosmos...</b><br>
        Explore the mysteries of the universe with us.
    </div>

    <div style="flex: 1; text-align: center;">
        <b style="color: #00bfff;">💫 NovaNet</b><br>
        Your gateway to space knowledge
    </div>

    <div style="flex: 1; text-align: right;">
        <b>📬 Contact Us</b><br>
        ssworld7105@gmail.com<br>+971 563711020
    </div>

</div>
""", unsafe_allow_html=True)
