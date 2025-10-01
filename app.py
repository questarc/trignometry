import streamlit as st

# Import only confirmed working page functions
from pages.trig_encyclopedia import show_trig_encyclopedia
from pages.geometry import show_geometry_page

# Initialize session state for navigation
if 'category' not in st.session_state:
    st.session_state.category = "Home"
if 'trig_page' not in st.session_state:
    st.session_state.trig_page = None

# App Title
st.title("MathBook App: Trigonometry & Geometry for High Schoolers")
st.markdown("""
Welcome to the MathBook App! Explore Trigonometry and Geometry through interactive visualizations, clear explanations, and interactive tools. 
Select a category from the sidebar to begin learning.
""")

# Sidebar with tree-like structure
st.sidebar.title("Options Tree")

# Home as top-level button
if st.sidebar.button("🏠 Home", key="category_home"):
    st.session_state.category = "Home"
    st.session_state.trig_page = None

# Trigonometry as expander with sub-page
with st.sidebar.expander("📐 Trigonometry"):
    if st.button("📚 Encyclopedia", key="trig_encyclopedia"):
        st.session_state.category = "Trigonometry"
        st.session_state.trig_page = "Encyclopedia"

# Geometry as top-level button
if st.sidebar.button("🔲 Geometry", key="category_geometry"):
    st.session_state.category = "Geometry"
    st.session_state.trig_page = None

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
    st.markdown("Select a tool from the sidebar to explore trigonometry concepts.")
    current_page = st.session_state.get('trig_page', "Encyclopedia")
    
    page_functions = {
        "Encyclopedia": show_trig_encyclopedia
    }
    
    if current_page in page_functions:
        page_functions[current_page]()
    else:
        st.error(f"Page '{current_page}' not found. Please select a Trigonometry tool from the sidebar.")

elif st.session_state.category == "Geometry":
    st.header("Geometry")
    show_geometry_page()
