import streamlit as st

# Import trig page functions
from pages.trig_encyclopedia import show_trig_encyclopedia
from pages.trig_calculator import show_trig_calculator
from pages.trig_quiz import show_trig_quiz
from pages.trig_real_world import show_trig_real_world
from pages.trig_ar_unit_circle import show_trig_ar_unit_circle
from pages.trig_vr_environments import show_trig_vr_environments
from pages.trig_story_creator import show_trig_story_creator
from pages.trig_clinometer import show_trig_clinometer
from pages.trig_puzzles_games import show_trig_puzzles_games
from pages.trig_spinner_sketcher import show_trig_spinner_sketcher
from pages.trig_radian_crafts import show_trig_radian_crafts
from pages.trig_motion_waves import show_trig_motion_waves
from pages.geometry import show_geometry_page

# Initialize session state for navigation
if 'category' not in st.session_state:
    st.session_state.category = "Home"

# App Title
st.title("MathBook App: Trigonometry & Geometry for High Schoolers")
st.markdown("""
Welcome to the MathBook App! Explore Trigonometry and Geometry through interactive visualizations, clear explanations, and interactive tools. 
Select a category from the sidebar to begin learning.
""")

# Sidebar Main Categories
st.sidebar.header("Categories")
categories = {
    "🏠 Home": "Home",
    "📐 Trigonometry": "Trigonometry",
    "🔲 Geometry": "Geometry"
}

for icon_label, category in categories.items():
    if st.sidebar.button(icon_label, key=category):
        st.session_state.category = category
        if category == "Trigonometry":
            if 'trig_page' not in st.session_state:
                st.session_state.trig_page = "Encyclopedia"

# Conditional Sub-Navigation for Trigonometry
if st.session_state.category == "Trigonometry":
    st.sidebar.header("Trigonometry Tools")
    trig_pages = {
        "📚 Encyclopedia": "Encyclopedia",
        "🧮 Trig Calculator": "Trig Calculator",
        "❓ Quiz": "Quiz",
        "🌍 Real-World Applications": "Real-World Applications",
        "🔄 AR Unit Circle": "AR Unit Circle",
        "🌐 VR Environments": "VR Environments",
        "📖 Story Creator": "Story Creator",
        "📏 Clinometer Simulator": "Clinometer Simulator",
        "🧩 Puzzles & Games": "Puzzles & Games",
        "🎡 Spinner & Sketcher": "Spinner & Sketcher",
        "🎨 Radian Crafts": "Radian Crafts",
        "🚀 Motion & Waves": "Motion & Waves"
    }

    for icon_label, page_name in trig_pages.items():
        if st.sidebar.button(icon_label, key=f"trig_{page_name}"):
            st.session_state.trig_page = page_name

# Page Rendering
if st.session_state.category == "Home":
    st.header("Welcome to MathBook")
    st.markdown("""
    Choose a category from the sidebar to explore:
    - **Trigonometry**: Dive into angles, triangles, and waves with visualizations, calculators, and real-world applications.
    - **Geometry**: Learn about shapes, areas, volumes, and transformations with interactive tools.
    """)

elif st.session_state.category == "Trigonometry":
    st.header("Trigonometry")
    current_page = st.session_state.get('trig_page', "Encyclopedia")
    
    if current_page == "Encyclopedia":
        show_trig_encyclopedia()
    elif current_page == "Trig Calculator":
        show_trig_calculator()
    elif current_page == "Quiz":
        show_trig_quiz()
    elif current_page == "Real-World Applications":
        show_trig_real_world()
    elif current_page == "AR Unit Circle":
        show_trig_ar_unit_circle()
    elif current_page == "VR Environments":
        show_trig_vr_environments()
    elif current_page == "Story Creator":
        show_trig_story_creator()
    elif current_page == "Clinometer Simulator":
        show_trig_clinometer()
    elif current_page == "Puzzles & Games":
        show_trig_puzzles_games()
    elif current_page == "Spinner & Sketcher":
        show_trig_spinner_sketcher()
    elif current_page == "Radian Crafts":
        show_trig_radian_crafts()
    elif current_page == "Motion & Waves":
        show_trig_motion_waves()

elif st.session_state.category == "Geometry":
    show_geometry_page()
