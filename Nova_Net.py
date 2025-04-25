import streamlit as st
import requests
import random

st.set_page_config(page_title="Nova Net", layout="wide", page_icon="💫")

# NASA API key
API_KEY = "ZUyBjPsg0MqHf8kPZVgoZEPJlwaGuH7Fgswc7Bto"  # Replace with your own key if needed

# Function to get Astronomy Picture of the Day
def get_apod():
    url = f"https://api.nasa.gov/planetary/apod?api_key=ZUyBjPsg0MqHf8kPZVgoZEPJlwaGuH7Fgswc7Bto"
    response = requests.get(url)
    return response.json()

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


st.markdown("""<div style='text-align: center; margin-top: 2rem;'>
            <h1 style='font-size: 60px;'>Welcome to NovaNet! 💫</h1>
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
                    <h1>🌎 Home</h1>
                    <p style='text-align: center;'>Explore the universe from your screen – facts, features, and the wonders of space, all in one place.</p>
                    </div>""", unsafe_allow_html=True)
    
    st.markdown("---")
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
    
    st.markdown("---")
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

    st.markdown("---")
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
    <h2 style='text-align: center;'>🕵️‍♂️ Unsolved Mysteries of the Universe 🌌</h2>
    <p style='text-align: center;'>Here are some of the most intriguing space mysteries that remain unsolved:</p>
    """, unsafe_allow_html=True)
    st.markdown("---")
    
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
                        "<a href='https://en.wikipedia.org/wiki/Quantum_gravity' target='_blank'>Learn more</a>."},
        {"title": "The Multiverse Theory 🌐", 
         "description": "Is there more than one universe? Exploring the idea of parallel universes. "
                        "<a href='https://en.wikipedia.org/wiki/Multiverse' target='_blank'>Learn more</a>."},
        {"title": "The Search for Alien Life 👽", 
         "description": "How can we detect signs of extraterrestrial life, and why haven't we found any proof yet? "
                        "<a href='https://en.wikipedia.org/wiki/Search_for_extraterrestrial_intelligence' target='_blank'>Learn more</a>."},
        {"title": "The Origin of Cosmic Rays ⚡", 
         "description": "What causes the high-energy cosmic rays that bombard Earth, and where do they come from? "
                        "<a href='https://en.wikipedia.org/wiki/Cosmic_ray' target='_blank'>Learn more</a>."}
    ]

    col1, col2 = st.columns(2)
    
    with col1:
        for mystery in mysteries[:4]:
            st.markdown(f"""
            <div style='margin-bottom: 20px; text-align: center;'>
                <h3>{mystery['title']}</h3>
                <p>{mystery['description']}</p>
            </div>
            """, unsafe_allow_html=True)

    with col2:
        for mystery in mysteries[4:]:
            st.markdown(f"""
            <div style='margin-bottom: 20px; text-align: center;'>
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
            <div style='margin-bottom: 20px; text-align: center;'>
                <h3>{anomaly['title']}</h3>
                <p>{anomaly['description']}</p>
            </div>
            """, unsafe_allow_html=True)

    with col2:
        for anomaly in anomalies[3:]:
            st.markdown(f"""
            <div style='margin-bottom: 20px; text-align: center;'>
                <h3>{anomaly['title']}</h3>
                <p>{anomaly['description']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("<h2 style='text-align: center;'>🧠 Theories & Hypotheses</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div style='text-align: center;'>
        <h4>🌌 Dark Matter Web</h4>
        <p>What if it's the intelligent framework of the universe?</p>
        <a href='https://en.wikipedia.org/wiki/Dark_matter' target='_blank'>🔗 Learn More</a>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style='text-align: center; margin-top: 2rem;'>
        <h4>💥 White Holes</h4>
        <p>Theoretical opposites of black holes. Could they exist?</p>
        <a href='https://en.wikipedia.org/wiki/White_hole' target='_blank'>🔗 Learn More</a>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style='text-align: center;'>
        <h4>🧬 Shadow Biospheres</h4>
        <p>Alien life forms we can't detect with current tools?</p>
        <a href='https://en.wikipedia.org/wiki/Shadow_biosphere' target='_blank'>🔗 Learn More</a>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style='text-align: center; margin-top: 2rem;'>
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
    <p><i>“Wow!” – the signal that still puzzles scientists.</i></p>
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
    <h2>🚀 Europa Clipper</h4>
    <h6>Launched in 2024, Europa Clipper will explore Jupiter’s icy moon Europa to determine if it could support life. It will carry a suite of scientific instruments to scan the moon’s surface, subsurface ocean, and magnetic environment.</h6>
    <a href='https://europa.nasa.gov/' target='_blank'>🔗 Learn More</a>
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

elif st.session_state.active_tab == "❓ Quizzes":
    st.title("❓ Interactive Quizzes")
    st.header("Space Explorer Levels")
    st.write("User progress tracking and quiz results sharing.")
    st.write("AI-generated custom quizzes will be created after 3 completions.")

elif st.session_state.active_tab == "🤖 AI Conversations":
    st.title("🤖 AI Conversations")
    st.markdown("Talk to Gemini AI about space, science, or anything cosmic!")

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
